import { ClientApi } from "@/shared/api/apiClient"
import type { DashboardResponseDTO } from "./dto"
import type {
  CreateDashboardInput,
  Dashboard,
  UpdateDashboardInput,
} from "../model/types"
import type { Column } from "@/entities/column/model/types"
import { mapCreateDashboardInput, mapDashboardResponse, mapUpdateDashboardInput } from "./mappers"
import type { ColumnResponseDTO } from "@/entities/column/api/dto"
import { mapColumnResponse } from "@/entities/column/api/mappers"

export const DashboardApi = {
  postDashboard: async (
    input: CreateDashboardInput,
    author_id: string
  ): Promise<Dashboard> => {
    const body = mapCreateDashboardInput(input)
    const dto = await ClientApi.post<DashboardResponseDTO>(
      `/dashboards?author_id=${author_id}`,
      body
    )
    return mapDashboardResponse(dto)
  },
  getDashboardById: async (id: string): Promise<Dashboard> => {
    const dto = await ClientApi.get<DashboardResponseDTO>(`/dashboards/${id}`)
    return mapDashboardResponse(dto)
  },
  getDashboardColumns: async (dashboard_id: string): Promise<Column[]> => {
    const dtos = await ClientApi.get<ColumnResponseDTO[]>(
      `/dashboards/${dashboard_id}/columns`
    )
    return dtos.map(mapColumnResponse)
  },
  putDashboard: async (
    id: string,
    input: UpdateDashboardInput
  ): Promise<Dashboard> => {
    const body = mapUpdateDashboardInput(input)
    const dto = await ClientApi.put<DashboardResponseDTO>(`/dashboards/${id}`, body)
    return mapDashboardResponse(dto)
  },
  deleteDashboard: (id: string) =>
    ClientApi.delete<{detail: string}>(`/dashboards/${id}`),
}
