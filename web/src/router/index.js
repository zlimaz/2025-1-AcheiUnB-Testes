import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import About from "../views/About.vue";
import Lost from "../views/Lost.vue";
import Found from "../views/Found.vue";
import Register from "../views/Register.vue";
import User from "../views/User.vue";
import Chats from "../views/Chats.vue";
import ItemFound from "../views/ItemFound.vue"
import ItemLost from "../views/ItemLost.vue"

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
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/user",
    name: "User",
    component: User,
  },
  {
    path: "/chats",
    name: "Chats",
    component: Chats,
  },
  {
    path: "/item-found",
    name: "ItemFound",
    component: ItemFound,
  },
  {
    path: "/item-lost",
    name: "ItemLost",
    component: ItemLost,
  },
];

const router = createRouter({
  history: createWebHashHistory(), // Usar histórico do navegador
  routes,
});

export default router;
