<template>
  <div class="h-screen">
    <div class="sticky top-0">
      <Header />
    </div>
    <div
      class="grid grid-cols-[repeat(auto-fit,_minmax(180px,_1fr))] sm:grid-cols-[repeat(auto-fit,_minmax(200px,_1fr))] justify-items-center align-items-center p-3 gap-y-3"
    >
      <ItemCard image="/src/assets/images/carteira.png" />
      <ItemCard image="/src/assets/images/gloss.png" />
      <ItemCard image="/src/assets/images/caneta.png" />
      <ItemCard image="/src/assets/images/sombrinha.png" />
      <ItemCard />
      <ItemCard image="/src/assets/images/bone.png" />
      <ItemCard image="/src/assets/images/carteira.png" />
      <ItemCard image="/src/assets/images/gloss.png" />
      <ItemCard image="/src/assets/images/caneta.png" />
      <ItemCard image="/src/assets/images/sombrinha.png" />
      <ItemCard />
      <ItemCard image="/src/assets/images/bone.png" />
    </div>

    <ButtonAdd class="" />
    <div class="fixed bottom-0 w-full">
      <MainMenu activeIcon="search" />
    </div>
  </div>
</template>

<script setup>
import MainMenu from "../components/Main-Menu.vue";
import ItemCard from "../components/Item-Card.vue";
import ButtonAdd from "../components/Button-Add.vue";
import Header from "../components/Header.vue";
import SearchBar from "@/components/SearchBar.vue";
</script>

<style scoped></style>
