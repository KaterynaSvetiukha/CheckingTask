import type { User } from "../model/types"
import type { UserResponseDTO } from "./dto"

export function mapUserResponse(dto: UserResponseDTO): User {
  return {
    id: dto.id,
    username: dto.username,
    email: dto.email,
    dashboards: dto.dashboards ?? [],
  }
}