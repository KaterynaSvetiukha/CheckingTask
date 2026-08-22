import type { ColumnResponseDTO } from "@/entities/column/api/dto"
import type { UserResponseDTO } from "@/entities/user/api/dto"

export type Priority = "low" | "medium" | "high"

export interface TaskResponseDTO {
  id: string
  title: string
  description?: string
  tag?: TagDTO["id"][]
  priority: Priority
  timeTo: string
  createdAt: string
  updatedAt?: string
  assignees?: UserResponseDTO["id"][]
  author: UserResponseDTO["id"]
  columnId: ColumnResponseDTO["id"]
  position: string
}

export interface CreateTaskDTO {
  title: string
  description?: string
  tag?: TagDTO["id"][]
  priority: Priority
  timeTo: string
  assignees?: UserResponseDTO["id"][]
  columnId: ColumnResponseDTO["id"]
}

export type UpdateTaskDTO = Partial<CreateTaskDTO>

export interface TagDTO {
  id: string
  name: string
  color: string
}

export interface TagCreateDTO {
  name: string
  color: string
}
