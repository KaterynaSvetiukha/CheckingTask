export type Priority = "low" | "medium" | "high"

export interface TaskResponseDTO {
  id: string
  title: string
  description?: string
  tags?: string[]
  priority: Priority
  timeTo?: string
  createdAt: string
  updatedAt?: string
  assignees?: string[]
  author: string
  columnId: string
  position: string
}

export interface CreateTaskDTO {
  title: string
  description?: string
  tags?: string[]
  priority: Priority
  timeTo?: string
  assignees?: string[]
  columnId: string
}

export type UpdateTaskDTO = Partial<CreateTaskDTO>