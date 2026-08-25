from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class DashboardResponse(BaseModel):
    id: UUID
    name: str
    columns: list[UUID] = Field(default_factory=list)
    members: list[UUID] = Field(default_factory=list)
    author_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class CreateDashboard(BaseModel):
    name: str
    members: list[UUID] = Field(default_factory=list)

class UpdateDashboard(BaseModel):
    name: Optional[str] = None
    members: Optional[list[UUID]] = None
    columns: Optional[list[UUID]] = None

class DashboardShortResponse(BaseModel):
    id: UUID
    name: str
    author_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)