from sqlalchemy import Column, DateTime, ForeignKey, String
from src.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid_utils as uuid
from sqlalchemy.orm import relationship

class DashboardModel(Base):
    __tablename__ = 'dashboards'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)

    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)

    columns = relationship(
        "ColumnModel",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )

    members = relationship(
        "UserModel",
        secondary="viewers",
        back_populates="dashboards",
    )

    author = relationship(
        "UserModel",
        foreign_keys=[author_id],
        back_populates="authored_dashboards",
    )