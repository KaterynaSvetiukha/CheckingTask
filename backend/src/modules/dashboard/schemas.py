from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class DashboardResponse(BaseModel):
    id: UUID
    name: str
    columns: Optional[List[UUID]] = []
    members: Optional[List[UUID]] = []
    author_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class CreateDashboard(BaseModel):
    name: str
    members: Optional[List[UUID]] = []

class UpdateDashboard(BaseModel):
    name: Optional[str] = None
    members: Optional[List[UUID]] = None
    columns: Optional[List[UUID]] = None