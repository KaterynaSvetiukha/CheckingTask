from sqlalchemy import Column, String, ForeignKey
from src.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

class AssigneeModel(Base):
    __tablename__ = 'assignee'

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("task.id", ondelete="CASCADE"), primary_key=True)

class ViewerModel(Base):
    __tablename__ = 'viewer'

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    dashboard_id = Column(UUID(as_uuid=True), ForeignKey("dashboard.id", ondelete="CASCADE"), primary_key=True)