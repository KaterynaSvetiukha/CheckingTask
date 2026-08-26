export interface RegisterDTO {
  username: string
  email: string
  password: string
}

export interface LoginDTO {
  email: string
  password: string
}

export interface UserResponseDTO {
  id: string
  username: string
  email: string
  dashboards: string[]
}
