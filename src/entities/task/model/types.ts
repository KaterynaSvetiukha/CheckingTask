import type { User } from "@/entities/user/model/types"

export type Priority = "low" | "medium" | "high"

export interface Task {
  id: string
  title: string
  description?: string
  tag?: Tag[]
  priority: Priority
  timeTo: string
  createdAt: string
  updatedAt?: string
  assignees?: User[]
  author: User["id"]
  columnId: string
  position: number
}

export interface CreateTaskInput {
  title: string
  description?: string
  tag?: Tag[]
  priority: Priority
  timeTo: string
  assigneesIds?: string[]
  columnId: string
}

export type UpdateTaskInput = Partial<{
  title: string
  description?: string
  tag?: Tag[]
  priority: Priority
  timeTo: string
  assigneesIds?: string[]
  columnId: string
  position: number
}>

export interface Tag {
  id: string
  name: string
  color: string
}
