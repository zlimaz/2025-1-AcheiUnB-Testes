<template>
    <div class="flex flex-col items-center justify-center h-64 text-center">
        <img :src="box" class="w-40 h-40 mb-4" />
        <p class="text-cinza3 font-inter text-lg">
            Parece que você não tem itens {{ message }} <span class="text-azul font-bold">{{ highlightText }}</span>
        </p>
    </div>
</template>

<script setup>
import box from "@/assets/icons/found-and-lost-box.jpg";

defineProps({
    message: String,
    highlightText: String
});
</script>