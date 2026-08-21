import type { Dashboard } from "@/entities/dashboard/model/types"


export interface User {
  id: string
  username: string
  email: string
  password: string
  dashboards?: Dashboard[]
}

export interface RegisterInput {
  username: string
  email: string
  password: string
}

export interface LoginInput {
  email: string
  password: string
}
