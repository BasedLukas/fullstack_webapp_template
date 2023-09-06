<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})

import { ref} from 'vue';
import { fetchData } from '@/services/api';  // Adjust the import to match your project structure

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
  <div class="greetings">
    <h3>
      This is the HelloWorld.vue component
    </h3>
    <h1 class="green">Here is a message passed in to the Hello World Component: {{ msg }}</h1>
    <button @click="makeApiCall">Make API Call</button>
    <pre v-if="data">{{ data }}</pre>
  </div>
</template>

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

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
