import type { Task } from "@/entities/task/model/types"

export type Status =
  "backlog" | "ready" | "in_progress" | "in_viewer" | "done" | "overdue"

export interface Column {
  id: string
  tasks: Task["id"][]
  dashboardId: string
  status: Status
}

export interface CreateColumnInput {
  dashboardId: string
  status: Status
}

export interface UpdateColumnInput {
  status?: Status
}