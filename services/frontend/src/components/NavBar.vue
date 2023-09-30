<template>
  <header>
    <nav>
      <ul v-if="isLoggedIn">
        <li>
          <router-link to="/">Home</router-link>
        </li>
        <li>
          <router-link to="/users">Users</router-link>
        </li>
        <li>
          <router-link to="/profile">My Profile</router-link>
        </li>
        <li>
          <router-link :to="{name: 'Friends', params:{id: me.id}}">Friends</router-link>
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
    </nav>
  </header>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters } from 'vuex';

export default defineComponent({
  name: 'NavBar',
  computed: {
    ...mapGetters({ me: 'stateMe' }),
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

nav ul {
  display: flex;
  flex-direction: row;
}

nav ul li {
  margin: 0 1em;
}
</style>
