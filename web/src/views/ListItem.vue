<template>
  <div class="fixed w-full top-0 z-[1]">
    <ItemHeader :title="itemStatus === 'found' ? 'Item Achado' : 'Item Perdido'" />
  </div>

  <div class="px-6 py-[120px] flex flex-col items-center gap-6" v-if="item">
    <!-- Container principal para desktop -->
    <div class="w-full md:flex md:gap-8 md:max-w-4xl">
      <!-- Container de Imagens (Esquerda) -->
      <div class="w-full max-w-md md:max-w-none md:w-1/2 relative">
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
          :class="item.image_urls.length === 1 ? 'grid-cols-1' : 'grid-cols-2 gap-4'"
        >
          <img
            v-for="(url, index) in item.image_urls.slice(0,2)"
            :key="index"
            :src="url"
            :alt="`Imagem ${index + 1} do item`"
            class="h-64 w-full object-cover rounded-lg"
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

      <!-- Container de Informações (Direita) -->
      <div class="w-full md:w-1/2 mt-6 md:mt-0">
        <h1 class="text-lg md:text-2xl font-bold text-left">{{ item.name }}</h1>
        
        <p class="text-sm md:text-base text-gray-500 text-left mt-2">
          {{ itemStatus === "found" ? "Achado em:" : "Perdido em:" }}
          {{ item.location_name || "Não especificado" }}
        </p>

        <!-- Data e horário com validação -->
        <p 
          v-if="shouldShowDateTime"
          class="text-sm md:text-base text-gray-500 text-left mt-1"
        >
          {{ itemStatus === "found" ? "Data do achado:" : "Data da perda:" }}
          {{ formatDateTime(item.found_lost_date) }}
        </p>

        <div class="flex flex-wrap gap-2 justify-start mt-4">
          <!-- ... (tags de categoria/marca/cor mantidas) ... -->
        </div>

        <p class="text-sm md:text-base text-gray-700 text-left mt-4">
          {{ item.description }}
        </p>
      </div>
    </div>

    <!-- Botão com efeito hover -->
    <button
    class="bg-laranja text-white w-full md:w-[70%] lg:w-[40%] font-medium py-4 rounded-full hover:scale-110 transition-transform duration-300 text-center text-lg lg:text-xl"
    @click="handleChat"
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
import { ref, onMounted, onBeforeUnmount, nextTick, computed } from "vue";
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

// Validação de datas para itens perdidos
const isValidLostDate = (dateString) => {
  const date = new Date(dateString);
  const minDate = new Date('2023-01-01T00:00:00-03:00'); // Fuso horário de Brasília
  const today = new Date();
  
  // Considera até o final do dia atual
  const endOfToday = new Date();
  endOfToday.setHours(23, 59, 59, 999);

  return date >= minDate && date <= endOfToday;
};

const shouldShowDateTime = computed(() => {
  if (!item.value.found_lost_date) return false;
  
  if (itemStatus.value === 'found') return true;
  
  return isValidLostDate(item.value.found_lost_date);
});

// Formatar data e hora
const formatDateTime = (dateString) => {
  const date = new Date(dateString);
  return `${date.toLocaleDateString('pt-BR', {
    timeZone: 'America/Sao_Paulo'
  })} às ${date.toLocaleTimeString('pt-BR', {
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'America/Sao_Paulo'
  })}`;
};

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

// Função para buscar o item
async function fetchItem() {
  try {
    const response = await api.get(`/items/${route.query.idItem}/`);
    item.value = response.data;
    itemStatus.value = item.value.status;
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
const handleChat = async () => {
  try {
    if (!currentUser.value?.id || !item.value?.user_id) {
      console.error("Erro: IDs de usuário inválidos");
      return;
    }

    // Verificar se já existe um chatroom
    const existingRoom = await findExistingChatroom();
    
    if (existingRoom) {
      // Redirecionar para o chat existente
      router.push(`/chat/${existingRoom.id}`);
      return;
    }

    // Criar novo chatroom
    const chatData = {
      participant_1: currentUser.value.id,
      participant_2: item.value.user_id,
      item_id: item.value.id
    };

    const response = await api.post("/chat/chatrooms/", chatData);
    
    if (response.data?.id) {
      // Redirecionar para o novo chat
      router.push(`/chat/${response.data.id}`);
    } else {
      throw new Error("Resposta inválida ao criar chatroom");
    }

  } catch (error) {
    console.error("Erro ao criar/aceder chat:", error.response?.data || error.message);
    alert("Ocorreu um erro ao iniciar o chat. Por favor, tente novamente.");
  }
};

// Função para buscar chatroom existente
const findExistingChatroom = async () => {
  try {
    const response = await api.get("/chat/chatrooms/", {
      params: {
        participant_1: currentUser.value.id,
        participant_2: item.value.user_id,
        item_id: item.value.id
      }
    });

    if (response.data?.results?.length > 0) {
      return response.data.results[0];
    }
    return null;
  } catch (error) {
    console.error("Erro ao buscar chatrooms:", error);
    return null;
  }
};

onMounted(async () => {
  window.addEventListener('resize', handleResize);
  await fetchCurrentUser();
  await fetchItem();
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize);
});
</script>