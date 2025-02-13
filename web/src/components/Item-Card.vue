<template>
  <div
    class="w-[170px] sm:w-[190px] h-[230px] bg-cinza1 rounded-sm shadow-complete p-2 flex flex-col relative z-0"
    @click="viewItemDetails()"
  >
    <!--imagem-->
    <div class="w-full h-[120px] bg-cinza2 rounded-sm flex justify-center items-start">
      <img :src="image" class="rounded-sm w-full h-full max-w-full max-h-full object-cover" />
    </div>

    <!-- Botão de excluir no canto inferior direito -->
    <button
      v-if="isMyItem"
      class="absolute p-1 bottom-2 border-2 border-laranja right-2 w-7 h-7 bg-white flex items-center justify-center text-xs rounded-full cursor-pointer"
      @click.stop="showConfirmModal = true"
    >
      <img src="../assets/icons/trash.svg" alt="Excluir" />
    </button>

  <!-- Modal de Confirmação de Exclusão -->
    <Teleport to="body"> <!-- Garante que o modal será renderizado fora do ItemCard -->
      <div 
        v-if="showConfirmModal" 
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div 
          class="bg-azul p-6 rounded-lg shadow-lg w-full max-w-sm sm:max-w-md lg:max-w-lg text-center relative"
          @click.stop
        >
          <p class="text-white font-inter text-lg">
            Você realmente deseja excluir este item do AcheiUnB?
          </p>

          <div class="flex flex-col sm:flex-row justify-center mt-4 gap-4">
            <button 
              class="bg-red-500 text-white font-inter px-4 py-2 rounded-md hover:bg-red-600 transition w-full sm:w-auto"
              @click="confirmDelete"
            >
              Excluir
            </button>
            <button 
              class="bg-white font-inter px-4 py-2 rounded-md hover:bg-gray-200 transition w-full sm:w-auto"
              @click="closeModal"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </Teleport>

    <!--linha-->
    <div class="h-[2px] w-1/4 bg-laranja mt-4"></div>

    <!--textos-->
    <div class="text-azul font-bold font-inter mt-1 truncate">{{ name }}</div>
    <div class="flex items-start">
      <img src="../assets/icons/locale.svg" alt="" class="w-[15px] h-[15px] mr-1" />
      <div class="text-azul font-inter text-sm">{{ location }}</div>
    </div>

    <!-- Exibe o tempo se não for um item do usuário -->
    <span
      class="text-right font-inter font-bold text-xs text-cinza3 p-1 flex justify-end items-center"
    >
      <template v-if="!isMyItem">
        {{ time }}
      </template>
    </span>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRouter } from "vue-router";

const props = defineProps({
  id: Number,
  image: String,
  name: String,
  time: String,
  location: String,
  isMyItem: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["delete"]);
const router = useRouter();
const showConfirmModal = ref(false);
const selectedItemId = ref(null);

const viewItemDetails = () => {
  if (!showConfirmModal.value) {
    router.push({ name: "ListItem", query: { idItem: props.id } });
  }
};

const openModal = (id) => {
  selectedItemId.value = id;
  showConfirmModal.value = true;

  // Bloqueia a rolagem da página quando o modal está aberto
  document.body.style.overflow = "hidden";
};

const closeModal = () => {
  showConfirmModal.value = false;
  selectedItemId.value = null;

  // Libera a rolagem da página ao fechar o modal
  document.body.style.overflow = "";
};

const confirmDelete = () => {
  emit("delete", props.id);
  showConfirmModal.value = false;
};
</script>

<style scoped></style>
