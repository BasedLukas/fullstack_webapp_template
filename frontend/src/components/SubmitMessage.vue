<script setup>
import { ref} from 'vue';
import { postData } from '@/services/api';  

const responseData = ref(null);

const makeApiCall = async (message) => {
  try {
    const response = await postData({ message: message });
    if (response) {
      responseData.value = response.message;
    }
  } catch (error) {
    responseData.value = `Error: ${error.message}`;
    console.error(`Error: ${error.message}`);
  }
};

</script>

<template>
    <div>
      <h1>This is the SubmitMessage.vue component</h1>
      <p>Write your message here:</p>
      <!-- Input Box -->
      <input type="text" v-model="message" />
      <!-- Button -->
      <button @click="makeApiCall(message)">Submit</button>
      <!-- Display response -->
      <p>Response: {{ responseData }}</p>
    </div>
  </template>
  

<style scoped>

</style>