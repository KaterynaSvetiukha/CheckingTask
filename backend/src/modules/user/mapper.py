from .models import UserModel
from .schemas import UserResponse

def user_to_response(user: UserModel) -> UserResponse:
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        dashboards=[dashboard.id for dashboard in user.dashboards]
    )