<template>
  <div class="relative flex flex-col h-screen bg-gray-100">

    <div class="flex absolute inset-0 justify-center items-center pointer-events-none z-0">
      <img
        src="@/assets/icons/Favicon.png"
        alt="Watermark"
        class="w-48 md:w-64 lg:w-80 opacity-20"
      />
    </div>

    <HeaderMessage
      v-if="receiverId && itemId"
      :itemId="String(itemId)" 
      :userId="String(receiverId)"
      class="fixed top-0 left-0 w-full z-20"
    />

    <div ref="messagesContainer" class="relative flex-1 pt-32 pb-24 px-4 overflow-y-auto z-10">
      <div v-for="message in messages" :key="message.id" class="mb-2 flex">
        
        <div v-if="message.sender === currentUser?.id" class="flex w-full justify-end">
          <div class="bg-laranja text-white p-3 rounded-2xl max-w-[70%] break-words shadow-md">
            <p class="text-sm">{{ message.content }}</p>
            <span class="text-xs opacity-75 mt-1 block text-right">
              {{ formatTime(message.timestamp) }}
            </span>
          </div>
        </div>

        <div v-else class="flex w-full justify-start">
          <div class="bg-gray-300 text-gray-800 p-3 rounded-2xl max-w-[70%] break-words shadow-md">
            <p class="text-sm">{{ message.content }}</p>
            <span class="text-xs opacity-75 mt-1 block text-left">
              {{ formatTime(message.timestamp) }}
            </span>
          </div>
        </div>

      </div>
    </div>
    
    <div class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 p-4 z-20">
      <div class="flex">
        <input
          v-model="messageContent"
          @keyup.enter="sendMessage"
          type="text"
          maxlength="80"
          placeholder="Digite uma mensagem (máx. 80 caracteres)..."
          class="flex-1 border border-gray-300 rounded-full px-4 py-2 focus:outline-none focus:border-laranja"
        />
        <button
          @click="sendMessage"
          :disabled="!messageContent.trim()"
          class="ml-2 bg-laranja text-white px-4 py-2 rounded-full hover:bg-laranja-dark disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          Enviar
        </button>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../services/api";
import HeaderMessage from "@/components/Header-Message.vue";

const route = useRoute();
const messages = ref([]);
const messageContent = ref("");
const currentUser = ref(null);
const item = ref(null);
const receiverId = ref(null);

const chatroomId = ref(route.params.chatroomId || route.query.chatroomId);
const itemId = ref(route.params.itemId || route.query.itemId);

if (!chatroomId.value) {
  console.error("ID do chat não encontrado na rota");
} else {
  console.log("chatroomId:", chatroomId.value);
}

const sendMessage = async () => {
  if (!chatroomId.value) {
    console.error("ID do chat não encontrado, não é possível enviar mensagem");
    return;
  }
  if (!messageContent.value.trim()) {
    console.warn("Mensagem vazia, nada a enviar");
    return;
  }
  try {
    console.log("Enviando mensagem para room:", chatroomId.value, "Conteúdo:", messageContent.value);
    // Chama a API para enviar a mensagem
    await api.post("/chat/messages/", {
      room: chatroomId.value,
      content: messageContent.value
    });
    messageContent.value = "";
    await fetchMessages();
  } catch (error) {
    console.error("Erro ao enviar mensagem:", error.response?.data || error.message);
  }
};

const fetchMessages = async () => {
  if (!chatroomId.value) return;
  try {
    const response = await api.get("/chat/messages/", {
      params: { room: chatroomId.value }
    });
    messages.value = response.data.results || response.data;
  } catch (error) {
    console.error("Erro ao buscar mensagens:", error);
  }
};

const fetchCurrentUser = async () => {
  try {
    const response = await api.get("/auth/user/");
    currentUser.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar usuário:", error);
  }
};

const fetchItem = async () => {
  if (!itemId.value) return;
  try {
    const response = await api.get(`/items/${itemId.value}`);
    item.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar item:", error);
  }
};

const fetchReceiverId = async () => {
  if (!itemId.value) return;
  try {
    const response = await api.get(`/items/${itemId.value}`);
    receiverId.value = response.data.user_id;
  } catch (error) {
    console.error("Erro ao buscar dono do item:", error);
  }
};

const formatTime = (timestamp) => {
  return new Date(timestamp).toLocaleTimeString("pt-BR", {
    hour: "2-digit",
    minute: "2-digit"
  });
};

const fetchChatroomData = async () => {
  if (!chatroomId.value) return;
  try {
    await api.get(`/chat/chatrooms/${chatroomId.value}/`);
    // Se necessário, processar os dados do chatroom aqui.
  } catch (error) {
    console.error("Erro ao buscar dados do chatroom:", error);
  }
};


onMounted(async () => {
  await fetchCurrentUser();
  await fetchItem();
  await fetchReceiverId();
  await fetchChatroomData();
  await fetchMessages();
});
</script>

<style scoped></style>