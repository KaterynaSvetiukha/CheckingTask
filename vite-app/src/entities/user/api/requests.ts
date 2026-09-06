import { ClientApi } from "@/shared/api/apiClient"
import type { User} from "../model/types"
import type { LoginDTO, RegisterDTO, UserResponseDTO } from "./dto"
import { mapUserResponse } from "./mappers"
import type { DashboardShortResponseDTO } from "@/entities/dashboard/api/dto"
import type { TaskShortResponseDTO } from "@/entities/task/api/dto"

export const userApi = {
  getSearch: async (query: string): Promise<User[]> => {
    const dtos = await ClientApi.get<UserResponseDTO[]>(
      `/users/search?query=${encodeURIComponent(query)}`
    )
    return dtos.map(mapUserResponse)
  },
  register: async (input: RegisterDTO): Promise<User> => {
    const dto = await ClientApi.post<UserResponseDTO>("/users", input)
    return mapUserResponse(dto)
  },
  login: async (input: LoginDTO): Promise<User> => {
    const dto = await ClientApi.post<UserResponseDTO>("/users/login", input)
    return mapUserResponse(dto)
  },
  getUserById: async (id: string): Promise<User> => {
    const dto = await ClientApi.get<UserResponseDTO>(`/users/${id}`)
    return mapUserResponse(dto)
  },
  deleteUser: (id: string) =>
    ClientApi.delete<{ detail: string }>(`/users/${id}`),

  getDashboardsWhereUserIsOwn: (id: string) =>
    ClientApi.get<DashboardShortResponseDTO[]>(
      `/users/${id}/is-own-dashboards`
    ),
  getUserTasks: (id: string) =>
    ClientApi.get<TaskShortResponseDTO[]>(`/users/${id}/assigned-tasks`),
  getUserDashboards: (id: string) =>
    ClientApi.get<DashboardShortResponseDTO[]>(`/users/${id}/dashboards`),

  addUserToTask: (user_id: string, task_id: string) =>
    ClientApi.post<{ detail: string }>(
      `/users/${user_id}/tasks/${task_id}`,
      {}
    ),
  addUserToDashboard: (user_id: string, dashboard_id: string) =>
    ClientApi.post<{ detail: string }>(
      `/users/${user_id}/dashboards/${dashboard_id}`,
      {}
    ),
  
  deleteUserFromTask: (user_id: string, task_id: string) =>
    ClientApi.delete<{ detail: string }>(`/users/${user_id}/tasks/${task_id}`),
  deleteUserFromDashboard: (user_id: string, dashboard_id: string) =>
    ClientApi.delete<{ detail: string }>(
      `/users/${user_id}/dashboards/${dashboard_id}`
    ),
}
