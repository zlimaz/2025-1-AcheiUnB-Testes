<template>
  <div class="fixed top-0 left-0 w-full bg-verde shadow-md py-3 px-4 flex items-center z-10">
    
    <!-- Botão de Voltar -->
    <img 
      @click="goBack"
      :src="LeftArrow"
      alt="Voltar"
      class="w-6 h-6 md:w-8 md:h-8 cursor-pointer"
    />
    
    <!-- Container do usuário e item com espaçamento adequado -->
    <div class="flex items-center space-x-4 ml-2">
      <!-- Foto do Usuário -->
      <img
        :src="userImage || defaultAvatar"
        alt="Foto do usuário"
        class="w-8 h-8 md:w-10 md:h-10 rounded-full object-cover border-2 border-white"
      />

      <!-- Nome do Usuário -->
      <span class="text-white font-semibold text-sm md:text-base truncate max-w-[120px] md:max-w-[200px]">
        {{ userName || "Usuário" }}
      </span>

      <!-- Imagem do Item -->
      <img
        :src="itemImage || notAvailableImage"
        alt="Imagem do item"
        class="w-8 h-8 md:w-10 md:h-10 rounded-lg object-cover border-2 border-white"
      />
    </div>

    <!-- Logo: alinhada à direita em telas menores, centralizada em telas maiores -->
    <div class="ml-auto md:absolute md:left-1/2 md:transform md:-translate-x-1/2">
      <router-link to="/about" class="no-underline text-white">
        <Logo class="pr-4" sizeClass="text-2xl" />
      </router-link>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";
import Logo from "./Logo.vue"; // Importa a logo branca do projeto
import defaultAvatar from "@/assets/images/default-avatar.png";
import notAvailableImage from "@/assets/images/not-available.png";
import LeftArrow from "@/assets/icons/arrow-left-white.svg";

const props = defineProps({
  userId: {
    type: String,
    required: true,
  },
  itemId: {
    type: String,
    required: true,
  },
});

const router = useRouter();
const userName = ref("");
const userImage = ref(null);
const itemImage = ref(null);

const fetchUserData = async () => {
  if (!props.userId) return;
  try {
    const response = await api.get(`/users/${props.userId}/`);
    userName.value = response.data.first_name || "Usuário";
    userImage.value = response.data.foto;
  } catch (error) {
    console.error("Erro ao buscar dados do usuário:", error);
  }
};

const fetchItemData = async () => {
  if (!props.itemId) return;
  try {
    const response = await api.get(`/items/${props.itemId}`);
    itemImage.value = response.data.image_urls?.[0] || notAvailableImage;
  } catch (error) {
    console.error("Erro ao buscar dados do item:", error);
  }
};

const goBack = () => {
  router.back();
};

onMounted(async () => {
  await fetchUserData();
  await fetchItemData();
});
</script>
