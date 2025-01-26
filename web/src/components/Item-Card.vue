<template>
  <div
    class="w-[170px] sm:w-[190px] h-[230px] bg-cinza1 rounded-sm shadow-complete p-2 flex flex-col"
    @click="viewItemDetails()"
  >
    <!--imagem-->
    <div
      class="w-full h-[120px] bg-cinza2 rounded-sm flex justify-center items-start"
    >
      <img :src="image" class="rounded-sm w-full h-full object-cover" />
    </div>

    <!--linha-->
    <div class="h-[2px] w-1/4 bg-laranja mt-4"></div>

    <!--textos-->
    <div class="text-azul font-bold font-inter mt-1">{{ name }}</div>
    <div class="flex items-start">
      <img
        src="../assets/icons/locale.svg"
        alt=""
        class="w-[15px] h-[15px] mr-1"
      />
      <div class="text-azul font-inter text-sm">{{ location }}</div>
    </div>
    <span class="text-right font-inter font-bold text-xs text-cinza3 p-1">{{
      time
    }}</span>
  </div>
</template>

<script>
export default {
  name: "ItemCard",
  props: {
    id: Number,
    image: String,
    name: String,
    time: String,
    location: String,
  },
  methods: {
    viewItemDetails() {
      this.$router.push({ name: "ListItem", query: { idItem: this.id } });
    },
  },
};
</script>

<style scoped></style>
