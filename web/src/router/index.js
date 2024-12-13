import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import About from "../views/About.vue";
import Lost from "../views/Lost.vue";
import Found from "../views/Found.vue";

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
  {
    path: "/lost",
    name: "Lost",
    component: Lost,
  },
  {
    path: "/found",
    name: "Found",
    component: Found,
  },
];

const router = createRouter({
  history: createWebHashHistory(), // Usar histórico do navegador
  routes,
});

export default router;
