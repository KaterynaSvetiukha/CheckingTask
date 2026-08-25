from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from .schemas import CreateTag
from .models import TagModel, TaskTag
from .mapper import tag_to_response
from ..task.models import TaskModel


async def get_all_tags(session: AsyncSession):
    result = await session.execute(
        select(TagModel).order_by(TagModel.name)
    )

    tags = result.scalars().all()

    return [tag_to_response(tag) for tag in tags]

async def create_tag(session: AsyncSession, tag: CreateTag) -> TagModel:
    new_tag = TagModel(**tag.model_dump())

    session.add(new_tag)
    await session.commit()
    await session.refresh(new_tag)

    return new_tag

async def delete_tag(session: AsyncSession, tag_id: UUID) -> bool | None:
    db_tag = await session.get(TagModel, tag_id)

    if db_tag is None:
        return None

    await session.delete(db_tag)
    await session.commit()

    return True

async def get_tasks_for_tag(session: AsyncSession, tag_id: UUID):
    result = await session.execute(
        select(TaskModel)
        .join(TaskTag, TaskTag.task_id == TaskModel.id)
        .where(TaskTag.tag_id == tag_id)
    )

    return result.scalars().all()

async def add_tag_to_task(session: AsyncSession, tag_id: UUID, task_id: UUID) -> bool:
    task_tag = TaskTag(task_id=task_id, tag_id=tag_id)

    session.add(task_tag)
    await session.commit()
    return True

async def remove_tag_to_task(session: AsyncSession, tag_id: UUID, task_id: UUID) -> bool | None:
    task_tag = await session.execute(
        select(TaskTag).where(TaskTag.task_id == task_id,
                              TaskTag.tag_id == tag_id,))

    result = task_tag.scalar_one_or_none()

    if result is None:
        return None

    await session.delete(result)
    await session.commit()

    return True