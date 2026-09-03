import type { Tag } from "@/entities/tag/model/types"
import type { User } from "@/entities/user/model/types"

export type Priority = "low" | "medium" | "high"

export interface Task {
  id: string
  title: string
  description: string | null
  tags: Tag["id"][]
  priority: Priority
  timeTo: string | null
  createdAt: Date
  updatedAt: Date | null
  assignees: User["id"][]
  author: User["id"]
  columnId: string
  position: string
}

export interface CreateTaskInput {
  title: string
  description: string | null
  tags: Tag["id"][]
  priority: Priority
  timeTo: string | null
  assignees: User["id"][]
  columnId: string
  authorId: string
  position: string
}

export interface UpdateTaskInput {
  title?: string
  description?: string | null
  priority?: Priority
  timeTo?: string | null
  position?: string
}

export interface MoveTaskInput {
  columnId: string
  position: string
}