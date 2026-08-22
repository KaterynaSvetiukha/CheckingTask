from sqlalchemy import Column, DateTime, ForeignKey
from src.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid

class DashboardModel(Base):
    __tablename__ = 'dashboards'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)

    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True)