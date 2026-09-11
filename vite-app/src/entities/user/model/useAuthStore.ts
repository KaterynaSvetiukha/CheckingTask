import { create } from "zustand"
import { persist } from "zustand/middleware"
import type { User } from "./types"

interface AuthState {
    user: User | null
    setUser: (user: User | null) => void
    logout: () => void
}

export const useAuthStore = create<AuthState>()(
    persist(
        (set) => ({ // update value in storage
            user: null, // when we just have entered without register/login
            setUser: (user) => set({ user }),
            logout: () => set({user: null}),
        }),
        {
            name: "auth-storage", // data will be save with this key in localStorage
        }
    )
)