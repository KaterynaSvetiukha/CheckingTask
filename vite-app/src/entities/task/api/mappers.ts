import type { Task, CreateTaskInput, UpdateTaskInput } from "../model/types"
import type { TaskResponseDTO, CreateTaskDTO, UpdateTaskDTO } from "./dto"

export function mapTaskResponse(dto: TaskResponseDTO): Task {
  return {
    id: dto.id,
    title: dto.title,
    description: dto.description ?? null,
    tags: dto.tags ?? [],
    priority: dto.priority,
    timeTo: dto.time_to ?? null,
    createdAt: new Date(dto.created_at),
    updatedAt: dto.updated_at ? new Date(dto.updated_at) : null,
    assignees: dto.assignees ?? [],
    author: dto.author_id,
    columnId: dto.column_id,
    position: dto.position,
  }
}

export function mapCreateTaskInput(input: CreateTaskInput): CreateTaskDTO {
  return {
    title: input.title,
    description: input.description ?? null,
    tags: input.tags ?? [],
    priority: input.priority,
    time_to: input.timeTo ?? null,
    assignees: input.assignees ?? [],
    column_id: input.columnId,
    author_id: input.authorId,
    position: input.position,
  }
}

export function mapUpdateTaskInput(input: UpdateTaskInput): UpdateTaskDTO {
  return {
    ...(input.title !== undefined && { title: input.title }),
    ...(input.description !== undefined && {
      description: input.description,
    }),
    ...(input.priority !== undefined && {
      priority: input.priority,
    }),
    ...(input.timeTo !== undefined && {
      time_to: input.timeTo,
    }),
    ...(input.position !== undefined && {
      position: input.position,
    }),
  }
}