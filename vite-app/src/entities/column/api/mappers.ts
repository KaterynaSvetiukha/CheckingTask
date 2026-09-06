import type { Column, CreateColumnInput, UpdateColumnInput } from "../model/types"
import type { ColumnResponseDTO, CreateColumnDTO, UpdateColumnDTO } from "./dto"

export function mapColumnResponse(dto: ColumnResponseDTO): Column {
  return {
    id: dto.id,
    status: dto.status,
    dashboardId: dto.dashboard_id,
    tasks: dto.tasks ?? [],
  }
}

export function mapCreateColumnInput(
  input: CreateColumnInput
): CreateColumnDTO {
  return {
    dashboard_id: input.dashboardId,
    status: input.status,
  }
}

export function mapUpdateColumnInput(
  input: UpdateColumnInput
): UpdateColumnDTO {
  return {
    status: input.status
  }
}
