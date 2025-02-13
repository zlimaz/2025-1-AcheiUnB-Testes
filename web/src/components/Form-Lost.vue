<template>
  <form id="app" @submit="save">
    <div class="grid md:grid-cols-4 gap-4">
      <!-- Nome do item -->
      <div class="mb-4 col-span-2">
        <label for="name" class="font-inter block text-azul text-sm font-bold mb-2"
          >Item <span class="text-red-500">*</span></label
        >
        <input
          id="name"
          class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          v-model="item.name"
          type="text"
          name="name"
          placeholder="Escreva o nome do item"
        />
      </div>

      <!-- Categoria -->
      <div class="block relative mb-4 col-span-2">
        <label for="category" class="font-inter block text-azul text-sm font-bold mb-2"
          >Categoria <span class="text-red-500">*</span></label
        >
        <select
          id="category"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="item.category === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="item.category"
          @change="handleSelectChange"
          name="category"
        >
          <option disabled value="">Selecione</option>
          <option value="clear">Limpar seleção</option>
          <option
            v-for="category of categories"
            :key="category.id"
            :value="category.id"
            class="block text-gray-700"
          >
            {{ category.name }}
          </option>
        </select>
        <div
          class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6"
        >
          <img
            src="../assets/icons/chevron-down.svg"
            alt="chevron-down"
            class="w-[15px] h-[15px]"
          />
        </div>
      </div>

      <!-- Location -->
      <div class="block relative mb-4 col-span-2">
        <label for="location" class="font-inter block text-azul text-sm font-bold mb-2"
          >Local <span class="text-red-500">*</span></label
        >
        <select
          id="location"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="item.location === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="item.location"
          @change="handleSelectChange"
          name="location"
        >
          <option value="" disabled selected>Selecione</option>
          <option value="clear">Limpar seleção</option>
          <option
            v-for="location of locations"
            :key="location.id"
            :value="location.id"
            class="block text-gray-700"
          >
            {{ location.name }}
          </option>
        </select>
        <div
          class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6"
        >
          <img
            src="../assets/icons/chevron-down.svg"
            alt="chevron-down"
            class="w-[15px] h-[15px]"
          />
        </div>
      </div>

      <!-- Color -->
      <div class="block relative mb-4 col-span-2">
        <label for="color" class="font-inter block text-azul text-sm font-bold mb-2">Cor</label>
        <select
          id="color"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="item.color === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="item.color"
          @change="handleSelectChange"
          name="color"
        >
          <option value="" disabled selected>Selecione</option>
          <option value="clear">Limpar seleção</option>
          <option
            v-for="color of colors"
            :key="color.id"
            :value="color.id"
            class="block text-gray-700"
          >
            {{ color.name }}
          </option>
        </select>
        <div
          class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6"
        >
          <img
            src="../assets/icons/chevron-down.svg"
            alt="chevron-down"
            class="w-[15px] h-[15px] fill-current text-white"
          />
        </div>
      </div>

      <!-- Brand -->
      <div class="block relative mb-4 col-span-2">
        <label for="color" class="font-inter block text-azul text-sm font-bold mb-2">Marca</label>
        <select
          id="brand"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="item.brand === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="item.brand"
          @change="handleSelectChange"
          name="color"
        >
          <option value="" disabled selected>Selecione</option>
          <option value="clear">Limpar seleção</option>
          <option
            v-for="brand of brands"
            :key="brand.id"
            :value="brand.id"
            class="block text-gray-700"
          >
            {{ brand.name }}
          </option>
        </select>
        <div
          class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6"
        >
          <img
            src="../assets/icons/chevron-down.svg"
            alt="chevron-down"
            class="w-[15px] h-[15px] fill-current text-white"
          />
        </div>
      </div>

      <!-- Data -->
      <div class="mb-4 col-span-2">
        <label for="lostDate" class="font-inter block text-azul text-sm font-bold mb-2"
          >Data em que foi perdido</label
        >
        <input
          id="lostDate"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="item.lostDate === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="item.lostDate"
          type="date"
          name="lostDate"
        />
      </div>

      <!-- Horário -->
      <div class="mb-4 col-span-2">
        <label for="lostTime" class="font-inter block text-azul text-sm font-bold mb-2"
          >Horário em que foi perdido</label
        >
        <input
          id="lostTime"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="lostTime === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="lostTime"
          type="time"
          name="lostTime"
        />
      </div>

      <!-- Descrição -->
      <div class="mb-4 col-span-2">
        <label for="description" class="font-inter block text-azul text-sm font-bold mb-2">
          Descrição
        </label>
        <textarea
          id="description"
          v-model="item.description"
          name="description"
          rows="4"
          placeholder="Descreva detalhadamente o item"
          class="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        ></textarea>
      </div>

      <div>
        <!-- Upload de arquivo -->
        <label
          for="images"
          class="flex bg-azul text-white text-base px-5 py-3 outline-none rounded cursor-pointer font-inter"
          :class="previews?.length > 1 ? 'opacity-50 cursor-not-allowed' : ''"
        >
          <img src="../assets/icons/add-item-white.svg" alt="" class="mr-2" />
          Adicionar imagens
          <input
            type="file"
            id="images"
            class="hidden"
            @change="onFileChange"
            :disabled="previews?.length > 1"
          />
        </label>
      </div>

      <div class="flex flex-wrap gap-4 col-span-3">
        <!-- Loop de Imagens -->
        <div
          v-for="(image, index) in previews"
          :key="index"
          class="w-64 h-64 border rounded relative"
        >
          <!-- Imagem de Pré-visualização -->
          <img :src="image" alt="Preview" class="w-full h-full object-cover rounded" />

          <!-- Botão Remover -->
          <div
            class="absolute p-1 bottom-2 border-2 border-laranja right-2 w-12 h-12 bg-white flex items-center justify-center text-xs rounded-full cursor-pointer"
            @click="removeImage(index)"
          >
            <img src="../assets/icons/trash.svg" alt="" />
          </div>
        </div>
      </div>

      <!-- Enviar -->
      <div class="col-span-4">
        <button
          type="button"
          @click="save"
          class="inline-block text-center rounded-full bg-laranja px-5 py-3 text-md text-white w-full"
        >
          Enviar
        </button>
      </div>
    </div>
  </form>

  <Alert v-if="submitError" type="error" :message="alertMessage" @closed="submitError = false" />

  <Alert
    v-if="formSubmitted"
    type="success"
    message="Item publicado com sucesso"
    @closed="formSubmitted = false"
  />
</template>

<script>
import Form from "../models/Form";
import Item from "../models/Item";
import Alert from "./Alert.vue";
import api from "../services/api";

export default {
  name: "FormComponent",
  data() {
    return {
      item: new Item(),
      lostTime: "",
      lostDate: "",
      previews: [],
      submitError: false,
      formSubmitted: false,
      alertMessage: "",
      categories: [],
      locations: [],
      colors: [],
      brands: [],
    };
  },

  props: {
    editMode: {
      type: Boolean,
      default: false
    },
    existingItem: {
      type: Object,
      default: null
    }
  },

  mounted() {
    this.initializeData();

    if (this.editMode && this.existingItem) {
      console.log(this.existingItem)
      // Preencher dados existentes
      this.item = Object.assign(new Item(), this.existingItem);
      
      this.previews.push(...this.existingItem.image_urls);

      if (this.item.found_lost_date) {
        try {
          const date = new Date(this.item.found_lost_date);
          this.item.lostDate = date.getFullYear() + '-' + 
                          String(date.getMonth() + 1).padStart(2, '0') + '-' + 
                          String(date.getDate()).padStart(2, '0');
          this.lostTime = String(date.getHours()).padStart(2, '0') + ':' + 
                          String(date.getMinutes()).padStart(2, '0');
        } catch (error) {
          console.error("Erro ao processar found_lost_date:", error);
        }
        
      }
    }
  },
  methods: {
    initializeData() {
      this.initializeCategories();
      this.initializeLocations();
      this.initializeColors();
      this.initializeBrands();
    },

    async initializeCategories() {
      try {
        const result = await api.get("/categories/");
        this.categories = result.data.results;
      } catch {
        console.log("Erro ao carregar categorias");
      }
    },

    async initializeLocations() {
      try {
        const result = await api.get("/locations/");
        this.locations = result.data.results;
      } catch {
        console.log("Erro ao carregar locais");
      }
    },

    async initializeColors() {
      try {
        const result = await api.get("/colors/");
        this.colors = result.data.results;
      } catch {
        console.log("Erro ao carregar cores");
      }
    },

    async initializeBrands() {
      try {
        const result = await api.get("/brands/");
        this.brands = result.data.results;
      } catch {
        console.log("Erro ao carregar marcas");
      }
    },

    async save() {
      this.item.status = "lost";

      const form = new Form(this.item);

      if (!form.validate()) {
        this.alertMessage = "Verifique os campos marcados com *.";
        this.submitError = true;
        return;
      }

      if (this.item.lostDate) {
        const formattedFoundLostDate = this.formatFoundLostDate();
        form.setFieldValue("found_lost_date", formattedFoundLostDate);
      }

      const formData = form.toFormData();

      try {
        if (this.editMode) {
          
          // Enviar a requisição PATCH para atualizar o item
          await api.patch(`/items/${this.item.id}/`, formData);
          this.formSubmitted = true;
        } else {
          // Criar um novo item normalmente
          await api.post("/items/", formData);
          this.formSubmitted = true;
        }
        setTimeout(() => {
          window.location.replace(`http://localhost:8000/#/lost`);
        }, 1000);
      } catch (error) {
        this.alertMessage = "Erro ao publicar item.";
        this.submitError = true;
      }
    },

    onFileChange(event) {
      if (!this.item.images) {
        this.item.images = [];
      }

      const files = Array.from(event.target.files);
      this.item.images.push(...files);

      files.forEach((file) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.previews.push(e.target.result);
        };
        reader.readAsDataURL(file);
      });
    },

    formatFoundLostDate() {
      const [year, month, day] = this.item.lostDate.split("-").map(Number);

      const [hours, minutes] = this.lostTime?.split(":").map(Number);

      const date = new Date(year, month - 1, day, hours ?? 0, minutes ?? 0);

      const timezoneOffset = date.getTimezoneOffset();
      const sign = timezoneOffset > 0 ? "-" : "+";
      const offset = Math.abs(timezoneOffset);
      const offsetHours = String(Math.floor(offset / 60)).padStart(2, "0");
      const offsetMinutes = String(offset % 60).padStart(2, "0");

      return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}T${String(date.getHours()).padStart(2, "0")}:${String(date.getMinutes()).padStart(2, "0")}:${String(date.getSeconds()).padStart(2, "0")}${sign}${offsetHours}${offsetMinutes}`;
    },

    async removeImage(index) {
      if (index < this.existingItem.image_urls.length) {
        const imageId = this.existingItem.image_ids[index];
        if (imageId) {
          try {
            await api.delete(`/items/${this.item.id}/images/${imageId}/`);
            console.log(`Imagem ${imageId} removida.`);
          } catch (error) {
            console.error("Erro ao remover imagem:", error);
            alert("Erro ao remover a imagem. Tente novamente.");
            return;
          }

          // Remove a imagem dos arrays de imagens existentes
          this.existingItem.image_urls.splice(index, 1);
          this.existingItem.image_ids.splice(index, 1);
        }
      } else {
          // Imagem nova (ainda não foi enviada para a API)
          const newIndex = index - this.existingItem.image_urls.length;
          this.item.images.splice(newIndex, 1);
      }

        // Atualiza a lista de previews corretamente
        this.previews.splice(index, 1);
        
        // Verifica se agora há menos de 2 imagens para reativar o botão de adicionar
        this.$forceUpdate();
    },

    handleSelectChange(event) {
      const element = event.target;

      if (element.value == "clear") {
        this.item[`${element.id}`] = "";
      }
    },
  },
};
</script>

<style scoped></style>
