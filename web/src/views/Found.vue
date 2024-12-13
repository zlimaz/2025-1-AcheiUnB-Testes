<template>
  <div class="h-screen">
    <div class="sticky top-0">
      <Header />
    </div>
    <SubMenu />
    <div
      class="grid grid-cols-[repeat(auto-fit,_minmax(180px,_1fr))] sm:grid-cols-[repeat(auto-fit,_minmax(200px,_1fr))] justify-items-center align-items-center py-6 lg:px-3 gap-y-3"
    >
      <ItemCard :image="imagem1" time="Agora a pouco" />
      <ItemCard :image="imagem2" time="Há uma hora" />
      <ItemCard :image="imagem3" time="Há 2 seg" />
      <ItemCard :image="imagem3" time="Agora a pouco" />
      <ItemCard :image="imagem5" time="Há uma hora" />
      <ItemCard :image="imagem4" time="Agora a pouco" />
      <ItemCard :image="imagem5" time="Agora a pouco" />
      <ItemCard :image="imagem6" time="Há uma hora" />
      <ItemCard :image="imagem4" time="Há 2 seg" />
      <ItemCard :image="imagem5" time="Agora a pouco" />
      <ItemCard :image="imagem6" time="Há uma hora" />
      <ItemCard :image="imagem1" time="Há 2 seg" />
      <ItemCard :image="imagem2" time="Há uma hora" />
      <ItemCard :image="imagem6" time="Há uma hora" />
      <ItemCard :image="imagem1" time="Há uma hora" />
      <ItemCard :image="imagem2" time="Agora a pouco" />
      <ItemCard :image="imagem3" time="Há 2 seg" />
      <ItemCard :image="imagem4" time="Há uma hora" />
    </div>

    <div class="flex pb-20 w-full justify-center gap-x-6">
      <img
        src="../assets/icons/arrow-left.svg"
        alt=""
        class="w-[30px] h-[30px]"
      />
      <img
        src="../assets/icons/arrow-right.svg"
        alt=""
        class="w-[30px] h-[30px]"
      />
    </div>

    <ButtonAdd class="" />
    <div class="fixed bottom-0 w-full">
      <MainMenu activeIcon="search" />
    </div>
  </div>
</template>

<script setup>
import MainMenu from "../components/Main-Menu.vue";
import ItemCard from "../components/Item-Card.vue";
import ButtonAdd from "../components/Button-Add.vue";
import Header from "../components/Header.vue";
import SubMenu from "../components/Sub-Menu.vue";
import imagem1 from "/src/assets/images/carteira.png";
import imagem2 from "/src/assets/images/bone.png";
import imagem3 from "/src/assets/images/caneta.png";
import imagem4 from "/src/assets/images/gloss.png";
import imagem5 from "/src/assets/images/not-available.png";
import imagem6 from "/src/assets/images/sombrinha.png";
</script>

<style scoped></style>
