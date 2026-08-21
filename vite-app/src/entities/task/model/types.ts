import type { User } from "@/entities/user/model/types"

export type Priority = "low" | "medium" | "high"

export interface Task {
  id: string
  title: string
  description?: string
  tag?: Tag['id'][]
  priority: Priority
  timeTo: string
  createdAt: string
  updatedAt?: string
  assignees?: User['id'][]
  author: User["id"]
  columnId: string
  position: string
}

export interface CreateTaskInput {
  title: string
  description?: string
  tag?: Tag["id"][]
  priority: Priority
  timeTo: string
  assignees?: User["id"][]
  columnId: string
}

export type UpdateTaskInput = Partial<CreateTaskInput>

export interface Tag {
  id: string
  name: string
  color: string
}
