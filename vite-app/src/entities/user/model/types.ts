import type { Dashboard } from "@/entities/dashboard/model/types"


export interface User {
  id: string
  username: string
  email: string
  dashboards: Dashboard['id'][]
}