<script setup>
</script>


<template>
  <div class="login bordered">
    <h3>
      This is the Login.vue component
    </h3>
    <button @click="">Login</button>
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