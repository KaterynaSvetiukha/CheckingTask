from sqlalchemy import Column, Enum, ForeignKey
from src.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import enum
import uuid_utils as uuid

class StatusEnum(str, enum.Enum):
    backlog = "backlog"
    ready = "ready"
    in_process = "in_process"
    in_viewer = "in_viewer"
    done = "done"
    overdue = "overdue"


class ColumnModel(Base):
    __tablename__ = 'columns'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid7)
    status = Column(Enum(StatusEnum, name="status_enum"), nullable=False, default=StatusEnum.backlog)

    dashboard_id = Column(UUID(as_uuid=True), ForeignKey("dashboards.id", ondelete="CASCADE"), index=True)