<template>
  <div class="fixed top-0 left-0 w-full bg-verde shadow-md py-3 px-4 flex items-center z-10">
    
    <!-- Seção Esquerda: Botão de Voltar, Dados do Usuário e Item -->
    <div class="flex items-center space-x-2 min-w-[180px] md:min-w-[260px]">
      <!-- Botão de Voltar -->
      <img 
        @click="goBack"
        :src="LeftArrow"
        alt="Voltar"
        class="w-6 h-6 md:w-8 md:h-8 cursor-pointer"
      />
      
      <!-- Foto do Usuário -->
      <img
        :src="userImage || defaultAvatar"
        alt="Foto do usuário"
        class="w-9 h-9 md:w-10 md:h-10 rounded-full object-cover border-2 border-white"
      />

      <!-- Nome do Usuário -->
      <span class="text-white font-semibold text-xs md:text-sm truncate max-w-[90px] md:max-w-[160px]">
        {{ userName || "Usuário" }}
      </span>

      <!-- Imagem do Item -->
      <img
        :src="itemImage || notAvailableImage"
        alt="Imagem do item"
        class="w-9 h-9 md:w-12 md:h-12 rounded-lg object-cover border-2 border-white"
      />
    </div>

    <div class="absolute left-1/2 transform -translate-x-1/2 top-2 md:top-3 lg:top-4 flex justify-center pointer-events-auto">
      <router-link to="/about">
        <Logo class="text-white w-2 h-1 sm:w-6 sm:h-2.5 md:w-4 md:h-1.5 lg:w-8 lg:h-3.5" />
      </router-link>
    </div>
  </div>*/
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";
//import Logo from "./Logo.vue";
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
