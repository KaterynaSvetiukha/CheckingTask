export type Status =
  "backlog" | "ready" | "in_progress" | "in_viewer" | "done" | "overdue"

export interface Column {
  id: string
  title: string
  taskIds?: string[]
  status: Status
}