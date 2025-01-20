<template>
  <!-- Header fixo no topo -->
  <div class="fixed w-full top-0" style="z-index: 1">
    <ItemHeader :title="itemStatus === 'found' ? 'Item Achado' : 'Item Perdido'" />
  </div>

  <!-- Conteúdo principal -->
  <div class="px-6 py-[120px] flex flex-col items-center gap-6" v-if="item">
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
        {{ itemStatus === 'found' ? 'Achado em:' : 'Perdido em:' }} {{ locationName || "Não especificado" }}
      </p>

      <!-- Labels dinâmicas -->
      <div class="flex flex-wrap gap-2 justify-center mt-2">
        <span
          v-for="(label, index) in labels"
          :key="index"
          :class="label.type === 'category' ? 'bg-blue-500' : label.type === 'brand' ? 'bg-laranja' : 'bg-gray-500'"
          class="px-4 py-2 rounded-full text-sm font-medium text-white"
        >
          {{ label.type === 'category' ? 'Categoria: ' : label.type === 'brand' ? 'Marca: ' : 'Cor: ' }}{{ label.name }}
        </span>
      </div>
    </div>

    <!-- Descrição -->
    <p class="text-sm md:text-base text-gray-700 text-center">
      {{ item.description }}
    </p>

    <!-- Botões diretamente no fluxo -->
    <button
      class="w-full py-3 text-center text-white font-semibold rounded-lg bg-laranja hover:bg-laranja active:bg-laranja focus:ring-2 focus:ring-laranja"
      @click="viewMatches"
    >
      {{ itemStatus === 'found' ? 'Ver possíveis matches' : 'Reportar possível match' }}
    </button>
    <button
      class="w-full py-3 text-center text-white font-semibold rounded-lg bg-verde hover:bg-verde active:bg-verde focus:ring-2 focus:ring-verde"
      @click="confirmItem"
    >
      {{ itemStatus === 'found' ? 'Achei este item' : 'Confirmar que é meu item' }}
    </button>
  </div>

  <div v-else class="py-6 text-center">
    <p class="text-gray-600">Carregando informações do item...</p>
  </div>

  <div class="fixed bottom-0 w-full">
    <MainMenu :activeIcon="itemStatus === 'found' ? 'found' : 'lost'" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api"; // Importa o arquivo api.js
import ItemHeader from "../components/Item-Header.vue";
import MainMenu from "../components/Main-Menu.vue";

const item = ref(null);
const itemStatus = ref("");
const locationName = ref("");
const labels = ref([]);

async function fetchItem() {
  try {
    // Busca o item pelo ID
    const response = await api.get(`/items/1`); // Substitua "1" pelo ID dinâmico do item
    item.value = response.data;

    // Determina o status do item (achado ou perdido)
    itemStatus.value = item.value.status === 'found' ? 'found' : 'lost';

    // Busca o nome do local
    if (item.value.location) {
      const locationResponse = await api.get(`/locations/${item.value.location}`);
      locationName.value = locationResponse.data.name;
    } else {
      locationName.value = "Não especificado";
    }

    // Adiciona as labels dinamicamente
    labels.value = [];

    // Categoria
    if (item.value.category) {
      const categoryIds = Array.isArray(item.value.category)
        ? item.value.category
        : [item.value.category];
      const categoryPromises = categoryIds.map((id) =>
        api.get(`/categories/${id}`).then((res) => ({ name: res.data.name, type: 'category' }))
      );
      const categories = await Promise.all(categoryPromises);
      labels.value.push(...categories);
    }

    // Cor
    if (item.value.color) {
      const colorResponse = await api.get(`/colors/${item.value.color}`);
      labels.value.push({ name: colorResponse.data.name, type: 'color' });
    }

    // Marca
    if (item.value.brand) {
      const brandResponse = await api.get(`/brands/${item.value.brand}`);
      labels.value.push({ name: brandResponse.data.name, type: 'brand' });
    }
  } catch (error) {
    console.error("Erro ao carregar item:", error);
  }
}

function viewMatches() {
  alert(itemStatus.value === 'found' ? "Exibindo possíveis matches!" : "Reportando possível match!");
}

function confirmItem() {
  alert(itemStatus.value === 'found' ? "Confirmando que o item foi encontrado." : "Confirmando que é o item perdido.");
}

// Carrega os dados do item e os detalhes relacionados quando o componente é montado
onMounted(fetchItem);
</script>

<style scoped></style>
