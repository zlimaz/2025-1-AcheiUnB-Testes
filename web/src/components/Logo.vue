<template>
  <h1 :class="['text-5xl italic', customClass || 'text-light']">
    Achei<span class="text-5xl font-bold">UnB</span>
  </h1>
</template>

<script>
export default {
  props: {
    customClass: {
      type: String,
    },
  },
};
</script>

<style scoped></style>
