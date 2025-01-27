<template>
    <div class="h-[100px] bg-verde shadow-md rounded-b-xl flex items-center justify-start text-white gap-x-9 p-6">
        <router-link to="/user" class="inline-block">
            <img src="../assets/icons/arrow-left-white.svg" alt="Voltar" class="w-[30px] h-[30px] text-white" />
        </router-link>
    </div>

    <div class="pb-8">
        <SubMenu />
    </div>

    <div class="grid grid-cols-[repeat(auto-fit,_minmax(180px,_1fr))] sm:grid-cols-[repeat(auto-fit,_minmax(200px,_1fr))] justify-items-center align-items-center lg:px-3 gap-y-3 pb-10">
        <ItemCard
            v-for="item in myItemsFound"
            :key="item.id"
            :id="item.id"
            :name="item.name"
            :location="item.location_name"
            :time="formatTime(item.created_at)"
            :image="item.image_urls[0] || NotAvailableImage"
            :isMyItem="true" 
            @delete="handleDelete"
        />
    </div>

    <ButtonAdd />
    <div class="fixed bottom-0 w-full">
        <MainMenu activeIcon="search" />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { fetchMyItemsFound, deleteItem } from '@/services/apiItems';
import { formatTime } from '@/utils/dateUtils';
import MainMenu from "../components/Main-Menu.vue";
import SubMenu from "../components/Sub-Menu-UserFound.vue";
import ItemCard from '@/components/Item-Card.vue';
import NotAvailableImage from '@/assets/images/not-available.png';

const myItemsFound = ref([]);


const fetchItems = async () => {
    const response = await fetchMyItemsFound();
    myItemsFound.value = response;
};


const handleDelete = async (itemId) => {
    try {
        await deleteItem(itemId); // Chama o serviço para deletar o item no backend
        myItemsFound.value = myItemsFound.value.filter(item => item.id !== itemId); // Atualiza a lista removendo o item excluído
    } catch (error) {
        console.error('Erro ao deletar o item:', error);
    }
};


onMounted(() => fetchItems());
</script>

<style scoped></style>
