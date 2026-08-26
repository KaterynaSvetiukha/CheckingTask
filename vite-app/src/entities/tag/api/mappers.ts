import type { Tag } from "../model/types"
import type { TagResponseDTO } from "./dto"

export function mapTagResponse(dto: TagResponseDTO): Tag {
  return {
    id: dto.id,
    name: dto.name,
    color: dto.color,
    tasks: dto.tasks ?? [],
  }
}
