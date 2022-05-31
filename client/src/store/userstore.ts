import { ref } from 'vue'
import { defineStore, StoreDefinition, } from 'pinia'

type User = {
    id: string
    username: string
    email: string
    picture: string
}


export const useAuthStore: StoreDefinition = defineStore("auth", {
    state: () => ({
        user : ref<User | null>(null),
        token: ref<string | null>(null)
    }),
    getters: {
        isLoggedIn: (state:any) => !!state.user.value,
        user: (state:any) => state.user.value,
    },
    actions: {
        login: (state:any, user:User) => {
            state.user.value = user
        },
        logout: (state:any) => {
            state.user.value = null
        }
    }
})

export default useAuthStore