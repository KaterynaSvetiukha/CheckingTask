from sqlalchemy import Column, String, Enum, ForeignKey
from src.core.database import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid, enum

class StatusEnum(str, enum.Enum):
    backlog = "backlog"
    ready = "ready"
    in_process = "in_process"
    in_viewer = "in_viewer"
    done = "done"
    overdue = "overdue"


class ColumnModel(Base):
    __tablename__ = 'column'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    status = Column(Enum(StatusEnum, name="status_enum"), nullable=False, default=StatusEnum.backlog)

    dashboard_id = Column(UUID(as_uuid=True), ForeignKey("dashboard.id", ondelete="CASCADE"))