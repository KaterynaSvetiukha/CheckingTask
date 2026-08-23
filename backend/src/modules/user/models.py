from sqlalchemy import Column, String, ForeignKey, Index
from src.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False)

    __table_args__ = (
        Index('idx_username_email', 'username', 'email'),
    )

    dashboards = relationship(
        "DashboardModel",
        secondary="viewers",
        back_populates="members",
    )

    assigned_tasks = relationship(
        "TaskModel",
        secondary="assignees",
        back_populates="assignees",
    )

    authored_tasks = relationship(
        "TaskModel",
        foreign_keys="TaskModel.author_id",
        back_populates="author",
    )

    authored_dashboards = relationship(
        "DashboardModel",
        foreign_keys="DashboardModel.author_id",
        back_populates="author",
    )

class AssigneeModel(Base):
    __tablename__ = 'assignees'

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        Index('idx_assignee_task_id', 'task_id'),
    )

class ViewerModel(Base):
    __tablename__ = 'viewers'

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    dashboard_id = Column(UUID(as_uuid=True), ForeignKey("dashboards.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        Index('idx_viewer_dashboard_id', 'dashboard_id'),
    )