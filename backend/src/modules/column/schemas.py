from pydantic import BaseModel, ConfigDict
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
    tasks: Optional[List[UUID]] = []
    status: StatusEnum

    model_config = ConfigDict(from_attributes=True)

class CreateColumn(BaseModel):
    status: StatusEnum

class UpdateColumn(BaseModel):
    status: Optional[StatusEnum] = None
    tasks: Optional[List[UUID]] = None