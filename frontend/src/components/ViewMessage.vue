<script setup>
import { computed, ref} from 'vue';
import { fetchData } from '@/services/api';  
import { useCounterStore } from '@/stores/counter';


// Declare reactive variable to store fetched data
const data = ref(null);
const counterStore = useCounterStore();

// computed property state.count
const count = computed(() => counterStore.count); 

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
    <div class="bordered">
      <h1>This is the ViewMessage.vue component</h1>
      <p>Number of successful sent messages: {{ count }}</p>
        <button @click="makeApiCall">Make API Call</button>
        <pre v-if="data">{{ data }}</pre>
    </div>
</template>

<style scoped>
.bordered {
  border: solid rgb(242, 29, 29);  /* 2px width, solid line, black color */
}
</style>