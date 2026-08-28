from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.core.database import get_db
from ..task.schemas import TaskShortResponse
from . import schemas
from . import service

router = APIRouter(prefix="/columns", tags=["Columns"])

@router.get("/{column_id}/tasks", response_model=list[TaskShortResponse])
async def get_column_tasks( column_id: UUID, session: AsyncSession = Depends(get_db),
):
    tasks = await service.get_tasks_for_column(session=session, column_id=column_id)

    if tasks is None:
        raise HTTPException(status_code=404, detail="Tasks not found")

    return tasks

@router.get("/{dashboard_id}/columns", response_model=list[schemas.ColumnShortResponse])
async def get_column_for_dashboard( dashboard_id: UUID, session: AsyncSession = Depends(get_db),
):
    return await service.get_columns_by_dashboard_id(session=session, dashboard_id=dashboard_id)

@router.get("", response_model=list[schemas.ColumnShortResponse])
async def get_columns( session: AsyncSession = Depends(get_db),
):
    return await service.get_all_columns(session=session)

@router.get("/{column_id}", response_model=schemas.ColumnShortResponse)
async def get_column(column_id: UUID, session: AsyncSession = Depends(get_db),
):
    column = await service.get_column_by_id(session=session, column_id=column_id)

    if column is None:
        raise HTTPException(status_code=404, detail="Column not found")

    return column

@router.post("", response_model=schemas.ColumnResponse)
async def create_column(data: schemas.CreateColumn, session: AsyncSession = Depends(get_db)):
    return await service.create_column(session=session, data=data)

@router.put("/{column_id}", response_model=schemas.ColumnResponse)
async def update_column(column_id: UUID, data: schemas.UpdateColumn, session: AsyncSession = Depends(get_db)):
    column = await service.update_column(session=session, data=data, column_id=column_id)

    if column is None:
        raise HTTPException(status_code=404, detail="Column not found")

    return column

@router.delete("/{column_id}")
async def delete_column(column_id: UUID, session: AsyncSession = Depends(get_db)):
    success = await service.delete(session=session, column_id=column_id)

    if success is None:
        raise HTTPException(status_code=404, detail="Column not found")

    return {'detail': 'Column deleted'}