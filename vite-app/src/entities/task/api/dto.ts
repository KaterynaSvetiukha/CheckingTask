export type Priority = "low" | "medium" | "high"

export interface TaskResponseDTO {
  id: string
  title: string
  description: string | null
  tags: string[]
  priority: Priority
  time_to: string | null
  created_at: string
  updated_at: string | null
  assignees: string[]
  author_id: string
  column_id: string
  position: string
}

export interface CreateTaskDTO {
  title: string
  description: string | null
  tags: string[] | null
  priority: Priority
  time_to: string | null
  assignees: string[]
  column_id: string
}

export type UpdateTaskDTO = Partial<CreateTaskDTO>