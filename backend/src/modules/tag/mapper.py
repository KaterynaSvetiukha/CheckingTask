from .models import TagModel
from .schemas import TagResponse

def tag_to_response(tag: TagModel) -> TagResponse:
    return TagResponse(
        id=tag.id,
        name=tag.name,
        color=tag.color,
        tasks=[task.id for task in tag.tasks],
    )