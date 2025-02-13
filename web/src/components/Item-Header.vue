<template>
  <div
    class="h-[100px] bg-verde shadow-md rounded-b-xl flex items-center text-white p-4 md:p-6"
    :class="{ visible: isVisible, invisible: !isVisible }"
  >
    <!-- Botão de Voltar -->
    <div class="flex items-center w-1/4">
      <img
        @click="goBack"
        src="../assets/icons/arrow-left-white.svg"
        alt="Voltar"
        class="w-[30px] h-[30px] text-white cursor-pointer"
      />
    </div>

    <!-- Título Centralizado -->
    <div class="flex-grow flex justify-center">
      <span class="font-inter font-semibold text-2xl text-center break-words">
        {{ title }}
      </span>
    </div>

    <!-- Logo à Direita -->
    <div class="flex items-center w-1/4 justify-end">
      <router-link to="/about" class="no-underline text-white">
        <Logo class="pr-2 md:pr-4" sizeClass="text-xl md:text-2xl" />
      </router-link>
    </div>
  </div>
</template>

<script>
import Logo from "./Logo.vue";

export default {
  name: "ItemHeader",
  components: {
    Logo,
  },
  data() {
    return {
      isVisible: false,
    };
  },
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  methods: {
    goBack() {
      this.$router.back(); // Retorna para a página anterior
    },
  },
  mounted() {
    setTimeout(() => {
      this.isVisible = true;
    }, 1);
  },
};
</script>

<style scoped>
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
