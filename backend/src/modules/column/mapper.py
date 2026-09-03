from .models import ColumnModel
from .schemas import ColumnResponse

def column_to_response(column: ColumnModel) -> ColumnResponse:
    return ColumnResponse(
        id=column.id,
        dashboard_id=column.dashboard_id,
        tasks=[task.id for task in column.tasks],
        status=column.status,
    )