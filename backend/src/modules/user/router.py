from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from . import schemas
from . import service
from ..dashboard.schemas import DashboardShortResponse
from ..task.schemas import TaskShortResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/login", response_model=schemas.UserResponse)
async def login(data: schemas.Login, session: AsyncSession = Depends(get_db)):
    user = await service.login_user(session=session, user=data)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        )

    return user

@router.get("/{user_id}", response_model=schemas.UserResponse)
async def get_user(user_id: str, session: AsyncSession = Depends(get_db)):
    user = await service.get_user_by_id(session=session, user_id=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/assigned-tasks", response_model=TaskShortResponse)
async def get_assigned_tasks(user_id: str, session: AsyncSession = Depends(get_db)):
    assigned_tasks = await service.user_tasks(session=session, user_id=user_id)

    if assigned_tasks is None:
        raise HTTPException(status_code=404, detail="User not found")

    return assigned_tasks

@router.get("/{user_id}/dashboards", response_model=DashboardShortResponse)
async def get_user_dashboards(user_id: str, session: AsyncSession = Depends(get_db)):
    user_dashboards = await service.user_dashboards(session=session, user_id=user_id)

    if user_dashboards is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_dashboards

@router.post("", response_model=schemas.UserResponse)
async def post_user(data: schemas.Register, session: AsyncSession = Depends(get_db)):
    user = await service.create(session=session, user=data)

    if user is None:
        raise HTTPException(status_code=409, detail="Username or email already exists")

    return user

@router.delete("/{user_id}")
async def delete_user(user_id: str, session: AsyncSession = Depends(get_db)):
    success = await service.delete(session=session, user_id=user_id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": "User deleted"}