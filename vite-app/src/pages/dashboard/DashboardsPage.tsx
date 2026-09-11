import { Button } from "@/components/ui/button";
import { useAuthStore } from "@/entities/user/model/useAuthStore";

export const DashboardsPage = () => {
  const logout = useAuthStore((state) => state.logout);
  return <Button onClick={logout}>Log Out</Button>
}
