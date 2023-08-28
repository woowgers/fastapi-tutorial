<template>
  <p><strong>Nickname:</strong> {{ user.username }}</p>
  <p><strong>Full name:</strong> {{ user.full_name }}</p>
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
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['viewUser']),
  },
});
</script>
