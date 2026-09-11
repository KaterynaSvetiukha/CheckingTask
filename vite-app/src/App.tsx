import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import { useAuthStore } from "./entities/user/model/useAuthStore"
import { LoginPage } from "./pages/login/LoginPage"
import { RegisterPage } from "./pages/register/RegisterPage"
import { DashboardsPage } from "./pages/dashboard/DashboardsPage"
import { BoardPage } from "./pages/dashboard/BoardPage"
import { NotFoundPage } from "./pages/error/NotFoundPage"

export function App() {
  const user = useAuthStore((state) => state.user)
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/login"
          element={user ? <Navigate to="/dashboards" replace /> : <LoginPage />}
        />

        <Route
          path="/register"
          element={
            user ? <Navigate to="/dashboards" replace /> : <RegisterPage />
          }
        />

        <Route
          path="/dashboards"
          element={user ? <DashboardsPage /> : <Navigate to="/login" replace />}
        />

        <Route
          path="/dashboards/:dashboardId"
          element={user ? <BoardPage /> : <Navigate to="/login" replace />}
        />

        <Route
          path="*"
          element={<NotFoundPage />}
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App
