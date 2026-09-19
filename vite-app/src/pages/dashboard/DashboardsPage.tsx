import { Button } from "@/components/ui/button"
import { DashboardApi } from "@/entities/dashboard/api/requests"
import { userApi } from "@/entities/user/api/requests"
import { useAuthStore } from "@/entities/user/model/useAuthStore"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { LayoutDashboard, UserIcon } from "lucide-react"
import { useState } from "react"
import { DashboardList } from "./DashboardList"

export const DashboardsPage = () => {
  const user = useAuthStore((state) => state.user)
  const logout = useAuthStore((state) => state.logout)
  const queryClient = useQueryClient()
  const [isCreating, setIsCreating] = useState(false)
  const [newDashboardName, setNewDashboardName] = useState("")

  const { data: dashboards = [], isLoading } = useQuery({
    queryKey: ["user-dashboards", user?.id],
    queryFn: () => userApi.getUserDashboards(user!.id),
    enabled: !!user?.id,
  })

  const createMunation = useMutation({
    mutationFn: (name: string) =>
      DashboardApi.postDashboard({ name, members: [] }, user!.id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["user-dashboards", user?.id] })
      setNewDashboardName("")
      setIsCreating(false)
    },
  })

  const handleCreateDashboard = (e: React.FormEvent) => {
    e.preventDefault()
    if (!newDashboardName.trim()) return
    createMunation.mutate(newDashboardName)
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <header className="sticky top-0 z-50 border-b border-purple-900/30 bg-purple-950/20 backdrop-blur-md">
        <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
          <div className="flex items-center gap-3">
            <div className="flex h-9 w-9 items-center justify-center bg-purple-600 text-white shadow-lg shadow-purple-600/30">
              <LayoutDashboard className="h-5 w-5" />
            </div>
            <span className="text-lg font-bold tracking-wider text-purple-200">
              CheckingTask
            </span>
          </div>

          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 text-sm text-purple-200/80">
              <div className="rounded-3xl border bg-purple-950 px-4 py-2.5">
                {user?.username.charAt(0).toUpperCase() || (
                  <UserIcon className="h-4 w-4" />
                )}
              </div>
              <span>{user?.username}</span>
            </div>

            <Button
              size="sm"
              variant="outline"
              onClick={logout}
              className="border-purple-800/40 bg-purple-950/40 text-purple-300 hover:border-blue-500/40 hover:bg-blue-500/20 hover:text-blue-300"
            >
              Log Out
            </Button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl space-y-6 p-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-bold text-2xl text-white">My dashboards</h1>
            <span className="text-md text-bold text-purple-300/60">
              Lead your projects and tasks
            </span>
          </div>
          <div>
            <Button
              className="flex bg-purple-600 text-white shadow-lg shadow-purple-600/30 hover:bg-purple-500"
              onClick={() => setIsCreating(true)}
            >
              New Dashboard
            </Button>
          </div>
        </div>
        {isCreating && (
          <div className="flex w-full items-center justify-center">
            <form
              onSubmit={handleCreateDashboard}
              className="max-w-2xl flex-col flex w-full gap-5 rounded-xl border border-purple-500/40 bg-purple-950/40 p-4"
            >
              <div className="flex flex-col gap-1">
                <label htmlFor="name">Enter dashboard name</label>
                <input
                  type="text"
                  name="name"
                  id="name"
                  onChange={(e) => setNewDashboardName(e.target.value)}
                  autoFocus
                  required
                  value={newDashboardName}
                  className="sm:flex-1text-sm w-full rounded-lg border border-purple-800/50 bg-purple-900/30 px-3.5 py-2 text-white focus:ring-2 focus:ring-purple-400 focus:outline-none"
                />
              </div>
              <div className="flex w-full items-center justify-between">
                <Button
                  type="submit"
                  disabled={createMunation.isPending}
                  className="flex-1 bg-purple-600 p-4 text-white hover:bg-purple-500 sm:flex-initial"
                >
                  {createMunation.isPending ? "Creating..." : "Create"}
                </Button>
                <Button
                  type="button"
                  onClick={() => setIsCreating(false)}
                  className="border-slate-950 bg-slate-950 p-4 text-purple-300 hover:bg-slate-800"
                >
                  Cancel
                </Button>
              </div>
            </form>
          </div>
        )}

        {isLoading ? (
          <div className="py-12 text-center text-purple-300/60">Loading...</div>
        ) : dashboards.length === 0 ? (
          <div className="rounded-xl border border-dashed border-purple-900/40 p-8 py-16 text-center">
            There is no any dashboard
          </div>
        ) : (
          <DashboardList dashboards={dashboards} />
        )}
      </main>
    </div>
  )
}
