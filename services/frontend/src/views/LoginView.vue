<template>
  <section>
    <form @submit.prevent="submit">
      <div>
        <label for="username">Username:</label>
        <input type="text" name="username" v-model="form.username" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" name="password" v-model="form.password" />
      </div>
      <button type="submit">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'LoginView',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      await this.logIn(User);
      this.$router.push('/users');
    },
  },
});
</script>
