<template>
    <div class="min-h-screen">
        <div class="fixed w-full top-0">
            <HeaderMyItems/>
        </div>

        <div class="grid grid-cols-[repeat(auto-fit,_minmax(180px,_1fr))] sm:grid-cols-[repeat(auto-fit,_minmax(200px,_1fr))] justify-items-center align-items-center lg:px-3 gap-y-3 pb-10"
            >
            <ItemCard
                v-for="item in myItemsFound"
                :key="item.id"
                :name="item.name"
                :location="item.location_name"
                :time="formatTime(item.created_at)"
                :image="item.image_urls[0] || NotAvailableImage"
            />
        </div>

        <div class="fixed bottom-0 w-full">
            <MainMenu/>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import HeaderMyItems from '@/components/Header-MyItems.vue';
import MainMenu from '@/components/Main-Menu.vue';
import { fetchMyItemsFound } from '@/services/apiItems';

const myItemsFound = ref([]);

const fetchItems = async () => {
    const response = await fetchMyItemsFound();
    myItemsFound.value = response.results;
}


onMounted(() => fetchItems());
</script>


<style></style>