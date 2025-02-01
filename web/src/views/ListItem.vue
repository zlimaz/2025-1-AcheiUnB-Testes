<template>
  <div class="fixed w-full top-0 z-[1]">
    <ItemHeader :title="itemStatus === 'found' ? 'Item Achado' : 'Item Perdido'" />
  </div>

  <div class="px-6 py-[120px] flex flex-col items-center gap-6" v-if="item">
    <!-- Container de Imagens Responsivo -->
    <div class="w-full max-w-md relative">
      <!-- Imagem padrão quando não há fotos -->
      <div v-if="!item.image_urls || item.image_urls.length === 0" class="w-full h-64">
        <img
          :src="notAvailableImage"
          alt="Imagem não disponível"
          class="w-full h-full object-contain"
        />
      </div>

      <!-- Grid para desktop -->
      <div 
        v-else
        class="hidden md:grid"
        :class="item.image_urls.length === 1 ? 'grid-cols-1 justify-items-center' : 'grid-cols-2 gap-4'"
      >
        <img
          v-for="(url, index) in item.image_urls.slice(0,2)"
          :key="index"
          :src="url"
          :alt="`Imagem ${index + 1} do item`"
          class="h-64 object-cover rounded-lg"
          :class="item.image_urls.length === 1 ? 'w-full' : ''"
        />
      </div>

      <!-- Carrossel para mobile -->
      <div 
        v-if="item.image_urls && item.image_urls.length > 0"
        class="md:hidden overflow-hidden relative"
      >
        <div
          class="flex transition-transform duration-300 ease-out snap-x snap-mandatory"
          :style="{ transform: `translateX(-${activeIndex * 100}%)` }"
        >
          <div
            v-for="(url, index) in item.image_urls"
            :key="index"
            class="w-full flex-shrink-0 relative snap-start"
          >
            <img
              :src="url"
              :alt="`Imagem ${index + 1} do item`"
              class="w-full h-64 object-cover rounded-lg"
            />
          </div>
        </div>

        <!-- Indicadores -->
        <div v-if="item.image_urls.length > 1" class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2">
          <div
            v-for="(_, index) in item.image_urls"
            :key="index"
            class="w-2 h-2 rounded-full transition-colors duration-300"
            :class="activeIndex === index ? 'bg-white' : 'bg-gray-300'"
          />
        </div>

        <!-- Botões de navegação -->
        <button
          v-if="item.image_urls.length > 1"
          @click="prevImage"
          class="absolute left-2 top-1/2 transform -translate-y-1/2 bg-white/30 rounded-full p-2 backdrop-blur-sm"
        >
          ←
        </button>
        <button
          v-if="item.image_urls.length > 1"
          @click="nextImage"
          class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-white/30 rounded-full p-2 backdrop-blur-sm"
        >
          →
        </button>
      </div>
    </div>

    <!-- Container de texto alinhado à esquerda -->
    <div class="w-full max-w-md">
      <h1 class="text-lg md:text-2xl font-bold text-left">{{ item.name }}</h1>
      
      <p class="text-sm md:text-base text-gray-500 text-left mt-2">
        {{ itemStatus === "found" ? "Achado em:" : "Perdido em:" }}
        {{ item.location_name || "Não especificado" }}
      </p>

      <div class="flex flex-wrap gap-2 justify-start mt-4">
        <span
          v-if="item.category_name"
          class="px-4 py-2 rounded-full text-sm font-medium text-white bg-blue-500"
        >
          Categoria: {{ item.category_name }}
        </span>
        
        <span
          v-if="item.brand_name"
          class="px-4 py-2 rounded-full text-sm font-medium text-white bg-laranja"
        >
          Marca: {{ item.brand_name }}
        </span>
        
        <span
          v-if="item.color_name"
          class="px-4 py-2 rounded-full text-sm font-medium text-white bg-gray-500"
        >
          Cor: {{ item.color_name }}
        </span>
      </div>

      <p class="text-sm md:text-base text-gray-700 text-left mt-4">
        {{ item.description }}
      </p>
    </div>

    <!-- Botão centralizado -->
    <button
      class="w-full md:w-1/3 py-3 text-center text-white font-semibold rounded-full bg-laranja hover:bg-laranja active:bg-laranja focus:ring-2 focus:ring-laranja mt-8"
      @click="startChat"
    >
      É meu item
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
import { ref, onMounted, onBeforeUnmount, nextTick } from "vue";
import api from "../services/api";
import ItemHeader from "../components/Item-Header.vue";
import MainMenu from "../components/Main-Menu.vue";
import { useRoute, useRouter } from "vue-router";
import notAvailableImage from "@/assets/images/not-available.png";

const route = useRoute();
const router = useRouter();
const item = ref(null);
const itemStatus = ref("");
const currentUser = ref(null);
const activeIndex = ref(0);
const isMobile = ref(window.innerWidth < 768);

// Carrossel
const nextImage = () => {
  activeIndex.value = (activeIndex.value + 1) % item.value.image_urls.length;
};

const prevImage = () => {
  activeIndex.value = (activeIndex.value - 1 + item.value.image_urls.length) % item.value.image_urls.length;
};

// Responsividade
const handleResize = () => {
  isMobile.value = window.innerWidth < 768;
};

async function fetchItem() {
  try {
    const response = await api.get(`/items/${route.query.idItem}/`);
    item.value = response.data;
    itemStatus.value = item.value.status;
    
    if (item.value.image_urls && item.value.image_urls.length > 0) {
      await nextTick();
    }
  } catch (error) {
    console.error("Erro ao carregar item:", error);
  }
}

async function fetchCurrentUser() {
  try {
    const response = await api.get(`/auth/user/`);
    currentUser.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar usuário:", error);
  }
}

async function startChat() {
  try {
    if (!currentUser.value?.id || !item.value?.user_id) return;

    const chatData = {
      participant_1: currentUser.value.id,
      participant_2: item.value.user_id,
      item_id: route.query.idItem
    };

    const chatResponse = await api.post("/chat/chatrooms/", chatData);
    router.push(`/chat/${chatResponse.data.id}`);
  } catch (error) {
    console.error("Erro ao criar chat:", error.response?.data || error.message);
  }
}

onMounted(async () => {
  window.addEventListener('resize', handleResize);
  await fetchCurrentUser();
  await fetchItem();
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize);
});
</script>