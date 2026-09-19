import type { Dashboard } from "@/entities/dashboard/model/types"
import { Link } from "react-router-dom"
import { Calendar, LayoutDashboard, ArrowRight, Trash2 } from "lucide-react"

interface DashboardCardProps {
  dashboard: Dashboard
  onDelete: (id: string) => void
}

export const DashboardCard = ({ dashboard, onDelete }: DashboardCardProps) => {
  const handleDeleteClick = (e: React.MouseEvent) => {
    e.preventDefault() // не переходимо по посиланню Link
    e.stopPropagation();
    onDelete(dashboard.id)
  }
  return (
    <Link
      to={`/dashboards/${dashboard.id}`}
      className="group border-rounded-xl relative flex justify-between border border-purple-900/40
       bg-purple-950/20 p-5 shadow-lg backdrop-blur-sm transition-all duration-200 
       hover:-translate-y-1 hover:border-purple-500/50 hover:bg-purple-900/30 
       hover:shadow-purple-900/20"
    >
      <div className="space-y-3 w-full">
        <div className="flex items-center justify-between">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-purple-600/20 text-purple-400 group-hover:bg-purple-600/30 group-hover:text-purple-300">
            <LayoutDashboard className="h-5 w-5" />
          </div>
          <span className="flex items-center gap-1 text-xs text-purple-300/60">
            <Calendar className="h-3.5 w-3.5" />
            {new Date(dashboard.createdAt).toLocaleDateString()}
          </span>
          <button
            className="rounded-md p-1.5 text-purple-300/40 transition-colors hover:bg-blue-500/20 hover:text-bue-400"
            onClick={handleDeleteClick} title="Delete board"
          >
            <Trash2 className="h-5 w-5" />
          </button>
        </div>

        <h3 className="text-lg font-semibold tracking-tight text-white group-hover:text-purple-200">
          {dashboard.name}
        </h3>
        <div className="mt-6 flex items-center justify-between border-t border-purple-900/30 pt-3 text-xs text-purple-300/60">
          <span>Open board</span>
          <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1 group-hover:text-purple-300" />
        </div>
      </div>
    </Link>
  )
}
