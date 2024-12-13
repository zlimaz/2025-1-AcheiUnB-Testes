<template>
    <div
    class="h-full bg-verde shadow-md rounded-b-xl flex items-center justify-between text-white gap-x-9 p-4"
    >
      <div class="flex-1">
        <SearchBar />
      </div>
      <button
      >
      <router-link to="/about" class="no-underline text-white"><Logo class="pr-4" sizeClass="text-2xl" /></router-link>
        
      </button>
    </div>
  </template>

<script>
import SearchBar from './SearchBar.vue';
import Logo from './Logo.vue';

export default {
  name: "Header",
    components: {
        SearchBar,
        Logo,
  },
};
</script>

<style scoped>

</style>