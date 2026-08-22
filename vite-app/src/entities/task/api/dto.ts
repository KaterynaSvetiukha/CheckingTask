import type { User } from "@/entities/user/model/types"

export type Priority = "low" | "medium" | "high"

export interface TaskResponseDTO {
  id: string
  title: string
  description?: string
  tag?: string[]
  priority: Priority
  timeTo: string
  createdAt: string
  updatedAt?: string
  assignees?: string[]
  author: User
  columnId: string
  position: string
}

export interface CreateTaskDTO {
  title: string
  description?: string
  tag?: string[]
  priority: Priority
  timeTo: string
  assignees?: string[]
  columnId: string
}

export type UpdateTaskDTO = Partial<CreateTaskDTO>

export interface TagCreateDTO {
  name: string
  color: string
}
