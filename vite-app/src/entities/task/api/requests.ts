import { ClientApi } from "@/shared/api/apiClient"
import type { CreateTaskInput, MoveTaskInput, Task, UpdateTaskInput } from "@/entities/task/model/types"
import type { TaskResponseDTO } from "./dto"
import { mapCreateTaskInput, mapTaskResponse, mapUpdateTaskInput } from "./mappers"
import type { UserShortResponseDTO } from "@/entities/user/api/dto"
import type { TagShortResponseDTO } from "@/entities/tag/api/dto"

export const taskApi = {
  getTasks: async (): Promise<Task[]> => {
    const dtos = await ClientApi.get<TaskResponseDTO[]>("/tasks")
    return dtos.map(mapTaskResponse)
  },
  postTask: async (input: CreateTaskInput): Promise<Task> => {
    const body = mapCreateTaskInput(input)
    const dto = await ClientApi.post<TaskResponseDTO>("/tasks", body)
    return mapTaskResponse(dto)
  },
  getTaskById: async (id: string): Promise<Task> => {
    const dto = await ClientApi.get<TaskResponseDTO>(`/tasks/${id}`)
    return mapTaskResponse(dto)
  },
  putTask: async (id: string, input: UpdateTaskInput): Promise<Task> => {
    const body = mapUpdateTaskInput(input)
    const dto = await ClientApi.put<TaskResponseDTO>(`/tasks/${id}`, body)
    return mapTaskResponse(dto)
  },
  patchTask: async (id: string, input: MoveTaskInput): Promise<Task> => {
    const body = { column_id: input.columnId, position: input.position }
    const dto = await ClientApi.patch<TaskResponseDTO>(
      `/tasks/${id}/move`,
      body
    )
    return mapTaskResponse(dto)
  },
  getAssigneesById: (task_id: string) =>
    ClientApi.get<UserShortResponseDTO[]>(`/tasks/${task_id}/assignees`),
  getTagsById: (task_id: string) =>
    ClientApi.get<TagShortResponseDTO[]>(`/tasks/${task_id}/tags`),
  deleteTask: (id: string) =>
    ClientApi.delete<{ detail: string }>(`/tasks/${id}`),
}
