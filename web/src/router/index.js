import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import About from "../views/About.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
];

const router = createRouter({
  history: createWebHashHistory(), // Usar histórico do navegador
  routes,
});

export default router;
