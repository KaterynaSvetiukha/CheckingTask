import type { Dashboard, CreateDashboardInput, UpdateDashboardInput } from "../model/types"
import type { DashboardResponseDTO, CreateDashboardDTO, UpdateDashboardDTO } from "./dto"

export function mapDashboardResponse(dto: DashboardResponseDTO): Dashboard {
  return {
    id: dto.id,
    name: dto.name,
    author: dto.author_id,
    columns: dto.columns ?? [],
    members: dto.members ?? [],
    createdAt: new Date(dto.created_at),
    updatedAt: dto.updated_at ? new Date(dto.updated_at) : null,
  }
}

export function mapCreateDashboardInput(
  input: CreateDashboardInput
): CreateDashboardDTO {
  return {
    name: input.name,
    members: input.members ?? [],
  }
}

export function mapUpdateDashboardInput(
  input: UpdateDashboardInput
): UpdateDashboardDTO {
  return {
    ...(input.name !== undefined && { name: input.name }),
    ...(input.columns !== undefined && {
      columns: input.columns,
    }),
    ...(input.members !== undefined && { members: input.members }),
  }
}