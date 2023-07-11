import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import Create from './components/Create.vue'
import Get from './components/Get.vue'

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
            props: true
        },
        {
            path: '/create',
            name: 'create',
            component: Create,
        },
        {
            path: '/get',
            name: 'get',
            component: Get,
        },
    ]
})