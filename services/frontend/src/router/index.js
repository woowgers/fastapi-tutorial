import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import RegisterView from "@/views/RegisterView.vue";
import LoginView from "@/views/LoginView.vue";
import UsersView from "@/views/UsersView.vue";
import ProfileView from "@/views/ProfileView.vue";
import UserView from "@/views/UserView.vue";
import FriendsView from "@/views/FriendsView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterView,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/users",
    name: "Users",
    component: UsersView,
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
  },
  {
    path: "/users/:id",
    name: "User",
    component: UserView,
    props: true,
  },
  {
    path: "/users/:id/friends",
    name: "Friends",
    component: FriendsView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
