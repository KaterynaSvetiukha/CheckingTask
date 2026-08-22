import type { TaskResponseDTO } from "@/entities/task/api/dto"

export type Status =
  "backlog" | "ready" | "in_progress" | "in_viewer" | "done" | "overdue"

export interface ColumnResponseDTO {
  id: string
  tasks?: TaskResponseDTO['id'][]
  status: Status
}

export interface CreateColumnDTO {
  status: Status
}

export interface UpdateColumnDTO {
  status: Status
  tasks?: TaskResponseDTO["id"][]
}