import type { Column } from "../model/types"
import type { ColumnResponseDTO } from "./dto"

export function mapColumnResponse(dto: ColumnResponseDTO): Column {
  return {
    id: dto.id,
    status: dto.status,
    tasks: dto.tasks ?? [],
  }
}
