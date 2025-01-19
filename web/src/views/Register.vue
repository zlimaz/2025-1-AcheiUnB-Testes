<template>
  <div class="fixed w-full top-0" style="z-index: 1">
    <Header />
  </div>

  <div class="px-6 py-[140px]" style="z-index: 2">
    <Form />
  </div>

  <div class="fixed bottom-0 w-full">
    <MainMenu activeIcon="search" />
  </div>
</template>

<script setup>
import Form from "../components/Form.vue";
import Header from "../components/Header.vue";
import MainMenu from "../components/Main-Menu.vue";
</script>

<style scoped></style>
