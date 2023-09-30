<template>
  <h1>Users</h1>
  <hr/><br/>

  <div v-for="user in users" :key="user.id">
    <ul>
      <li><strong>ID:</strong> {{ user.id }}</li>
      <li><strong>Nickname:</strong> {{ user.username }}</li>
      <li><strong>Full name:</strong> {{ user.full_name }}</li>
      <li><router-link :to="{name: 'User', params:{id: user.id}}">View</router-link></li>
    </ul>
    <br/>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters } from 'vuex';

export default defineComponent({
  name: 'UsersView',
  created: function() {
    return this.$store.dispatch('viewFriends');
  },
  computed: {
    ...mapGetters({ users: 'stateUsers' })
  },
});
</script>
