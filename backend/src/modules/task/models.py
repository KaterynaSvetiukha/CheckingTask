from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, Index
from src.core.database import Base
import enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid

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
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    position = Column(String(100), nullable=False, unique=True)

    column_id = Column(UUID(as_uuid=True), ForeignKey("columns.id", ondelete="CASCADE"))
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True)

    __table_args__ = (
        Index('idx_column_position", "column_id", "position')
    )

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    name = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False)

class TaskTag(Base):
    __tablename__ = 'tasks_tags'

    tag_id = Column(UUID(as_uuid=True), ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        Index('idx_task_tag_task_id', 'task_id')
    )