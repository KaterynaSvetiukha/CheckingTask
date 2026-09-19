import { ClientApi } from "@/shared/api/apiClient"
import type { User} from "../model/types"
import type { LoginDTO, RegisterDTO, UserResponseDTO } from "./dto"
import { mapUserResponse } from "./mappers"
import type { DashboardShortResponseDTO } from "@/entities/dashboard/api/dto"
import type { Dashboard } from "@/entities/dashboard/model/types"
import type { Task } from "@/entities/task/model/types"
import { mapDashboarShortResponse } from "@/entities/dashboard/api/mappers"

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

  getDashboardsWhereUserIsOwn: async (id: string) => {
    const dtos = await ClientApi.get<DashboardShortResponseDTO[]>(
      `/users/${id}/is-own-dashboards`)
    return dtos.map(mapDashboarShortResponse)
  },
  getUserTasks: (id: string) =>
    ClientApi.get<Task[]>(`/users/${id}/assigned-tasks`),

  getUserDashboards: async (id: string): Promise<Dashboard[]> => {
    const dtos = await ClientApi.get<DashboardShortResponseDTO[]>(
      `/users/${id}/dashboards`
    )
    return dtos.map(mapDashboarShortResponse)
  },

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
