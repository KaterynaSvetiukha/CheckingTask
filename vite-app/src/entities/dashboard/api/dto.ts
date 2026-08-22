import type { User } from "@/entities/user/model/types"

export interface DashboardResponseDTO {
  id: string
  name: string
  columns?: string[]
  author: User
  members?: string[]
  createdAt: string
  updatedAt?: string
}

export interface CreateDashboardDTO {
  name: string
  members?: string[]
}

export type UpdateDashboardDTO = Partial<{
  name: string
  columns: string[]
  members: string[]
}>