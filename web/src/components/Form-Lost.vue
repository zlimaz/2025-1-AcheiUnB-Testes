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
          maxlength="750"
          placeholder="Escreva o nome do item"
        />
      </div>

      <!-- Categoria -->
      <div class="block relative mb-4 col-span-2">
        <label for="category" class="font-inter block text-azul text-sm font-bold mb-2">
          Categoria <span class="text-red-500">*</span>
        </label>
        <div class="relative">
          <input
            type="text"
            v-model="searchCategory"
            placeholder="Pesquisar Categoria..."
            class="w-full border rounded py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            @focus="showCategoryDropdown = true"
            @blur="hideDropdown('category')"
          />
          <div class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <img
              src="../assets/icons/chevron-down.svg"
              alt="chevron-down"
              class="w-[15px] h-[15px] cursor-pointer"
              @click="showCategoryDropdown = !showCategoryDropdown"
            />
          </div>
          <ul
            v-if="showCategoryDropdown"
            class="absolute z-10 bg-white border rounded mt-1 w-full max-h-48 overflow-y-auto shadow-lg"
          >
            <li
              v-for="category in filteredCategories"
              :key="category.id"
              @mousedown="selectCategory(category)"
              class="px-3 py-2 hover:bg-gray-200 cursor-pointer"
            >
              {{ category.name }}
            </li>
          </ul>
        </div>
      </div>

      <!-- Location -->
      <div class="block relative mb-4 col-span-2">
        <label for="location" class="font-inter block text-azul text-sm font-bold mb-2 mt-4">
          Localização <span class="text-red-500">*</span>
        </label>
        <div class="relative">
          <input
            type="text"
            v-model="searchLocation"
            placeholder="Pesquisar Localização..."
            class="w-full border rounded py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            @focus="showLocationDropdown = true"
            @blur="hideDropdown('location')"
          />
          <div class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <img
              src="../assets/icons/chevron-down.svg"
              alt="chevron-down"
              class="w-[15px] h-[15px] cursor-pointer"
              @click="showLocationDropdown = !showLocationDropdown"
            />
          </div>
          <ul
            v-if="showLocationDropdown"
            class="absolute z-10 bg-white border rounded mt-1 w-full max-h-48 overflow-y-auto shadow-lg"
          >
            <li
              v-for="location in filteredLocations"
              :key="location.id"
              @mousedown="selectLocation(location)"
              class="px-3 py-2 hover:bg-gray-200 cursor-pointer"
            >
              {{ location.name }}
            </li>
          </ul>
        </div>
      </div>

      <!-- Color -->
      <div class="block relative mb-4 col-span-2">
        <label for="color" class="font-inter block text-azul text-sm font-bold mb-2 mt-4">
          Cor <span class="text-red-500">*</span>
        </label>
        <div class="relative">
          <input
            type="text"
            v-model="searchColor"
            placeholder="Pesquisar Cor..."
            class="w-full border rounded py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            @focus="showColorDropdown = true"
            @blur="hideDropdown('color')"
          />
          <div class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <img
              src="../assets/icons/chevron-down.svg"
              alt="chevron-down"
              class="w-[15px] h-[15px] cursor-pointer"
              @click="showColorDropdown = !showColorDropdown"
            />
          </div>
          <ul
            v-if="showColorDropdown"
            class="absolute z-10 bg-white border rounded mt-1 w-full max-h-48 overflow-y-auto shadow-lg"
          >
            <li
              v-for="color in filteredColors"
              :key="color.id"
              @mousedown="selectColor(color)"
              class="px-3 py-2 hover:bg-gray-200 cursor-pointer"
            >
              {{ color.name }}
            </li>
          </ul>
        </div>
      </div>

      <!-- Brand -->
      <div class="block relative mb-4 col-span-2">
        <label for="brand" class="font-inter block text-azul text-sm font-bold mb-2 mt-4">
          Marca <span class="text-red-500">*</span>
        </label>
        <div class="relative">
          <input
            type="text"
            v-model="searchBrand"
            placeholder="Pesquisar Marca..."
            class="w-full border rounded py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            @focus="showBrandDropdown = true"
            @blur="hideDropdown('brand')"
          />
          <div class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <img
              src="../assets/icons/chevron-down.svg"
              alt="chevron-down"
              class="w-[15px] h-[15px] cursor-pointer"
              @click="showBrandDropdown = !showBrandDropdown"
            />
          </div>
          <ul
            v-if="showBrandDropdown"
            class="absolute z-10 bg-white border rounded mt-1 w-full max-h-48 overflow-y-auto shadow-lg"
          >
            <li
              v-for="brand in filteredBrands"
              :key="brand.id"
              @mousedown="selectBrand(brand)"
              class="px-3 py-2 hover:bg-gray-200 cursor-pointer"
            >
              {{ brand.name }}
            </li>
          </ul>
        </div>
      </div>

      <!-- Data -->
      <div class="mb-4 col-span-2">
        <label for="foundLostDate" class="font-inter block text-azul text-sm font-bold mb-2"
          >Data em que foi perdido</label
        >
        <input
          id="foundLostDate"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="item.foundLostDate === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="item.foundLostDate"
          type="date"
          name="foundLostDate"
        />
      </div>

      <!-- Horário -->
      <div class="mb-4 col-span-2">
        <label for="foundTime" class="font-inter block text-azul text-sm font-bold mb-2"
          >Horário em que foi perdido</label
        >
        <input
          id="foundTime"
          class="appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
          :class="foundTime === '' ? 'text-gray-400' : 'text-gray-700'"
          v-model="foundTime"
          type="time"
          name="foundTime"
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
          maxlength="750"
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
          :class="item.images?.length > 1 ? 'opacity-50 cursor-not-allowed' : ''"
        >
          <img src="../assets/icons/add-item-white.svg" alt="" class="mr-2" />
          Adicionar imagens
          <input
            type="file"
            id="images"
            class="hidden"
            @change="onFileChange"
            :disabled="item.images?.length > 1"
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
      foundTime: "",
      previews: [],
      submitError: false,
      formSubmitted: false,
      alertMessage: "",
      categories: [],
      locations: [],
      colors: [],
      brands: [],
      searchCategory: "",
      searchLocation: "",
      searchBrand: "",
      searchColor: "",
      showCategoryDropdown: false,
      showLocationDropdown: false,
      showBrandDropdown: false,
      showColorDropdown: false,
    };
  },
  mounted() {
    this.initializeData();
  },
  computed: {
    filteredCategories() {
      return this.categories.filter((category) =>
        category.name.toLowerCase().includes(this.searchCategory.toLowerCase()),
      );
    },
    filteredLocations() {
      return this.locations.filter((location) =>
        location.name.toLowerCase().includes(this.searchLocation.toLowerCase()),
      );
    },
    filteredBrands() {
      return this.brands.filter((brand) =>
        brand.name.toLowerCase().includes(this.searchBrand.toLowerCase()),
      );
    },
    filteredColors() {
      return this.colors.filter((color) =>
        color.name.toLowerCase().includes(this.searchColor.toLowerCase()),
      );
    },
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

      if (this.item.foundDate) {
        const formattedFoundLostDate = this.formatFoundLostDate();
        form.setFieldValue("found_lost_date", formattedFoundLostDate);
      }

      const formData = form.toFormData();
      try {
        await api.post("/items/", formData);
        this.formSubmitted = true;

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
      const [year, month, day] = this.item.foundDate.split("-").map(Number);

      const [hours, minutes] = this.foundTime?.split(":").map(Number);

      const date = new Date(year, month - 1, day, hours ?? 0, minutes ?? 0);

      const timezoneOffset = date.getTimezoneOffset();
      const sign = timezoneOffset > 0 ? "-" : "+";
      const offset = Math.abs(timezoneOffset);
      const offsetHours = String(Math.floor(offset / 60)).padStart(2, "0");
      const offsetMinutes = String(offset % 60).padStart(2, "0");

      return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}T${String(date.getHours()).padStart(2, "0")}:${String(date.getMinutes()).padStart(2, "0")}:${String(date.getSeconds()).padStart(2, "0")}${sign}${offsetHours}${offsetMinutes}`;
    },

    removeImage(index) {
      this.previews.splice(index, 1);
      this.item.images.splice(index, 1);
    },

    handleSelectChange(event) {
      const element = event.target;

      if (element.value == "clear") {
        this.item[`${element.id}`] = "";
      }
    },

    selectCategory(category) {
      this.item.category = category.id;
      this.searchCategory = category.name;
      this.showCategoryDropdown = false;
    },

    selectLocation(location) {
      this.item.location = location.id;
      this.searchLocation = location.name;
      this.showLocationDropdown = false;
    },

    selectBrand(brand) {
      this.item.brand = brand.id;
      this.searchBrand = brand.name;
      this.showBrandDropdown = false;
    },

    selectColor(color) {
      this.item.color = color.id;
      this.searchColor = color.name;
      this.showBrandDropdown = false;
    },

    hideDropdown(field) {
      setTimeout(() => {
        if (field === "category") this.showCategoryDropdown = false;
        if (field === "location") this.showLocationDropdown = false;
        if (field === "brand") this.showBrandDropdown = false;
        if (field === "color") this.showColorDropdown = false;
      }, 200);
    },
  },
};
</script>

<style scoped></style>
