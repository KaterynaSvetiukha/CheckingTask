export type Status =
  "backlog" | "ready" | "in_progress" | "in_viewer" | "done" | "overdue"

export interface ColumnResponseDTO {
  id: string
  tasks?: string[]
  status: Status
}

export interface CreateColumnDTO {
  status: Status
}

export interface UpdateColumnDTO {
  status: Status
  tasks?: string[]
}