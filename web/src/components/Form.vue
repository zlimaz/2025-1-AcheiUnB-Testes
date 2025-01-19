<template>
  <form id="app" @submit="save">
    <!-- Nome do item -->
    <div class="mb-4">
      <label
        for="name"
        class="block text-azul text-sm font-bold font-inter mb-2"
        >Item</label
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
    <div class="block relative mb-4">
      <label
        for="category"
        class="block text-azul text-sm font-bold font-inter mb-2"
        >Categoria</label
      >
      <select
        id="category"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="item.category"
        name="category"
      >
        <option value="" disabled selected>Selecione</option>
        <option
          v-for="category of categories"
          :key="category.id"
          :value="category.id"
          class="block text-gray-700 text-sm"
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
    <div class="block relative mb-4">
      <label
        for="location"
        class="block text-azul text-sm font-bold font-inter mb-2"
        >Local</label
      >
      <select
        id="location"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="item.location"
        name="location"
      >
        <option value="" disabled selected>Selecione</option>
        <option
          v-for="location of locations"
          :key="location.id"
          :value="location.id"
          class="block text-gray-700 text-sm"
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
    <div class="block relative mb-4">
      <label
        for="color"
        class="block text-azul text-sm font-bold font-inter mb-2"
        >Cor</label
      >
      <select
        id="color"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="item.color"
        name="color"
      >
        <option value="" disabled selected>Selecione</option>
        <option
          v-for="color of colors"
          :key="color.id"
          :value="color.id"
          class="block text-gray-700 text-sm"
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

    <!-- Data -->
    <div class="mb-4">
      <label
        for="foundLostDate"
        class="block text-azul text-sm font-bold font-inter mb-2"
        >Data</label
      >
      <input
        id="foundLostDate"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="item.foundLostDate"
        type="text"
        name="foundLostDate"
        placeholder="Escreva a data de quando encontrou"
      />
    </div>

    <!-- Brand -->
    <div class="block relative mb-4">
      <label
        for="color"
        class="block text-azul text-sm font-bold font-inter mb-2"
        >Marca</label
      >
      <select
        id="color"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="item.brand"
        name="color"
      >
        <option value="" disabled selected>Selecione</option>
        <option
          v-for="brand of brands"
          :key="brand.id"
          :value="brand.id"
          class="block text-gray-700 text-sm"
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

    <!-- Descrição -->
    <div class="relative w-full min-w-[200px] mb-4">
      <textarea
        id="description"
        v-model="item.description"
        class="peer h-full min-h-[100px] w-full resize-none rounded-[7px] border border-slate-300 bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-slate-300 placeholder-shown:border-t-slate-300 focus:border-2 focus:border-slate-300 focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 disabled:bg-blue-gray-50"
        placeholder=" "
        name="description"
      ></textarea>
      <label
        class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-slate-300 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-slate-300 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-gray-700 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-gray-700 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:border-slate-300 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-slate-300 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-700"
      >
        Descrição
      </label>
    </div>

    <!-- Upload de arquivo -->
    <div class="mb-4">
      <input @change="onFileChange" type="file" />
    </div>

    <!-- Enviar -->
    <div>
      <button
        @click="save"
        class="inline-block text-center rounded-full bg-laranja px-5 py-3 text-md text-white w-full"
      >
        Enviar
      </button>
    </div>
  </form>
</template>

<script>
import Form from "../models/Form";
import Item from "../models/Item";
import api from "../services/api";

export default {
  name: "FormComponent",
  data() {
    return {
      item: new Item(),
      categories: [],
      locations: [],
      colors: [],
      brands: [],
    };
  },
  mounted() {
    this.initializeData();
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
      this.item.status = "found";

      if (this.item.foundLostDate) {
        this.setFoundLostDate();
      }

      console.log("Valores dos campos", this.item);

      const form = new Form(this.item);

      if (form.validate()) {
        const formData = form.toFormData();
        try {
          await api.post("/items/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
          console.log("Formulário enviado com sucesso");
        } catch (error) {
          console.log("Erro ao enviar formulário", error);
        }
      }
    },

    onFileChange(event) {
      const files = Array.from(event.target.files);
      this.item.images = [];
      this.item.images.push(...files);
    },

    setFoundLostDate() {
      const [day, month, year] = this.item.foundLostDate.split("/").map(Number);
      this.item.foundLostDate = new Date(year, month - 1, day);
    },
  },
};
</script>

<style scoped></style>
