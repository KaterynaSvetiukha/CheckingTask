import { Button } from "@/components/ui/button"
import type { LoginDTO } from "@/entities/user/api/dto"
import { userApi } from "@/entities/user/api/requests"
import { useAuthStore } from "@/entities/user/model/useAuthStore"
import { useMutation } from "@tanstack/react-query"
import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"

export const LoginPage = () => {
  const navigate = useNavigate()
  const setUser = useAuthStore((state) => state.setUser)
  const [loginInput, setLoginInput] = useState<LoginDTO>({
    email: "",
    password: "",
  })

  const loginMutation = useMutation({
    mutationFn: userApi.login,
    onSuccess: (user) => {
      setUser(user)
      navigate("/dashboards")
    },
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setLoginInput((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    loginMutation.mutate(loginInput)
  }

  return (
    <div className="relative flex min-h-screen w-full items-center justify-center overflow-hidden bg-purple-950 p-4">
      <div className="pointer-events-none absolute -top-32 -left-32 h-96 w-96 rounded-full bg-purple-600/20 blur-3xl" />
      <div className="pointer-events-none absolute -right-32 -bottom-32 h-96 w-96 rounded-full bg-purple-600/20 blur-3xl" />
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-sm space-y-4 rounded-xl border bg-purple-900 p-6 shadow-2xl"
      >
        <div className="space-y-1 text-center">
          <h1 className="text-2xl font-bold tracking-tight text-shadow-md text-shadow-violet-300/30">
            Login
          </h1>
          <p className="text-sm text-muted-foreground">
            Sign in to account to lead the tasks
          </p>
        </div>

        {loginMutation.isError && (
          <div className="rounded-md bg-destructive/10 p-3 text-sm font-medium text-destructive">
            {loginMutation.error.message}
          </div>
        )}

        <div className="space-y-1.5">
          <label htmlFor="email" className="text-md font-medium">
            Enter your email
          </label>
          <input
            type="email"
            name="email"
            id="email"
            placeholder="example@gmail.com"
            value={loginInput.email}
            onChange={handleChange}
            required
            className="text-md w-full rounded-md border bg-purple-200 px-3 py-2 text-black shadow-md transition-colors focus:border-purple-600 focus:ring-1 focus:ring-purple-600 focus:outline-none"
          />
        </div>
        <div className="space-y-1.5">
          <label htmlFor="password" className="text-md font-medium">
            Enter your password
          </label>
          <input
            type="password"
            name="password"
            id="password"
            value={loginInput.password}
            onChange={handleChange}
            required
            className="text-md w-full rounded-md border bg-purple-200 px-3 py-2 text-black shadow-md transition-colors focus:border-purple-600 focus:ring-1 focus:ring-purple-600 focus:outline-none"
          />
        </div>

        <Button
          type="submit"
          className="bg- text-md mx-auto flex items-center justify-center bg-violet-300 px-10 py-5 text-purple-950 shadow-md shadow-violet-300/30 transition-colors hover:bg-violet-400"
          disabled={loginMutation.isPending}
        >
          {loginMutation.isPending ? "Login..." : "Login"}
        </Button>

        <p>
          Do you have not an account yet?{" "}
          <Link
            to="/register"
            className="text-purple-300 text-shadow-md text-shadow-purple-600/30"
          >
            Register
          </Link>
        </p>
      </form>
    </div>
  )
}
