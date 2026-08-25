from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import TaskModel
from ..user.models import AssigneeModel, UserModel
from ..tag.models import TagModel, TaskTag
from .schemas import CreateTask, UpdateTask
from .mapper import task_to_response

async def get_all_task(session: AsyncSession):
    result = await session.execute(select(TaskModel))
    tasks = result.scalars().all()
    return [task_to_response(task) for task in tasks]

async def create_task(session: AsyncSession, task: CreateTask) -> TaskModel:
    new_task = TaskModel(**task.model_dump())

    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)

    return new_task

async def update_task(session: AsyncSession, task: UpdateTask, task_id: str) -> TaskModel:
    db_task = await session.get(TaskModel, task_id)

    if not db_task:
        return None

    # exclude_none=True - для полей которые не надо менять
    # бек будет игнорировать пустые значения
    update_data = task.model_dump(exclude_none=True)

    for key, value in update_data.items():
        setattr(db_task, key, value)

    await session.commit()
    await session.refresh(db_task)

    return db_task

async def delete_task(session: AsyncSession, task_id: str):
    db_task = await session.get(TaskModel, task_id)

    if not db_task:
        return None

    await session.delete(db_task)
    await session.commit()
    return True

async def get_task_by_id(session: AsyncSession, task_id: str):
    db_task = await session.get(TaskModel, task_id)

    if not db_task:
        return None

    return task_to_response(db_task)

async def task_assignees(session: AsyncSession, task_id: str):
    task = await session.get(TaskModel, task_id)

    if not task:
        return None

    result = await session.execute(
        select(UserModel)
        .join(AssigneeModel, AssigneeModel.user_id == UserModel.id)
        .where(AssigneeModel.task_id == task_id)
    )
    return result.scalars().all()

async def task_tags(session: AsyncSession, task_id: str):
    task = await session.get(TaskModel, task_id)

    if not task:
        return None

    result = await session.execute(
        select(TagModel)
        .join(TaskTag, TaskTag.tag_id == TagModel.id)
        .where(TaskTag.task_id == task_id)
    )
    return result.scalars().all()