<template>
  <header>
    <nav>
      <div>
        <a href="/">FastAPI + Vue</a>
        <button type="button" >
          button
        </button>
        <div id="navbarCollapse">
          <ul v-if="isLoggedIn">
            <li>
              <router-link to="/">Home</router-link>
            </li>
            <li>
              <router-link to="/dashboard">Dashboard</router-link>
            </li>
            <li>
              <router-link to="/profile">My Profile</router-link>
            </li>
            <li>
              <a @click="logout">Log Out</a>
            </li>
          </ul>
          <ul v-else>
            <li>
              <router-link to="/">Home</router-link>
            </li>
            <li>
              <router-link to="/register">Register</router-link>
            </li>
            <li>
              <router-link to="/login">Log In</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavBar',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    },
  },
});
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
