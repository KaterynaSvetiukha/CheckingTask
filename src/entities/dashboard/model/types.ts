import type { User } from "@/entities/user/model/types"

export interface Dashboard {
  id: string
  name: string
  columnIds?: string[]
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
  columnIds: string[]
  membersIds: string[]
}>