import type { Dashboard } from "@/entities/dashboard/model/types"
import { DashboardCard } from "./DashboardCard"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { DashboardApi } from "@/entities/dashboard/api/requests"

interface DashboardListProps {
  dashboards: Dashboard[]
}

export const DashboardList = ({ dashboards }: DashboardListProps) => {
  const queryClient = useQueryClient();
  
  const deleteMutation = useMutation({
    mutationFn: DashboardApi.deleteDashboard,
    onSuccess: () => {
      // Оновлюємо кеш списку дощок
      queryClient.invalidateQueries({ queryKey: ["user-dashboards"] })
    },
  })

  const handleDelete = (id: string) => {
    deleteMutation.mutate(id)
  }

  return (
    <div className="grid grid-cols-1 gap-4 p-6 sm:grid-cols-2 lg:grid-cols-3">
      {dashboards?.map((dashboard) => (
        <DashboardCard
          key={dashboard.id}
          dashboard={dashboard}
          onDelete={handleDelete}
        />
      ))}
    </div>
  )
}
