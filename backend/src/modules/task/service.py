from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import TaskModel
from ..user.models import AssigneeModel, UserModel
from ..tag.models import TagModel, TaskTag
from .schemas import CreateTask, UpdateTask
from .mapper import task_to_response
from uuid import UUID
from ..column.models import ColumnModel

async def get_all_task(session: AsyncSession):
    result = await session.execute(select(TaskModel))
    tasks = result.scalars().all()
    return [task_to_response(task) for task in tasks]

async def create_task(session: AsyncSession, task: CreateTask) -> TaskModel:
    new_task = TaskModel(**task.model_dump(exclude={'tags', 'assignees'}))

    if task.tags:
        tags = (await session.execute(select(TagModel).where(TagModel.id.in_(task.tags)))).scalars().all()
        new_task.tags = tags
    else:
        new_task.tags = []

    if task.assignees:
        assignees = (await session.execute(select(UserModel).where(UserModel.id.in_(task.assignees)))).scalars().all()
        new_task.assignees = assignees
    else:
        new_task.assignees = []
    

    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)

    return task_to_response(new_task)

async def update_task(session: AsyncSession, task: UpdateTask, task_id: UUID) -> TaskModel:
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

async def delete_task(session: AsyncSession, task_id: UUID):
    db_task = await session.get(TaskModel, task_id)

    if not db_task:
        return None

    await session.delete(db_task)
    await session.commit()
    return True

async def get_task_by_id(session: AsyncSession, task_id: UUID):
    db_task = await session.get(TaskModel, task_id)

    if not db_task:
        return None

    return task_to_response(db_task)

async def task_assignees(session: AsyncSession, task_id: UUID):
    task = await session.get(TaskModel, task_id)

    if not task:
        return None

    result = await session.execute(
        select(UserModel)
        .join(AssigneeModel, AssigneeModel.user_id == UserModel.id)
        .where(AssigneeModel.task_id == task_id)
    )
    return result.scalars().all()

async def task_tags(session: AsyncSession, task_id: UUID):
    task = await session.get(TaskModel, task_id)

    if not task:
        return None

    result = await session.execute(
        select(TagModel)
        .join(TaskTag, TaskTag.tag_id == TagModel.id)
        .where(TaskTag.task_id == task_id)
    )
    return result.scalars().all()

async def move_task(session: AsyncSession, task_id: UUID, column_id: UUID, position: str) -> TaskModel | None: 
    task = await session.get(TaskModel, task_id)

    if task is None:
        return None

    column = await session.get(ColumnModel, column_id)

    if column is None:
        return None

    task.column_id = column_id
    task.position = position

    await session.commit()
    await session.refresh(task)

    return task