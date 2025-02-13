<template>
  <div class="fixed w-full top-0 z-[1]">
    <ItemHeader :title="'Mensagens'" />
  </div>

  <!-- Skeleton Loader -->
  <div v-if="loadingChats" class="pt-32 space-y-4">
    <div v-for="n in 3" :key="n" class="flex items-center px-4">
      <div class="w-[80px] h-[80px] rounded-full bg-cinza2 animate-pulse"></div>
      <div class="flex-1 px-4 space-y-2">
        <div class="h-6 bg-cinza2 rounded-md animate-pulse"></div>
        <div class="h-4 bg-cinza2 rounded-md animate-pulse"></div>
      </div>
    </div>
  </div>

  <!-- Chatrooms -->
  <div v-else-if="chatrooms.length" class="pt-32">
    <Chatroom
      v-for="(chatroom, index) in chatrooms"
      :key="chatroom.id"
      :recipient="chatroom.recipient"
      :item="chatroom.item_name"
      :id="chatroom.id"
    />
  </div>

  <!-- Sem chatrooms -->
  <div v-else class="flex flex-col items-center justify-center h-96 mt-10">
    <p class="text-lg text-cinza3">Nenhuma conversa encontrada.</p>
  </div>

  <div class="fixed bottom-0 w-full">
    <MainMenu :activeIcon="'chat'" />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../services/api";
import ItemHeader from "../components/Item-Header.vue";
import MainMenu from "../components/Main-Menu.vue";
import Chatroom from "../components/Chatroom.vue";

const currentUser = ref({});
const chatrooms = ref([]);
const loadingChats = ref(true);

async function fetchCurrentUser() {
  try {
    const response = await api.get(`/auth/user/`);
    currentUser.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar usuário:", error);
  }
}

async function fetchUserChatrooms() {
  try {
    if (currentUser.value) {
      const response = await api.get(`/chat/chatrooms/`);
      let chatroomsTemp = [];

      for (const chatroom of response.data.results) {
        if (chatroom.participant_1 == currentUser.value.id) {
          const userResponse = await api.get(`/users/${chatroom.participant_2}/`);
          chatroom.recipient = {
            name: chatroom.participant_2_username,
            foto: userResponse.data.foto,
          };
          chatroomsTemp.push(chatroom);
        } else if (chatroom.participant_2 == currentUser.value.id) {
          const userResponse = await api.get(`/users/${chatroom.participant_1}/`);
          chatroom.recipient = {
            name: chatroom.participant_1_username,
            foto: userResponse.data.foto,
          };
          chatroomsTemp.push(chatroom);
        }
      }

      chatrooms.value = chatroomsTemp;
    } else {
      console.log("Erro ao encontrar dados do usuário logado");
    }
  } catch (error) {
    console.error("Erro ao buscar conversas:", error);
  } finally {
    loadingChats.value = false; // Finaliza o estado de carregamento
  }
}

onMounted(async () => {
  await fetchCurrentUser();
  await fetchUserChatrooms();
});
</script>

<style scoped>
/* Adiciona uma animação de pulsar para o skeleton loader */
@keyframes pulse {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
  100% {
    opacity: 1;
  }
}

.animate-pulse {
  animation: pulse 1.5s infinite;
}
</style>
