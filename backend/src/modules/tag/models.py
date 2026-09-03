from sqlalchemy import Column, String, ForeignKey, Index
from src.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid
from sqlalchemy.orm import relationship

class TagModel(Base):
    __tablename__ = 'tags'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    name = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False)

    tasks = relationship(
        "TaskModel",
        secondary="tasks_tags",
        back_populates="tags",
        lazy="selectin"
    )

class TaskTag(Base):
    __tablename__ = 'tasks_tags'

    tag_id = Column(UUID(as_uuid=True), ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    __table_args__ = (
        Index('idx_task_tag_task_id', 'task_id'),
    )