import { createApp } from "vue";
import axios from "axios";

import App from "./App.vue";
import router from "./router";
import store from "./store";

const app = createApp(App);

app.use(router);
app.use(store);
app.mount("#app");

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:5000/";
