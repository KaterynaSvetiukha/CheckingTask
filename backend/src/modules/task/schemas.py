from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from uuid import UUID
import enum

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    tags: Optional[List[UUID]] = []
    priority: PriorityEnum
    time_to: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    assignees: Optional[List[UUID]] = []
    author_id: UUID
    column_id: UUID
    position: str

    model_config = ConfigDict(from_attributes=True)

class CreateTask(BaseModel):
    title: str
    description: Optional[str] = None
    tags: Optional[List[UUID]] = []
    priority: PriorityEnum
    time_to: Optional[datetime] = None
    assignees: Optional[List[UUID]] = []
    column_id: UUID

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[UUID]] = None
    priority: Optional[PriorityEnum] = None
    time_to: Optional[datetime] = None
    assignees: Optional[List[UUID]] = None
    column_id: Optional[UUID] = None
