<template>
  <div class="flex pt-10 space-x-8 justify-center">
    <router-link
      to="/user-items-found"
      class="no-underline text-lg font-inter font-bold text-cinza3 transform hover:scale-110 origin-center transition-transform duration-200"
    >
      Achados
    </router-link>
    <div class="flex-col space-y-1">
      <span class="font-inter font-bold text-laranja text-lg">Perdidos</span>
      <div class="h-[2px] bg-laranja"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SubMenu",
};
</script>

<style scoped></style>
