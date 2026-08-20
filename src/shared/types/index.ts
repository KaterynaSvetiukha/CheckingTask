export type Status = "created" | "in_process" | "done" | "overdue"
export type Priority = "low" | "medium" | "high"

export interface Task {
  id: string
  title: string
  description?: string
  tag?: Tag[]
  priority: Priority
  status: Status
  timeTo: string
  timeSpend: string
  createdAt: string
  updatedAt?: string
  coAuthors?: User[]
  author: User
  columnId: string
}

export type CreateTaskInput = Omit<
  Task,
  "id" | "createdAt" | "updatedAt" | "author" | "timeSpend"
>

export type UpdateTaskInput = Partial<CreateTaskInput>

export interface Tag {
  name: string
  color: string
}

export interface Column {
  id: string
  title: string
  taskIds: string[]
  status: Status
}

export interface Dashboard {
  columnIds: string[]
}

export interface User {
  id: string
  username: string
  email: string
  password: string
}

export type RegisterInput = Omit<User, "id">

export type LoginInput = Pick<User, "email" | "password">

export interface FilterTasks {
  priority: Priority | "all"
  status: Status | "all"
  searchQuery: string
  timeTo: string
  tags: Tag[]
}
