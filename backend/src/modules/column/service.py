from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from ..task.models import TaskModel

async def get_tasks_for_column(session: AsyncSession, column_id: UUID):
    tasks = await session.execute(
        select(TaskModel).where(TaskModel.column_id == column_id)
        .order_by(TaskModel.position)
    )

    return tasks.scalars().all()