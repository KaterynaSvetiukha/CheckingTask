import { Button } from "@/components/ui/button"
import { ArrowLeft, Home } from "lucide-react"
import { useNavigate } from "react-router-dom"

export const NotFoundPage = () => {
  const navigate = useNavigate()

  return (
    <div className="relative flex min-h-screen flex-col items-center justify-center overflow-hidden bg-purple-950 px-4 text-white">
      <div className="pointer-events-none absolute -top-32 -left-32 h-96 w-96 rounded-full bg-purple-600/20 blur-3xl" />
      <div className="pointer-events-none absolute -right-32 -bottom-32 h-96 w-96 rounded-full bg-purple-600/20 blur-3xl" />

      <div className="relative z-10 flex max-w-lg flex-col items-center text-center">
        <div className="relative mb-2">
          <span className="bg-gradient-to-b from-purple-600 via-purple-500 to-purple-900 bg-clip-text text-8xl font-black tracking-tighter text-transparent select-none sm:text-9xl">
            404
          </span>
          <div className="absolute inset-0 -z-10 text-8xl font-black tracking-tighter text-purple-900/10 blur-xl select-none sm:text-9xl">
            404
          </div>
        </div>

        <h1 className="text-2xl font-bold tracking-tight text-white sm:text-3xl">
          Page Not Found
        </h1>
        <p className="mt-3 text-sm text-purple-200/70 sm:text-base">
          Maybe this page is not exist, was reset or deleted.
        </p>

        <div className="mt-8 flex flex-col gap-6 sm:flex-row">
          <Button
            variant="outline"
            onClick={() => navigate(-1)}
            className="flex items-center gap-2 border-violet-800/50 bg-purple-950/40 text-purple-200 hover:bg-purple-900/60 hover:text-white"
          >
            <ArrowLeft className="h-4 w-4" />
            Back
          </Button>

          <Button
            onClick={() => navigate("/dashboards")}
            className="flex items-center gap-2 bg-purple-600 text-white shadow-lg shadow-purple-600/30 hover:bg-purple-500"
          >
            <Home className="h-4 w-4" />
            To my dashboards
          </Button>
        </div>

        <div className="mt-12 text-purple-300/40">Check url above</div>
      </div>
    </div>
  )
}
