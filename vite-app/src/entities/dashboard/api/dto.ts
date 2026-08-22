import type { ColumnDTO } from "@/entities/column/api/dto"
import type { UserResponseDTO } from "@/entities/user/api/dto"

export interface DashboardResponseDTO {
  id: string
  name: string
  columns?: ColumnDTO['id'][]
  author: UserResponseDTO['id']
  members?: UserResponseDTO['id'][]
  createdAt: string
  updatedAt?: string
}

export interface CreateDashboardDTO {
  name: string
  members?: UserResponseDTO["id"][]
}

export type UpdateDashboardDTO = Partial<{
  name: string
  columns: ColumnDTO["id"][]
  members: UserResponseDTO["id"][]
}>