import { ClientApi } from "@/shared/api/apiClient"
import type { Tag } from "../model/types"
import type { CreateTagDTO, TagResponseDTO } from "./dto"
import { mapTagResponse } from "./mappers"
import type { Task } from "@/entities/task/model/types"
import type { TaskResponseDTO } from "@/entities/task/api/dto"
import { mapTaskResponse } from "@/entities/task/api/mappers"

export const tagApi = {
  getTags: async (): Promise<Tag[]> => {
    const dtos = await ClientApi.get<TagResponseDTO[]>("/tags")
    return dtos.map(mapTagResponse)
  },
  postTag: async (input: CreateTagDTO): Promise<Tag> => {
    const dto = await ClientApi.post<TagResponseDTO>("/tags", input)
    return mapTagResponse(dto)
  },
  getTagTasks: async (id: string): Promise<Task[]> => {
    const dtos = await ClientApi.get<TaskResponseDTO[]>(`/tags/${id}/tasks`)
    return dtos.map(mapTaskResponse)
  },
  addTagToTask: (tag_id: string, task_id: string) =>
    ClientApi.post<{ detail: string }>(`/tags/${tag_id}/tasks/${task_id}`, {}),
  deleteTagFromTask: (tag_id: string, task_id: string) =>
    ClientApi.delete<{ detail: string }>(`/tags/${tag_id}/tasks/${task_id}`),
  deleteTag: (tag_id: string) =>
    ClientApi.delete<{ detail: string }>(`/tags/${tag_id}`),
}
