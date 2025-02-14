<template>
  <div
    class="fixed top-0 left-0 w-full bg-verde shadow-md py-3 px-4 flex items-center z-10"
    :class="{ visible: isVisible, invisible: !isVisible }"
  >
    <!-- Botão de Voltar -->
    <img
      @click="goBack"
      :src="LeftArrow"
      alt="Voltar"
      class="w-[35px] h-35[px] md:w-8 md:h-8 cursor-pointer transform transition duration-300 hover:scale-125"
    />

    <div class="flex items-center space-x-4 ml-2">
      <img
        :src="userImage"
        alt="Foto do usuário"
        class="w-10 h-10 md:w-12 md:h-12 rounded-full object-cover border-2 border-white"
      />

      <!-- Nome do Usuário -->
      <span
        class="text-white font-semibold text-sm md:text-base truncate max-w-[120px] md:max-w-[200px]"
      >
        {{ userName || "Usuário" }}
      </span>
      <img
        :src="itemImage"
        alt="Imagem do item"
        class="w-10 h-10 md:w-12 md:h-12 rounded-lg object-cover border-2 border-white"
      />
    </div>

    <div class="ml-auto md:absolute md:left-1/2 md:transform md:-translate-x-1/2">
      <router-link to="/about" class="no-underline text-white">
        <Logo class="pr-4" sizeClass="text-2xl" />
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watchEffect } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "../services/api";
import Logo from "./Logo.vue";
import defaultAvatar from "@/assets/images/default-avatar.png";
import notAvailableImage from "@/assets/images/not-available.png";
import LeftArrow from "@/assets/icons/arrow-left-white.svg";

const route = useRoute();
const router = useRouter();
const chatroomId = ref(route.params.chatroomId || route.query.chatroomId);
const userName = ref("Usuário");
const userImage = ref(defaultAvatar);
const itemImage = ref(notAvailableImage);
const userId = ref(null);
const itemId = ref(null);
const currentUser = ref(null);

const fetchCurrentUser = async () => {
  try {
    const response = await api.get(`/auth/user/`);
    currentUser.value = response.data;
  } catch {}
};

const fetchChatroomData = async () => {
  if (!chatroomId.value || !currentUser.value?.id) return;

  try {
    const response = await api.get(`/chat/chatrooms/${chatroomId.value}/`);
    const chatroom = response.data;

    userId.value =
      chatroom.participant_1 === currentUser.value.id
        ? chatroom.participant_2
        : chatroom.participant_1;

    itemId.value = chatroom.item_id;

    fetchUserData();
    fetchItemData();
  } catch {}
};
const isVisible = ref(false);

const fetchUserData = async () => {
  if (!userId.value) return;
  try {
    const response = await api.get(`/users/${userId.value}/`);
    userName.value = response.data.first_name || "Usuário";
    userImage.value = response.data.foto || defaultAvatar;
  } catch {}
};

const fetchItemData = async () => {
  if (!itemId.value) return;
  try {
    const response = await api.get(`/items/${itemId.value}`);
    itemImage.value = response.data.image_urls?.[0] || notAvailableImage;
  } catch {}
};

const goBack = () => {
  router.back();
};

watchEffect(() => {
  if (!currentUser.value) {
    fetchCurrentUser();
  } else {
    fetchChatroomData();
  }
});

onMounted(() => {
  fetchCurrentUser();

  setTimeout(() => {
    isVisible.value = true;
  }, 1);
});
</script>

<style>
.visible {
  opacity: 1;
  transform: translateY(0);

  transition:
    opacity 0.3s ease-in-out,
    transform 0.3s ease-in-out;
}

.invisible {
  opacity: 0;
  transform: translateY(-45px);
}
</style>
