from pydantic import BaseModel, ConfigDict
from typing import List, Optional
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
    dashboards: Optional[List[UUID]] = []

    model_config = ConfigDict(from_attributes=True)