


<template>
  <div class="login bordered">
    <h3>
      This is the Login.vue component
    </h3>
    <div v-if="responseData">
      <p>Response: {{ responseData }}</p>
    </div>
    <button @click="getPrivateData">Login</button>
  </div>
</template>

<script setup>
import { viewPrivate } from '@/services/api';  
import { ref } from 'vue';

const responseData = ref(null);

const getPrivateData = async () => {
  try {
    const response = await viewPrivate();
    if (response) {
      // Assuming the JWT is in the response and you want to display it directly
      responseData.value = response;
    }
  } catch (error) {
    responseData.value = `Error: ${error.message}`;
    console.error(`Error: ${error.message}`);
  }
};
</script>
<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.login h1, .login h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .login h1,
  .login h3 {
    text-align: left;
  }
}
</style>