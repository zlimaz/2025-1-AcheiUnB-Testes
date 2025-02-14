<template>
  <div class="min-h-screen pb-32">
    <div
      v
      class="grid grid-cols-[repeat(auto-fit,_minmax(180px,_1fr))] sm:grid-cols-[repeat(auto-fit,_minmax(200px,_1fr))] justify-items-center align-items-center lg:px-3 gap-y-3 pb-10"
    >
      <ItemCard
        v-for="item in foundItems"
        :key="item.id"
        :name="item.name"
        :location="item.location_name"
        :time="formatTime(item.created_at)"
        :image="item.image_urls[0] || NotAvailableImage"
        :id="item.id"
      ></ItemCard>
    </div>
  </div>
</template>

<script setup>
import ItemCard from "../components/Item-Card.vue";
import { ref, watch, onMounted } from "vue";
import { fetchFoundItems } from "@/services/apiItems";
import { formatTime } from "@/utils/dateUtils";
import NotAvailableImage from "@/assets/images/not-available.png";
import { filtersState } from "@/store/filters";

const foundItems = ref([]);
const currentPage = ref(1);
const totalPages = ref(1);

const fetchItems = async (page = 1) => {
  const { searchQuery, activeCategory, activeLocation } = filtersState;

  const response = await fetchFoundItems({
    page,
    search: searchQuery,
    category_name: activeCategory,
    location_name: activeLocation,
  });

  foundItems.value = response.results;
  totalPages.value = Math.ceil(response.count / 27); // 20 itens por página
};

// Navegação de páginas
const goToPreviousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value -= 1;
    fetchItems(currentPage.value);
  }
};

const goToNextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value += 1;
    fetchItems(currentPage.value);
  }
};

watch(
  () => [filtersState.searchQuery, filtersState.activeCategory, filtersState.activeLocation],
  () => {
    currentPage.value = 1; // Reseta para a primeira página ao mudar os filtros
    fetchItems(); // Atualiza os itens na tela
  },
);

onMounted(() => fetchItems(currentPage.value));
</script>

<style scoped></style>
