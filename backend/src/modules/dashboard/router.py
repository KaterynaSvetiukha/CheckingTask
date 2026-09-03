from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.core.database import get_db
from . import schemas
from . import service

router = APIRouter(prefix="/dashboards", tags=["Dashboards"])

@router.get("/{dashboard_id}", response_model=schemas.DashboardResponse)
async def get_dashboard(dashboard_id: UUID, session: AsyncSession = Depends(get_db)):
    dashboard = await service.get_dashboard_by_id(session=session, dashboard_id=dashboard_id)

    if dashboard is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dashboard not found')

    return dashboard

@router.post("", response_model=schemas.DashboardResponse)
async def post_dashboard(data: schemas.CreateDashboard, author_id: UUID, session: AsyncSession = Depends(get_db)):
    return await service.create_dashboard(session=session, data=data, author_id=author_id)

@router.put("/{dashboard_id}", response_model=schemas.DashboardResponse)
async def put_dashboard(dashboard_id: UUID, data: schemas.UpdateDashboard, session: AsyncSession = Depends(get_db)):
    dashboard = await service.update_dashboard(session=session, dashboard_id=dashboard_id, data=data)

    if dashboard is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dashboard not found')

    return dashboard

@router.delete("/{dashboard_id}")
async def delete_dashboard(dashboard_id: UUID, session: AsyncSession = Depends(get_db)):
    success = await service.delete(session=session, dashboard_id=dashboard_id)

    if success is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dashboard not found')

    return {'detail': 'Dashboard deleted'}