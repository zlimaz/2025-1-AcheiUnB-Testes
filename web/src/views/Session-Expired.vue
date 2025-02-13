<template>
  <div id="main-content" class="telaInteira bg-verde text-white p-4 min-h-screen">
    <div class="titulo flex space-x-1 mt-20 mb-16 ml-8 md:ml-0 md:flex md:justify-center md:mb-24">
      <Logo />
    </div>
    <div
      class="flex flex-col slogan max-w-72 ml-8 md:mr-8 md:max-w-none md:w-auto md:text-center mt-32"
    >
      <p class="text-5xl font-bold md:text-3xl">Sua sessão expirou.</p>
    </div>
    <div class="flex justify-center">
      <router-link
        to="/"
        class="inline-flex items-center rounded-full bg-gray-50 px-10 mt-8 py-3 md:px-24 md:py-4 text-azul ring-1 ring-inset ring-gray-500/10 font-bold font-inter text-lg md:text-xl no-underline w-auto"
      >
        Fazer login novamente
      </router-link>
    </div>
  </div>
</template>

<script setup>
import Logo from "../components/Logo.vue";
</script>
