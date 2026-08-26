from .models import TaskModel
from .schemas import TaskResponse

def task_to_response(task: TaskModel) -> TaskResponse:
    return TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        tags=[tag.id for tag in task.tags],
        priority=task.priority,
        time_to=task.time_to,
        created_at=task.created_at,
        updated_at=task.updated_at,
        assignees=[user.id for user in task.assignees],
        author_id=task.author_id,
        column_id=task.column_id,
        position=task.position,
    )