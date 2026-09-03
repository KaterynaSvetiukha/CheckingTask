from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from ..task.models import TaskModel
from .models import ColumnModel
from .mapper import column_to_response
from .schemas import CreateColumn, UpdateColumn, ColumnResponse

async def get_tasks_for_column(session: AsyncSession, column_id: UUID):
    tasks = await session.execute(
        select(TaskModel).where(TaskModel.column_id == column_id)
        .order_by(TaskModel.position)
    )

    return tasks.scalars().all()


async def get_columns_by_dashboard_id(session: AsyncSession, dashboard_id: UUID):
    columns = await session.execute(
        select(ColumnModel).where(ColumnModel.dashboard_id == dashboard_id)
    )

    return columns.scalars().all()

async def get_all_columns(session: AsyncSession):
    result = await session.execute(select(ColumnModel))
    columns = result.scalars().all()

    return [column_to_response(column) for column in columns]

async def get_column_by_id(session: AsyncSession, column_id: UUID) -> ColumnResponse | None:
    column = await session.get(ColumnModel, column_id)

    if column is None:
        return None

    return column_to_response(column)

async def create_column(session: AsyncSession, data: CreateColumn) -> ColumnResponse:
    new_column = ColumnModel(**data.model_dump())

    session.add(new_column)
    await session.commit()
    await session.refresh(new_column)

    return column_to_response(new_column)

async def update_column(session: AsyncSession, data: UpdateColumn, column_id: UUID) -> ColumnResponse | None:
    column = await session.get(ColumnModel, column_id)
    
    if column is None:
        return None

    update_data = data.model_dump(exclude_none=True)
    
    for key, value in update_data.items():
        setattr(column, key, value)

    await session.commit()
    await session.refresh(column)

    return column_to_response(column)

async def delete(session: AsyncSession, column_id: UUID) -> bool | None:
    column = await session.get(ColumnModel, column_id)
    
    if column is None:
        return None

    await session.delete(column)
    await session.commit()
    return True