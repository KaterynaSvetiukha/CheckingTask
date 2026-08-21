from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from src.core.database import Base
import enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskModel(Base):
    __tablename__ = 'task'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(Enum(PriorityEnum, name="priority_enum"), nullable=False, default=PriorityEnum.medium)
    time_to = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    position = Column(String, nullable=False)

    column_id = Column(UUID(as_uuid=True), ForeignKey("column.id", ondelete="CASCADE"))
    author_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"))

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)

class TaskTag(Base):
    __tablename__ = 'task_tag'

    tag_id = Column(UUID(as_uuid=True), ForeignKey("tag.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("task.id", ondelete="CASCADE"), primary_key=True)