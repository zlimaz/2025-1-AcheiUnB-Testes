<template>
  <div class="relative min-h-screen">
    <div 
      class="absolute inset-0 bg-no-repeat bg-cover bg-center opacity-10 z-[-1]"
      :style="{ 
        backgroundImage: `url(${backgroundImage})`, 
        backgroundSize: isLargeScreen ? '50%' : 'contain', 
        backgroundAttachment: 'fixed' 
      }"
    ></div>
    <div class="fixed w-full top-0" style="z-index: 1">
      <AboutHeader />
    </div>
    <div class="pt-[120px] flex justify-center my-6 text-azul">
      <Logo />
    </div>
    <span
      class="font-inter text-azul text-center
       flex justify-center items-center mx-auto max-w-3xl sm:px-0 px-4 md:max-w-2xl mt-7"
    >
      Somos um grupo da disciplina Métodos de Desenvolvimento de Software da Universidade de
      Brasília.<br />
      Temos como objetivo solucionar um dos problemas da faculdade, que é a falta de ferramentas para
      organizar itens achados e perdidos pelos estudantes.<br /> Com o AcheiUnB você consegue de forma simples e intuitiva procurar pelo seu item perdido ou
      cadastrar um item que você encontrou.
    </span>
    
    <div class="flex justify-center mt-6">
      <a
        href="https://unb-mds.github.io/2024-2-AcheiUnB/CONTRIBUTING/"
        target="_blank"
        class="bg-laranja text-white font-semibold px-6 py-2 rounded-full hover:bg-azulEscuro transition hover:text-white duration-300 shadow-md rounded-full hover:scale-110 transition-transform"
      >
        Como Contribuir?
      </a>
    </div>

    <div class="max-w-4xl mx-auto mt-10 p-5 pb-[140px]">
      <div class="text-azul text-lg text-center font-semibold mb-7">Criado por:</div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="creator in creators" :key="creator.name" class="flex flex-col items-center">
          <a :href="creator.github" target="_blank">
            <img
              :src="creator.image"
              :alt="creator.name"
              class="w-[100px] rounded-full hover:scale-110 transition-transform"
            />
          </a>
          <div class="text-center mt-2">
            <p class="font-inter font-medium">{{ creator.name }}</p>
            <p class="text-sm text-cinza3">Engenharia de Software</p>
          </div>
        </div>
      </div>
    </div>

    <ButtonAdd />
    <div class="fixed bottom-0 w-full">
      <MainMenu activeIcon="info" />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import AboutHeader from "../components/Header-About.vue";
import MainMenu from "../components/Main-Menu.vue";
import Logo from "../components/Logo.vue";
import backgroundImagePath from "@/assets/icons/Favicon.png";

const backgroundImage = ref(backgroundImagePath);

const creators = [
  {
    name: "Ana Elisa Ramos",
    github: "https://github.com/anaelisaramos",
    image: "https://github.com/anaelisaramos.png"
  },
  {
    name: "Davi Camilo",
    github: "https://github.com/DaviCamilo23",
    image: "https://github.com/DaviCamilo23.png"
  },
  {
    name: "Euller Júlio da Silva",
    github: "https://github.com/potatoyz908",
    image: "https://github.com/potatoyz908.png"
  },
  {
    name: "Leonardo Ramiro",
    github: "https://github.com/leoramiroo",
    image: "https://github.com/leoramiroo.png"
  },
  {
    name: "Pedro Everton",
    github: "https://github.com/pedroeverton217",
    image: "https://github.com/pedroeverton217.png"
  },
  {
    name: "Pedro Martins Silva",
    github: "https://github.com/314dro",
    image: "https://github.com/314dro.png"
  },
  {
    name: "Tiago Balieiro",
    github: "https://github.com/TiagoBalieiro",
    image: "https://github.com/TiagoBalieiro.png"
  }
];
</script>

<style scoped></style>
