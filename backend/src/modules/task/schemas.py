from pydantic import BaseModel, ConfigDict, Field
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
    tags: list[UUID] = Field(default_factory=list)
    priority: PriorityEnum
    time_to: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    assignees: list[UUID] = Field(default_factory=list)
    author_id: UUID
    column_id: UUID
    position: str

    model_config = ConfigDict(from_attributes=True)

class CreateTask(BaseModel):
    title: str
    description: Optional[str] = None
    tags: list[UUID] = Field(default_factory=list)
    priority: PriorityEnum
    time_to: Optional[datetime] = None
    assignees: list[UUID] = Field(default_factory=list)
    column_id: UUID

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[list[UUID]] = None
    priority: Optional[PriorityEnum] = None
    time_to: Optional[datetime] = None
    assignees: Optional[list[UUID]] = None
    column_id: Optional[UUID] = None
