from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from pwdlib import PasswordHash
from uuid import UUID

from .mapper import user_to_response
from .models import UserModel, AssigneeModel, ViewerModel
from .schemas import Register, Login, UserResponse
from ..task.models import TaskModel
from ..dashboard.models import DashboardModel

password_hash = PasswordHash.recommended()

async def get_user_by_id(session: AsyncSession, user_id: UUID):
    user = await session.get(UserModel, user_id)

    if not user:
        return None
    
    return user_to_response(user)

async def create(session: AsyncSession, user: Register) -> UserModel | None:
    user_data = user.model_dump()
    user_data["password"] = password_hash.hash(user.password)

    username_result = await session.execute(
        select(UserModel.id).where(UserModel.username == user.username)
    )

    if username_result.scalar_one_or_none() is not None:
        return None

    email_result = await session.execute(
        select(UserModel.id).where(UserModel.email == user.email)
    )

    if email_result.scalar_one_or_none() is not None:
        return None

    new_user = UserModel(**user_data)

    session.add(new_user)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        return None

    await session.refresh(new_user)

    return user_to_response(new_user)

async def login_user(session: AsyncSession, user: Login) -> UserModel | None:
    result = await session.execute(
        select(UserModel).where(UserModel.email == user.email)
    )
    stored_user = result.scalar_one_or_none()

    if not stored_user or not password_hash.verify(user.password, stored_user.password):
        return None

    return user_to_response(stored_user)

async def delete(session: AsyncSession, user_id: UUID):
    user = await session.get(UserModel, user_id)

    if not user:
        return None

    await session.delete(user)
    await session.commit()
    return True

async def user_tasks(session: AsyncSession, user_id: UUID):
    user = await session.get(UserModel, user_id)

    if not user:
        return None

    result = await session.execute(
        select(TaskModel)
        .join(AssigneeModel, AssigneeModel.task_id == TaskModel.id)
        .where(AssigneeModel.user_id == user_id)
    )
    return result.scalars().all()

async def user_dashboards(session: AsyncSession, user_id: UUID):
    user = await session.get(UserModel, user_id)
    
    if not user:
        return None

    result = await session.execute(
        select(DashboardModel)
        .join(ViewerModel, ViewerModel.dashboard_id == DashboardModel.id)
        .where(ViewerModel.user_id == user_id)
    )
    return result.scalars().all()

async def get_dashboards_where_user_is_own(session: AsyncSession, user_id: UUID):
    result = await session.execute(
        select(DashboardModel)
        .where(DashboardModel.author_id == user_id)
    )
    return result.scalars().all()

async def add_user_to_task(
    session: AsyncSession,
    user_id: UUID,
    task_id: UUID,
) -> bool | None:
    user = await session.get(UserModel, user_id)
    task = await session.get(TaskModel, task_id)

    if user is None or task is None:
        return None

    existing_assignee = await session.execute(
        select(AssigneeModel).where(
            AssigneeModel.user_id == user_id,
            AssigneeModel.task_id == task_id,
        )
    )

    if existing_assignee.scalar_one_or_none() is not None:
        return False

    assignee = AssigneeModel(user_id=user_id, task_id=task_id)

    session.add(assignee)
    await session.commit()
    return True


async def remove_user_from_task(
    session: AsyncSession,
    user_id: UUID,
    task_id: UUID,
) -> bool | None:
    result = await session.execute(
        select(AssigneeModel).where(
            AssigneeModel.user_id == user_id,
            AssigneeModel.task_id == task_id,
        )
    )
    assignee = result.scalar_one_or_none()

    if assignee is None:
        return None

    await session.delete(assignee)
    await session.commit()
    return True

async def add_user_to_dashboard(
    session: AsyncSession,
    user_id: UUID,
    dashboard_id: UUID,
) -> bool | None:
    user = await session.get(UserModel, user_id)
    dashboard = await session.get(DashboardModel, dashboard_id)

    if user is None or dashboard is None:
        return None

    existing_viewer = await session.execute(
        select(ViewerModel).where(
            ViewerModel.user_id == user_id,
            ViewerModel.dashboard_id == dashboard_id,
        )
    )

    if existing_viewer.scalar_one_or_none() is not None:
        return False

    viewer = ViewerModel(user_id=user_id, dashboard_id=dashboard_id)

    session.add(viewer)
    await session.commit()
    return True

async def remove_user_from_dashboard(
    session: AsyncSession,
    user_id: UUID,
    dashboard_id: UUID,
) -> bool | None:
    result = await session.execute(
        select(ViewerModel).where(
            ViewerModel.user_id == user_id,
            ViewerModel.dashboard_id == dashboard_id,
        )
    )
    viewer = result.scalar_one_or_none()

    if viewer is None:
        return None

    await session.delete(viewer)
    await session.commit()
    return True

async def search_users(session: AsyncSession, query: str, limit: int = 20) -> list[UserResponse]:
    if not query.strip():
        return []

    search_pattern = f"%{query.strip()}%"

    result = await session.execute(
        select(UserModel).where(
            UserModel.username.ilike(search_pattern) | UserModel.email.ilike(search_pattern)).limit(limit))

    users = result.scalars().all()

    return [user_to_response(user) for user in users]