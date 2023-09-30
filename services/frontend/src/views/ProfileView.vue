<template>
  <section>
    <h1>Your Profile</h1>
    <hr/><br/>
    <div>
      <p><strong>ID:</strong> {{ me.id }}</p>
      <p><strong>Full Name:</strong> {{ me.full_name }}</p>
      <p><strong>Username:</strong> {{ me.username }}</p>
      <p><button @click="deleteAccount()">Delete Account</button></p>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'ProfileView',
  created: function() {
    return this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({ me: 'stateMe' })
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount() {
      try {
        await this.deleteUser(this.me.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>
