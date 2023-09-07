<script setup>
import { ref} from 'vue';
import { fetchData } from '@/services/api';  

// Declare reactive variable to store fetched data
const data = ref(null);
// 

const makeApiCall = async () => {
  const response = await fetchData();
  if (response) {
    const responseData = await response;
    data.value = responseData;
  } else {
    data.value = `Error: ${response.status}`;
    console.error(`Error: ${response}`);
  }
};
</script>

<template>
    <div>
      <h1>This is the ViewMessage.vue component</h1>
        <button @click="makeApiCall">Make API Call</button>
        <pre v-if="data">{{ data }}</pre>
    </div>
</template>

<style scoped>

</style>