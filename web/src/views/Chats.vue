<template>
  <div class="fixed w-full top-0 z-[1]">
    <ItemHeader title="Mensagens" />
  </div>

  <div v-if="loadingChats" class="pt-32 space-y-4">
    <div v-for="n in 3" :key="n" class="flex items-center px-4">
      <div class="w-[80px] h-[80px] rounded-full bg-cinza2 animate-pulse"></div>
      <div class="flex-1 px-4 space-y-2">
        <div class="h-6 bg-cinza2 rounded-md animate-pulse"></div>
        <div class="h-4 bg-cinza2 rounded-md animate-pulse"></div>
      </div>
    </div>
  </div>

  <div v-else-if="chatrooms.length" class="pt-32">
    <div
      v-for="chatroom in chatrooms"
      :key="chatroom.id"
      class="flex items-center p-4 border-b border-gray-200 cursor-pointer hover:bg-gray-100 transition"
      @click="openChat(chatroom)"
    >
      <img
        :src="chatroom.recipient.foto"
        alt="Foto do usuário"
        class="w-12 h-12 md:w-16 md:h-16 rounded-full object-cover border-2 border-white"
      />
      <div class="ml-4">
        <p class="text-lg font-semibold">{{ chatroom.recipient.name }}</p>
        <p class="text-gray-500 text-sm">Sobre o item: {{ chatroom.item_name }}</p>
      </div>
    </div>
  </div>

  <div v-else class="flex flex-col items-center justify-center h-96">
    <p class="text-xl text-cinza4">Nenhuma conversa encontrada.</p>
  </div>

  <div class="fixed bottom-0 w-full">
    <MainMenu activeIcon="chat" />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";
import ItemHeader from "../components/Item-Header.vue";
import MainMenu from "../components/Main-Menu.vue";
import defaultAvatar from "@/assets/images/default-avatar.png";

const router = useRouter();
const currentUser = ref({});
const chatrooms = ref([]);
const loadingChats = ref(true);

const openChat = (chatroom) => {
  if (!chatroom.id || !chatroom.recipient?.id || !chatroom.item_id) return;
  router.push({
    path: `/chat/${chatroom.id}`,
    query: { userId: chatroom.recipient.id, itemId: chatroom.item_id },
  });
};

const fetchCurrentUser = async () => {
  try {
    const { data } = await api.get("/auth/user/");
    currentUser.value = data;
  } catch (error) {}
};

const fetchUserChatrooms = async () => {
  if (!currentUser.value?.id) return;

  try {
    const { data } = await api.get("/chat/chatrooms/");
    chatrooms.value = await Promise.all(
      data.results.map(async (chatroom) => {
        const otherUserId =
          chatroom.participant_1 === currentUser.value.id
            ? chatroom.participant_2
            : chatroom.participant_1;

        try {
          const { data: userData } = await api.get(`/users/${otherUserId}/`);
          return {
            ...chatroom,
            recipient: {
              id: otherUserId,
              name: userData.first_name || "Usuário",
              foto: userData.foto ? userData.foto : defaultAvatar,
            },
          };
        } catch {
          return {
            ...chatroom,
            recipient: { id: otherUserId, name: "Usuário", foto: defaultAvatar },
          };
        }
      })
    );
  } catch (error) {
  } finally {
    loadingChats.value = false;
  }
};

onMounted(async () => {
  await fetchCurrentUser();
  await fetchUserChatrooms();
});
</script>

<style scoped>
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
