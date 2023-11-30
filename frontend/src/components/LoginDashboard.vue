<template>
  <div class="login bordered">
    <h3>
      This is the Login.vue component
    </h3>
    <button @click="getPrivateData">Status</button>
    <button @click="loginRedirect">Login</button>
    <button @click="logoutRedirect">Logout</button>
    <div v-if="responseData">
      <p>{{ responseData }}</p>

    </div>
    <div v-else>
      <p>Click the Status button to view your login status</p>
    </div>
  </div>
</template>

<script setup>
import { viewPrivate, loginRedirect, logoutRedirect } from '@/services/api';  
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
    responseData.value = `${error.message}`;
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

.login button {
  margin: 0 10px; /* Adds horizontal margin to each button */
}

@media (min-width: 1024px) {
  .login h1,
  .login h3 {
    text-align: left;
  }

  .login button {
    margin: 0 15px; /* Slightly larger margin for wider screens */
  }
}
</style>

