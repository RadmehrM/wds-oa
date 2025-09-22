<template>
  <div>
    <Nav />
    <RouterView />
  </div>
</template>

<script>
import Nav from './components/Nav.vue'
import { RouterLink, RouterView } from 'vue-router'

export default {
  components: {
    Nav
  }
}
</script>

