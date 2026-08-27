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