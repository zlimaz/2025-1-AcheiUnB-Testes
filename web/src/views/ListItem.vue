<template>
  <div class="fixed w-full top-0 z-[1]" v-if="isLoaded">
    <ItemHeader 
      :title="itemStatus === 'found' ? 'Item Achado' : 'Item Perdido'"
      :userId="currentUser.id"
      :itemUserId="item.user_id"
      :itemId="item.id"
      />
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

        <div
          v-else
          class="hidden md:grid"
          :class="item.image_urls.length === 1 ? 'grid-cols-1' : 'grid-cols-2 gap-4'"
        >
          <img
            v-for="(url, index) in item.image_urls.slice(0, 2)"
            :key="index"
            :src="url"
            :alt="`Imagem ${index + 1} do item`"
            class="h-64 w-full object-cover rounded-lg"
          />
        </div>

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

          <div
            v-if="item.image_urls.length > 1"
            class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2"
          >
            <div
              v-for="(_, index) in item.image_urls"
              :key="index"
              class="w-2 h-2 rounded-full transition-colors duration-300"
              :class="activeIndex === index ? 'bg-white' : 'bg-gray-300'"
            />
          </div>

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

      <div class="w-full md:w-1/2 mt-6 md:mt-0">
        <h1 class="text-lg md:text-2xl font-bold break-words">{{ item.name }}</h1>

        <!-- Sempre exibe o local com o rótulo "Achado em:" -->
        <p class="text-sm md:text-base text-gray-500 text-left mt-2">
          Achado em: {{ item.location_name || "Não especificado" }}
        </p>

        <p
          v-if="item.found_lost_date && itemStatus === 'found'"
          class="text-sm md:text-base text-gray-500 text-left mt-1"
        >
          Data do achado: {{ formatDateTime(item.found_lost_date) }}
        </p>
        <p
          v-else-if="item.found_lost_date && itemStatus === 'lost'"
          class="text-sm md:text-base text-gray-500 text-left mt-1"
        >
          Data da perda: {{ formatDateTime(item.found_lost_date) }}
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
    </div>

    <button
      class="bg-laranja text-white w-full md:w-[70%] lg:w-[40%] font-medium py-4 rounded-full hover:scale-110 transition-transform duration-300 text-center text-lg lg:text-xl"
      @click="handleChat"
    >
      É meu item
    </button>

    <button
    v-if="currentUser.id == item.user_id"
      class="bg-red-500 text-white w-full md:w-[70%] lg:w-[40%] font-medium py-4 rounded-full hover:scale-110 transition-transform duration-300 text-center text-lg lg:text-xl"
      @click="confirmDelete(item.id)"
    >
      Excluir meu item
    </button>
  </div>

  <div class="fixed bottom-0 w-full">
    <MainMenu :activeIcon="itemStatus === 'found' ? 'found' : 'lost'" />
  </div>

  <Alert v-if="submitError" type="error" :message="alertMessage" @closed="submitError = false" />
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import api from "../services/api";
import ItemHeader from "../components/Item-Header.vue";
import MainMenu from "../components/Main-Menu.vue";
import { useRoute, useRouter } from "vue-router";
import notAvailableImage from "@/assets/images/not-available.png";
import Alert from "@/components/Alert.vue";
import { deleteItem } from "@/services/apiItems";

const route = useRoute();
const router = useRouter();
const item = ref(null);
const itemStatus = ref("");
const currentUser = ref(null);
const activeIndex = ref(0);
const isMobile = ref(window.innerWidth < 768);
const alertMessage = ref("");
const submitError = ref(false);
// Flag que indica se os dados foram carregados
const isLoaded = ref(false);

// Função para confirmar exclusão
const confirmDelete = async (itemId) => {
  console.log(itemStatus.value);
  console.log(item.value.id);
  try {
    await deleteItem(itemId); // Chama a API para excluir o item
    router.push(`/${itemStatus.value}`)
  } catch (error) {
    console.error("Erro ao excluir item:", error);
    alertMessage.value = "Erro ao excluir item.";
    submitError.value = true;
  }
};

const formatDateTime = (dateString) => {
  const date = new Date(dateString);
  return `${date.toLocaleDateString("pt-BR", {
    timeZone: "America/Sao_Paulo"
  })} às ${date.toLocaleTimeString("pt-BR", {
    hour: "2-digit",
    minute: "2-digit",
    timeZone: "America/Sao_Paulo"
  })}`;
};

const nextImage = () => {
  activeIndex.value =
    (activeIndex.value + 1) % item.value.image_urls.length;
};

const prevImage = () => {
  activeIndex.value =
    (activeIndex.value - 1 + item.value.image_urls.length) %
    item.value.image_urls.length;
};

const handleResize = () => {
  isMobile.value = window.innerWidth < 768;
};

async function fetchItem() {
  try {
    const response = await api.get(`/items/${route.query.idItem}/`);
    item.value = response.data;
    itemStatus.value = item.value.status;
    isLoaded.value = true;
  } catch (error) {
    console.error("Erro ao carregar item:", error);
    alertMessage.value = "Erro ao carregar item.";
    submitError.value = true;
  }
}

async function fetchCurrentUser() {
  try {
    const response = await api.get(`/auth/user/`);
    currentUser.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar usuário:", error);
    alertMessage.value = "Erro ao buscar usuário.";
    submitError.value = true;
  }
}

const handleChat = async () => {
  try {
    if (!item.value || !item.value.id) {
      console.error("Item inválido ou não carregado:", item.value);
      return;
    }
    if (!currentUser.value?.id || !item.value?.user_id) {
      console.error("IDs de usuário inválidos:", {
        currentUser: currentUser.value,
        item: item.value
      });
      return;
    }
    console.log("Item atual (ID):", item.value.id);
    console.log("Dono do item (user_id):", item.value.user_id);
    console.log("Usuário atual (ID):", currentUser.value.id);

    const searchParams = {
      participant_1: currentUser.value.id,
      participant_2: item.value.user_id,
      item_id: item.value.id
    };
    console.log("Parâmetros para busca de chat:", searchParams);

    const searchResponse = await api.get("/chat/chatrooms/", {
      params: searchParams
    });
    const chatsEncontrados = searchResponse.data;
    console.log("Chats encontrados:", chatsEncontrados);

    if (chatsEncontrados && chatsEncontrados.length > 0) {
      router.push(`/chat/${chatsEncontrados[0].id}?itemId=${item.value.id}`);
      return;
    }

    const chatData = {
      participant_1: currentUser.value.id,
      participant_2: item.value.user_id,
      item_id: item.value.id
    };
    console.log("Dados para criação de chat:", chatData);

    const createResponse = await api.post("/chat/chatrooms/", chatData);
    console.log("Resposta da criação de chat:", createResponse.data);

    if (createResponse.data?.id) {
      router.push(`/chat/${createResponse.data.id}?itemId=${item.value.id}`);
    } else {
      throw new Error("Resposta inválida ao criar chatroom");
    }
  } catch (error) {
    console.error("Erro ao criar/aceder chat:", error.response?.data || error.message);
    alertMessage.value = "Erro ao excluir item.";
    submitError.value = true;
  }
};

onMounted(async () => {
  await fetchCurrentUser();
  await fetchItem();
  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
});
</script>
