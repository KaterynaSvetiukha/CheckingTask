import type { Task } from "@/entities/task/model/types"

export type Status =
  "backlog" | "ready" | "in_progress" | "in_viewer" | "done" | "overdue"

export interface Column {
  id: string
  title: string
  tasks?: Task[]
  status: Status
  position: number
}