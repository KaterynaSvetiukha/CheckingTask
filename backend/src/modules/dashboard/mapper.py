from .models import DashboardModel
from .schemas import DashboardResponse

def dashboard_to_response(dashboard: DashboardModel) -> DashboardResponse:
    return DashboardResponse(
        id=dashboard.id,
        name=dashboard.name,
        columns=[column.id for column in dashboard.columns],
        members=[member.id for member in dashboard.members],
        author_id=dashboard.author_id,
        created_at=dashboard.created_at,
        updated_at=dashboard.updated_at,
    )