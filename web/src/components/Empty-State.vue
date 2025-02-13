<template>
    <div class="flex flex-col items-center justify-center h-64 text-center">
        <img :src="box" class="w-40 h-40 mb-4" />
        <p class="text-cinza3 font-inter text-lg">
            Parece que o <span class="text-azul font-bold">AcheiUnB</span> {{ computedMessage }}
        </p>
    </div>
</template>

<script setup>
import { computed } from "vue";
import { filtersState } from "@/store/filters"; // Importação corrigida sem Pinia
import box from "@/assets/icons/found-and-lost-box.jpg";

// Definição das propriedades recebidas
const props = defineProps({
    type: {
        type: String,
        required: true, // Obrigatório ("achado" ou "perdido")
    },
});

// Computed Property para modificar a mensagem dinamicamente
const computedMessage = computed(() => {
    // Define a palavra correta com base no tipo de item
    const itemType = props.type === "achado" ? "achado" : "perdido";

    // Verifica os filtros e retorna a mensagem correspondente
    if (filtersState.searchQuery.value) {
        return `não encontrou resultados para "${filtersState.searchQuery.value}" nos itens ${itemType}s.`;
    }
    if (filtersState.activeCategory.value) {
        return `não encontrou itens ${itemType}s da categoria "${filtersState.activeCategory.value}".`;
    }
    if (filtersState.activeLocation.value) {
        return `não encontrou itens ${itemType}s no local "${filtersState.activeLocation.value}".`;
    }

    return `está sem itens ${itemType}s... Você pode adicionar um!`;
});
</script>
