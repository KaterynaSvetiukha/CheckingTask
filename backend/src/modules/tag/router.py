from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.core.database import get_db
from . import schemas
from . import service

router = APIRouter(prefix="/tags", tags=["Tags"])

@router.post("/{tag_id}/tasks/{task_id}", status_code=201)
async def add_tag_to_task(
    tag_id: UUID,
    task_id: UUID,
    session: AsyncSession = Depends(get_db),
):
    result = await service.add_tag_to_task(
        session=session,
        tag_id=tag_id,
        task_id=task_id,
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Tag or task not found")

    if result is False:
        raise HTTPException(status_code=409, detail="Tag is already assigned to task")

    return {"detail": "Tag added to task"}

@router.get("", response_model=list[schemas.TagResponse])
async def get_tags(session: AsyncSession = Depends(get_db)):
    return await service.get_all_tags(session=session)

@router.get("/{tag_id}/tasks")
async def delete_tag(tag_id: UUID, session: AsyncSession = Depends(get_db)):
    data = await service.get_tasks_for_tag(session=session, tag_id=tag_id)

    if data is None:
        raise HTTPException('404', 'Tag not found')

    return data

@router.post("", response_model=list[schemas.TagResponse])
async def create_tags(data: schemas.CreateTag, session: AsyncSession = Depends(get_db)):
    return await service.create_tag(session=session, tag=data)



@router.delete("/{tag_id}")
async def delete_tag(tag_id: UUID, session: AsyncSession = Depends(get_db)):
    success = await service.delete_tag(session=session, tag_id=tag_id)

    if not success:
        raise HTTPException('404', 'Tag not found')

    return {"detail": "Tag deleted"}

@router.delete("/{tag_id}/tasks/{task_id}")
async def delete_tag_from_task(
    tag_id: UUID,
    task_id: UUID,
    session: AsyncSession = Depends(get_db),
):
    result = await service.remove_tag_from_task(
        session=session,
        tag_id=tag_id,
        task_id=task_id,
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Tag or task not found")

    return {"detail": "Tag added to task"}