export interface DashboardResponseDTO {
  id: string
  name: string
  columns: string[]
  author_id: string
  members: string[]
  created_at: string
  updated_at: string | null,
}

export interface CreateDashboardDTO {
  name: string
  members: string[]
}

export type UpdateDashboardDTO = Partial<{
  name: string
}>