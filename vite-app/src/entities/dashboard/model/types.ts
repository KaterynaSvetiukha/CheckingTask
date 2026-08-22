import type { Column } from "@/entities/column/model/types"
import type { User } from "@/entities/user/model/types"

export interface Dashboard {
  id: string
  name: string
  columns?: Column["id"][]
  author: User
  members?: User["id"][]
  createdAt: Date
  updatedAt?: Date
}

export interface CreateDashboardInput {
  name: string
  members?: User["id"][]
}

export type UpdateDashboardInput = Partial<{
  name: string
  columns: Column["id"][]
  members: User['id'][]
}>