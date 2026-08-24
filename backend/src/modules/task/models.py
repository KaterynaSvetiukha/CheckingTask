from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, Index
from src.core.database import Base
import enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid
from sqlalchemy.orm import relationship

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    title = Column(String(100), nullable=False)
    description = Column(String(256), nullable=True)
    priority = Column(Enum(PriorityEnum, name="priority_enum"), nullable=False, default=PriorityEnum.medium)
    time_to = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    position = Column(String(100), nullable=False)

    column_id = Column(UUID(as_uuid=True), ForeignKey("columns.id", ondelete="CASCADE"), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)

    __table_args__ = (
        Index("idx_column_position", "column_id", "position"),
    )

    column = relationship(
        "ColumnModel",
        back_populates="tasks",
    )

    author = relationship(
        "UserModel",
        foreign_keys=[author_id],
        back_populates="authored_tasks",
    )

    assignees = relationship(
        "UserModel",
        secondary="assignees",
        back_populates="assigned_tasks",
    )

    tags = relationship(
        "TagModel",
        secondary="tasks_tags",
        back_populates="tasks",
    )