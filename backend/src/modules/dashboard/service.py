from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from .models import DashboardModel
from .mapper import dashboard_to_response
from ..user.models import UserModel
from .schemas import CreateDashboard, UpdateDashboard, DashboardResponse
from ..column.models import ColumnModel, StatusEnum

DEFAULT_COLUMNS = [
    StatusEnum.backlog,
    StatusEnum.ready,
    StatusEnum.in_progress,
    StatusEnum.in_viewer,
    StatusEnum.done,
    StatusEnum.overdue,
]

async def get_dashboard_by_id(session: AsyncSession, dashboard_id: UUID):
    db_dashboard = await session.get(DashboardModel, dashboard_id)

    if db_dashboard is None:
        return None

    return dashboard_to_response(db_dashboard)

async def create_dashboard(session: AsyncSession, data: CreateDashboard, author_id: UUID) -> DashboardResponse:
    new_dashboard = DashboardModel(**data.model_dump(exclude={'members'}))
    new_dashboard.author_id = author_id

    member_ids = set(data.members) if data.members else set()
    member_ids.add(author_id)

    result = await session.execute(select(UserModel).where(UserModel.id.in_(member_ids)))
    new_dashboard.members = list(result.scalars().all())

    session.add(new_dashboard)
    await session.flush()

    for status in DEFAULT_COLUMNS:
        session.add(ColumnModel(dashboard_id=new_dashboard.id, status=status))

    await session.commit()
    await session.refresh(new_dashboard)

    return dashboard_to_response(new_dashboard)

async def update_dashboard(session: AsyncSession, data: UpdateDashboard, dashboard_id: UUID) -> DashboardResponse | None:
    dashboard = await session.get(DashboardModel, dashboard_id)

    if dashboard is None:
        return None

    update_data = data.model_dump(exclude_none=True)
    
    for key, value in update_data.items():
        setattr(dashboard, key, value)

    await session.commit()
    await session.refresh(dashboard)

    return dashboard_to_response(dashboard)

async def delete(session: AsyncSession, dashboard_id: UUID) -> bool | None:
    dashboard = await session.get(DashboardModel, dashboard_id)
    
    if dashboard is None:
        return None

    await session.delete(dashboard)
    await session.commit()
    return True

    