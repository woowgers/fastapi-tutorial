<template>
  <div>
    <p><strong>ID:</strong> {{ user.id }} </p>
    <p><strong>Username:</strong> {{ user.username }} </p>
    <p><strong>Full name:</strong> {{ user.full_name }} </p>
    <p><button @click="AddFriend()">Add friend</button></p>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'UserView',
  props: ['id'],
  async created() {
    try {
      await this.viewUser(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/users');
    }
  },
  computed: {
    ...mapGetters({ user: 'stateUser', me: 'stateMe' }),
  },
  methods: {
    ...mapActions(['viewUser', 'addFriend']),
    async AddFriend() {
      try {
        await this.addFriend(this.user.id);
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>
