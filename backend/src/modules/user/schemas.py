from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class Register(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    dashboards: list[UUID] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)

class UserShortResponse(BaseModel):
    id: UUID
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)