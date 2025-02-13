<template>
  <router-link to="/register-found">
    <button
      class="fixed right-0 bottom-28 rounded-l-lg w-60 h-12 cursor-pointer flex items-center border border-laranja bg-laranja group hover:bg-laranja active:bg-laranja active:border-laranja"
      :class="{ visible: isVisible, invisible: !isVisible }"
    >
      <span class="text-azul font-inter font-medium ml-6 transform group-hover:translate-x-0"
        >Adicionar item achado</span
      >
      <span
        class="absolute right-0 h-full w-10 rounded-lg bg-laranja flex items-center justify-center transform group-hover:translate-x-0 group-hover:w-full transition-all duration-300"
      >
        <img src="../assets/icons/add-item.svg" alt="" />
      </span>
    </button>
  </router-link>
</template>

<script>
export default {
  props: {
    customClass: {
      name: "ButtonAdd",
      type: String,
    },
  },
  data() {
    return {
      isVisible: false,
    };
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
  transform: translateX(0);
  transition:
    opacity 0.5s ease-in-out,
    transform 0.5s ease-in-out;
}

.invisible {
  opacity: 0;
  transform: translateX(70px);
}
</style>
