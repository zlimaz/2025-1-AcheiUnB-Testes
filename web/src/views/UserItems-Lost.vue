<template>
    <div class="h-[100px] bg-verde shadow-md rounded-b-xl flex items-center justify-start text-white gap-x-9 p-6">
        <router-link to="/user" class="inline-block">
            <img src="../assets/icons/arrow-left-white.svg" alt="Voltar" class="w-[30px] h-[30px] text-white" />
        </router-link>
    </div>
    <div class="pb-8">
        <SubMenu />
    </div>
    <ButtonAdd />
    <div class="fixed bottom-0 w-full">
        <MainMenu activeIcon="search" />
    </div>
</template>

<script setup>
import MainMenu from "../components/Main-Menu.vue";
import SubMenu from "../components/Sub-Menu-UserLost.vue";
</script>

<style scoped></style>