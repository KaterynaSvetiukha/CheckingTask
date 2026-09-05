export interface TagResponseDTO {
  id: string
  name: string
  color: string
  tasks: string[]
}

export interface TagShortResponseDTO {
  id: string
  name: string
  color: string
}

export interface CreateTagDTO {
  name: string
  color: string
}
