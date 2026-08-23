from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional
from uuid import UUID
import enum

class StatusEnum(str, enum.Enum):
    backlog = "backlog"
    ready = "ready"
    in_progress = "in_progress"
    in_viewer = "in_viewer"
    done = "done"
    overdue = "overdue"

class ColumnResponse(BaseModel):
    id: UUID
    tasks: list[UUID] = Field(default_factory=list)
    status: StatusEnum

    model_config = ConfigDict(from_attributes=True)

class CreateColumn(BaseModel):
    status: StatusEnum

class UpdateColumn(BaseModel):
    status: Optional[StatusEnum] = None
    tasks: Optional[list[UUID]] = None