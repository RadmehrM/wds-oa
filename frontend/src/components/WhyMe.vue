<template>
  <section class="why-me">
    <div class="cat-wrapper d-flex justify-content-center align-items-center">
        <button type="button" @click="getCatPhoto(); showModal()" class="btn btn-outline-light">Click Here for a random picture of Lucy the Cat</button>
    </div>
    <div class="why-me-content p-4">
      <h2 class="why-me-header mt-4 p-4">Why Choose Me?</h2>
      <div class="feature-list p-5">
        <div class="d-flex mb-4">
          <div class="me-3 text-primary">
            <i class="bi bi-check-circle-fill fs-5"></i>
          </div>
          <p class="mb-0 light-300 why-me-bullet">
            Proven full-stack development experience with Vue.js, Django, and PostgreSQL, delivering production-ready contract management tools at Bell Canada
          </p>
        </div>
        <div class="d-flex mb-4">
          <div class="me-3 text-primary">
            <i class="bi bi-check-circle-fill fs-5"></i>
          </div>
          <p class="mb-0 light-300 why-me-bullet">
            Strong ability to optimize workflows, demonstrated by automating manual processes that reduced a two-week task to a single day
          </p>
        </div>
        <div class="d-flex mb-4">
          <div class="me-3 text-primary">
            <i class="bi bi-check-circle-fill fs-5"></i>
          </div>
          <p class="mb-0 light-300 why-me-bullet">
            Leadership experience as a team lead for Western Developer Society, managing 8 developers and ensuring timely delivery of client projects
          </p>
        </div>
        <div class="d-flex mb-4">
          <div class="me-3 text-primary">
            <i class="bi bi-check-circle-fill fs-5"></i>
          </div>
          <p class="mb-0 light-300 why-me-bullet">
            Skilled in building scalable, user-friendly solutions, from REST APIs and real-time databases to interactive data visualization tools
          </p>
        </div>
      </div>
    </div>
  </section>

  <div ref="BootstrapModal" class="modal fade" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">{{ cat.description }}</h5>
        <button type="button" class="btn-close" @click="hideModal()" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <img :src="catImageUrl" alt="Cat" class="img-fluid" />
      </div>
      <div class="modal-footer">
        <button type="button" @click="hideModal()" class="btn btn-secondary">Close</button>
      </div>
    </div>
  </div>
</div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as bootstrap from 'bootstrap'
import axios from 'axios'
const BootstrapModal = ref(null)
const modal = ref(null)

const showModal = () => {
  modal.value.show()
}

const hideModal = () => {
  modal.value.hide()
}

const cat = ref({})
const catImageUrl = ref("")


const getCatPhoto = async () => {
  const randomId = Math.floor(Math.random() * 3) + 1;
  const response = await axios.get(`http://127.0.0.1:8000/api/showcat/${randomId}/`);
  cat.value = response.data
  // Prepend the base64 string with proper data URI
  catImageUrl.value = "data:image/jpeg;base64," + response.data.image_base64
}


onMounted(() => {
  modal.value = new bootstrap.Modal(BootstrapModal.value)
});
</script>