import { ClientApi } from "@/shared/api/apiClient"
import type { ColumnResponseDTO } from "./dto"
import type { Column, CreateColumnInput, UpdateColumnInput } from "../model/types"
import type { Task } from "@/entities/task/model/types"
import { mapColumnResponse, mapCreateColumnInput, mapUpdateColumnInput } from "./mappers"
import type { TaskResponseDTO } from "@/entities/task/api/dto"
import { mapTaskResponse } from "@/entities/task/api/mappers"

export const ColumnApi = {
  getColumns: async (): Promise<Column[]> => {
    const dtos = await ClientApi.get<ColumnResponseDTO[]>("/columns")
    return dtos.map(mapColumnResponse)
  },
  postColumn: async (input: CreateColumnInput): Promise<Column> => {
    const body = mapCreateColumnInput(input)
    const dto = await ClientApi.post<ColumnResponseDTO>("/columns", body)
    return mapColumnResponse(dto)
  },
  getColumnById: async (column_id: string): Promise<Column> => {
    const dto = await ClientApi.get<ColumnResponseDTO>(`/columns/${column_id}`)
    return mapColumnResponse(dto)
  },
  getColumnTasks: async (column_id: string): Promise<Task[]> => {
    const dtos = await ClientApi.get<TaskResponseDTO[]>(
      `/columns/${column_id}/tasks`
    )
    return dtos.map(mapTaskResponse)
  },
  putColumn: async (
    column_id: string,
    input: UpdateColumnInput
  ): Promise<Column> => {
    const body = mapUpdateColumnInput(input)
    const dto = await ClientApi.put<ColumnResponseDTO>(`/columns/${column_id}`, body)
    return mapColumnResponse(dto)
  },
  deleteColumn: (column_id: string) =>
    ClientApi.delete<{detail: string}>(`/columns/${column_id}`),
}
