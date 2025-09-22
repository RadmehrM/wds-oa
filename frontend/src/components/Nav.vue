<template>
  <nav
    class="navbar navbar-expand-lg p-3 fixed-top d-flex justify-content-between vw-100"
    :class="{ 'navbar-scrolled': scrolled }"
    :style="navbarStyle"
  >
    <button
      v-if="isMobile"
      class="navbar-toggler border border-white mx-auto mb-2 d-block"
      @click="toggleMenu"
      type="button"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <transition name="navbar-collapse" 
    @enter="enter"
    @leave="leave">
      <div
        class="ms-auto navbar-collapse"
        id="navbarNav"
        v-show="isMenuOpen"
        :style="navbarStyle"
      >
        <ul class="navbar-nav ms-auto p-3">
          <li class="nav-item align-self-center">
            <RouterLink class="nav-link btn-outline-primary rounded-pill px-4" to="/"
              >Home</RouterLink
            >
          </li>
          <li class="nav-item align-self-center">
            <RouterLink class="nav-link btn-outline-primary rounded-pill px-4" to="/"
              >Why Me?</RouterLink
            >
          </li>
          <li class="nav-item align-self-center">
            <RouterLink class="nav-link btn-outline-primary rounded-pill px-4" to="/Courses"
              >Lucy Pictures</RouterLink
            >
          </li>
          <li class="nav-item align-self-center">
            <RouterLink class="nav-link btn-outline-primary rounded-pill px-4" to="/facilities"
              >Dice Roller</RouterLink
            >
          </li>
           <li class="nav-item align-self-center">
              <button class="nav-link btn-outline-primary rounded-pill px-4" @click="showModal()">
                Contact
              </button>
            </li>
        </ul>
      </div>
    </transition>
  </nav>

   <!-- Contact Form Modal -->
  <div ref="BootstrapModal" class="modal fade" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Contact Me</h5>
          <button type="button" class="btn-close" @click="hideModal()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitContact">
            <input v-model="contact.name" type="text" placeholder="Your Name" required class="form-control mb-2" />
            <input v-model="contact.email" type="email" placeholder="Your Email" required class="form-control mb-2" />
            <textarea v-model="contact.message" placeholder="Your Message" required class="form-control mb-2"></textarea>
            <button type="submit" class="btn btn-primary">Send</button>
            <button type="button" class="btn btn-secondary ms-2" @click="hideModal()">Close</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'
import * as bootstrap from 'bootstrap'
import axios from 'axios'


const isMenuOpen = ref(false)
const isMobile = ref(window.innerWidth < 1024)

const router = useRouter()

const scrolled = ref(false)

const navbarStyle = computed(() => ({
  backgroundColor:
    scrolled.value === true ? '#2a0286' : isMenuOpen.value === true ? '#2a0286' : 'transparent',
}))

const BootstrapModal = ref(null)
const modal = ref(null)

const contact = ref({ name: '', email: '', message: '' })

const submitContact = () => {
  axios.post(`http://127.0.0.1:8000/api/savecontact/`, contact.value)
    .then(() => {
      alert('Message sent and saved to the database!\n' + JSON.stringify(contact.value, null, 2));
      contact.value = { name: '', email: '', message: '' };
    })
    .catch(() => {
      alert('Failed saving to database. Hint: Make sure to start up your backend server');
    });

    hideModal()

}




const showModal = () => {
  modal.value.show()
}

const hideModal = () => {
  modal.value.hide()
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const handleResize = () => {
  isMobile.value = window.innerWidth < 993
  if (!isMobile.value) {
    isMenuOpen.value = false 
  }
}

const handleScroll = () => {
  scrolled.value = window.scrollY > 50 
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
  window.addEventListener('scroll', handleScroll)
  handleResize()
  modal.value = new bootstrap.Modal(BootstrapModal.value)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})
</script>

