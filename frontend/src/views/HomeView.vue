<template>

  <Banner />


  <div id="why-me">
    <WhyMe />
  </div>

  <div id="dice-roller">
    <DiceRoll />
  </div>

</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import DiceRoll from '@/components/DiceRoll.vue';
import WhyMe from '@/components/WhyMe.vue'
import Banner from '@/components/Banner.vue';



const isMobile = ref(false)

const checkIsMobile = () => {
  isMobile.value = window.innerWidth <= 768
}



onMounted(() => {
  checkIsMobile()
  window.addEventListener('resize', checkIsMobile)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkIsMobile)
})
</script>

<style scoped>


</style>


