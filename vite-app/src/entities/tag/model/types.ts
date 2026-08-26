import type { Task } from "@/entities/task/model/types"

export interface Tag {
  id: string
  name: string
  color: string
  tasks: Task["id"][]
}