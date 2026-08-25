from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class TagResponse(BaseModel):
    id: UUID
    name: str
    color: str
    tasks: list[UUID] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)

class TagShortResponse(BaseModel):
    id: UUID
    name: str
    color: str

    model_config = ConfigDict(from_attributes=True)

class CreateTag(BaseModel):
    name: str
    color: str