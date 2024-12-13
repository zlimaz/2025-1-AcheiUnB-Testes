<template>
  <div class="flex space-x-1">
    <h1 :class="[customClass || 'text-light']">
      <span class="italic" :class="sizeClass">Achei</span>
    </h1>
    <h1 :class="[customClass || 'text-light']">
      <span class="font-bold" :class="sizeClass">UnB</span>
    </h1>
  </div>
</template>

<script>
export default {
  props: {
    customClass: {
      type: String,
    },
    sizeClass: {
      type: String,
      default: "text-5xl",
    },
  },
};
</script>

<style scoped></style>
