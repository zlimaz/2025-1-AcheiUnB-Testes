<template>
  <div
    class="flex items-center justify-between px-10 my-4 cursor-pointer hover:bg-cinza1 py-2"
    @click="enterChatroom"
  >
    <div class="flex" v-if="id">
      <div
        class="w-[60px] h-[60px] sm:w-[80px] sm:h-[80px] rounded-full bg-cinza3 flex items-center justify-center"
      >
        <div v-if="recipient.foto">
          <img :src="recipient.foto" alt="" />
        </div>
        <div v-else>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="white"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="#FFFFFF"
            class="w-8 h-8"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"
            />
          </svg>
        </div>
      </div>
      <div class="px-6">
        <div class="text-lg sm:text-xl text-azul font-bold font-inter my-1">
          {{ recipient.name }}
        </div>
        <div class="text-sm sm:text-md text-cinza3">Sobre o item: {{ item }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const props = defineProps({
  id: Number,
  recipient: {
    type: Object,
    default: () => ({ name: "", foto: "" }),
  },
  item: String,
});

function enterChatroom() {
  router.push({ name: "Chat", params: { chatroomId: props.id } });
}
</script>

<style scoped></style>
