from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.core.database import get_db
from ..tag.schemas import TagShortResponse
from ..user.schemas import UserShortResponse
from . import schemas
from . import service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/{task_id}/assignees", response_model=list[UserShortResponse])
async def get_task_assignees( task_id: UUID, session: AsyncSession = Depends(get_db),
):
    assignees = await service.task_assignees(session=session, task_id=task_id)

    if assignees is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return assignees

@router.get("/{task_id}/tags", response_model=list[TagShortResponse])
async def get_task_tags(
    task_id: UUID,
    session: AsyncSession = Depends(get_db),
):
    tags = await service.task_tags(session=session, task_id=task_id)

    if tags is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return tags

@router.get("", response_model=list[schemas.TaskResponse])
async def get_tasks(session: AsyncSession = Depends(get_db)):
    return await service.get_all_task(session=session)

@router.get("/{task_id}", response_model=schemas.TaskResponse)
async def get_task(task_id: UUID, session: AsyncSession = Depends(get_db)):
    task = await service.get_task_by_id(session=session, task_id=task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("", response_model=schemas.TaskResponse)
async def create_tasks(data: schemas.CreateTask, session: AsyncSession = Depends(get_db)):
    return await service.create_task(session=session, task=data)

@router.put("/{task_id}", response_model=schemas.TaskResponse)
async def update_tasks(task_id: UUID, data: schemas.UpdateTask, session: AsyncSession = Depends(get_db)):
    updated_task = await service.update_task(session=session, task=data, task_id=task_id)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}")
async def delete_tasks(task_id: UUID, session: AsyncSession = Depends(get_db)):
    success = await service.delete_task(session=session, task_id=task_id)

    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"detail": "Task deleted"}