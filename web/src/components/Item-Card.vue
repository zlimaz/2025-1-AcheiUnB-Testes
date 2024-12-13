<template>
  <div
    class="w-[170px] h-[220px] bg-cinza1 rounded-sm shadow-complete p-2 flex flex-col"
  >
    <!--imagem-->
    <div
      class="w-full h-[120px] bg-cinza2 rounded-sm flex justify-center items-start"
    >
      <img :src="image" class="rounded-sm w-full h-full object-cover" />
    </div>

    <!--linha-->
    <div class="h-[2px] w-1/4 bg-laranja mt-3"></div>

    <div class="text-azul font-bold font-inter my-1">Carteira</div>
    <img src="../assets/icons/locale.svg" alt="" class="w-[15px] h-[15px]" />
  </div>
</template>

<script>
export default {
  name: "ItemCard",
  props: {
    image: String,
  },
};
</script>

<style scoped></style>
