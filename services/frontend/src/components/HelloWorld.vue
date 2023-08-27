<template>
  <div>
    <p> {{ message }} </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TestComponent',
  data() {
    return {
      msg: '',
    }
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
  },
  created() {
    this.getMessage()
  },
}
</script>

<style scoped>
</style>
