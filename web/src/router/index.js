import { createRouter, createWebHashHistory } from 'vue-router'
import Login from "../views/Login.vue"

const routes = [
    {
      path: "/",
      name: "Login",
      component: Login,
    },
  ];
  
  const router = createRouter({
    history: createWebHashHistory(), // Usar histórico do navegador
    routes,
  });

export default router
