from pydantic import BaseModel, ConfigDict
from uuid import UUID

class TagResponse(BaseModel):
    id: UUID
    name: str
    color: str

    model_config = ConfigDict(from_attributes=True)

class CreateTag(BaseModel):
    name: str
    color: str