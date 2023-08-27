<template>
  <section>
    <form @submit.prevent="submit">
      <div>
        <label for="username">Username:</label>
        <input type="text" name="username" v-model="user.username" />
      </div>
      <div>
        <label for="full_name">Full Name:</label>
        <input type="text" name="full_name" v-model="user.full_name" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" name="password" v-model="user.password" />
      </div>
      <button type="submit">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'RegisterView',
  data() {
    return {
      user: {
        username: '',
        full_name: '',
        password: '',
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        await this.register(this.user);
      } catch (error) {
        throw 'Username already exists. Please, try again.';
      }
    },
  },
});
</script>
