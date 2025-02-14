<template>
  <div
    class="h-[100px] bg-verde shadow-md rounded-b-xl flex items-center justify-center text-white p-6"
    :class="{ visible: isVisible, invisible: !isVisible }"
  >
    <div>
      <span class="font-inter font-semibold text-2xl">
        {{ text ? text : "Sobre o projeto" }}
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutHeader",
  props: {
    text: String,
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
