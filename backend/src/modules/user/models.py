from sqlalchemy import Column, String, ForeignKey, Index
from src.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(256), nullable=False, index=True, unique=True)
    password = Column(String(256), nullable=False)

class AssigneeModel(Base):
    __tablename__ = 'assignees'

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        Index('idx_assignee_task_id', 'task_id')
    )

class ViewerModel(Base):
    __tablename__ = 'viewers'

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    dashboard_id = Column(UUID(as_uuid=True), ForeignKey("dashboards.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        Index('idx_viewer_dashboard_id', 'dashboard_id')
    )