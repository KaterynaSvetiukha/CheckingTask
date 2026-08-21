import type { Column } from "@/entities/column/model/types"
import type { User } from "@/entities/user/model/types"

export interface Dashboard {
  id: string
  name: string
  columns: Column[]
  author: User
  members?: User[]
  createdAt: string
  updatedAt?: string
}

export interface CreateDashboardInput {
  name: string
  membersIds?: string[]
}

export type UpdateDashboardInput = Partial<{
  name: string
  columns: Column[]
  membersIds: string[]
}>