<template>
  <div class="fixed w-full top-0" style="z-index: 1">
    <ItemHeader title="Item Achado" />
  </div>

  <div class="px-6 py-[120px] flex flex-col items-center gap-6">
    <!-- Imagem do Item -->
    <img
      :src="item.image"
      alt="Imagem do Item"
      class="w-full max-w-md h-64 md:h-80 object-cover rounded-lg"
    />

    <!-- Título, local e tags -->
    <div class="text-center">
      <h1 class="text-lg md:text-2xl font-bold">{{ item.name }}</h1>
      <p class="text-sm md:text-base text-gray-500">
        Achado em: {{ item.location }}
      </p>
      <div class="flex flex-wrap gap-2 justify-center mt-2">
        <span
          v-for="tag in item.tags"
          :key="tag.text"
          :class="tag.color"
          class="px-3 py-1 rounded-full text-sm font-medium text-white"
        >
          {{ tag.text }}
        </span>
      </div>
    </div>

    <!-- Descrição -->
    <p class="text-sm md:text-base text-gray-700 text-center">
      {{ item.description }}
    </p>

    <button
      class="w-full py-3 text-center text-white font-semibold rounded-lg bg-laranja hover:bg-laranja active:bg-laranja focus:ring-2 focus:ring-laranja"
      @click="viewMatches"
    >
      Ver possíveis matches
    </button>
    <button
      class="w-full py-3 text-center text-white font-semibold rounded-lg bg-verde hover:bg-verde active:bg-verde focus:ring-2 focus:ring-verde"
      @click="confirmItem"
    >
      Achei este item
    </button>
  </div>

  <!-- Menu fixo na parte inferior -->
  <div class="fixed bottom-0 w-full">
    <MainMenu activeIcon="found" />
  </div>
</template>

<script setup>
import ItemHeader from "../components/Item-Header.vue";
import MainMenu from "../components/Main-Menu.vue";

const item = {
  name: "Gloss Labial",
  location: "UAC",
  tags: [
    { text: "Cosmético", color: "bg-blue-500" },
    { text: "Vermelho", color: "bg-red-500" },
    { text: "Pequeno", color: "bg-purple-500" },
  ],
  description: "Hidratante labial da Nívea morango",
  image: "https://via.placeholder.com/400", // Substituir pela URL da imagem real
};

function viewMatches() {
  alert("Exibindo possíveis matches!");
}

function confirmItem() {
  alert("Confirmando que o item foi encontrado.");
}
</script>

<style scoped></style>
