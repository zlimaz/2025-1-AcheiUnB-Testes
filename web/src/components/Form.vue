<template>
  <form
    id="app"
    @submit="save"
  >

    <!-- <p v-if="errors.length">
      <b>Por favor, corrija o(s) seguinte(s) erro(s):</b>
      <ul>
        <li v-for="error in mainForm.errors">{{ error }}</li>
      </ul>
    </p> -->

    <p class="mb-4">
      <label for="name" class="block text-azul text-sm font-bold font-inter mb-2" >Item</label>
      <input
        id="name"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="mainForm.value.name"
        type="text"
        name="name"
        placeholder="Escreva o nome do item"
      >
    </p>

    <p class="block relative mb-4">
      <label for="category" class="block text-azul text-sm font-bold font-inter mb-2">Categoria</label>
      <select
        id="category"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="mainForm.value.category"
        name="category"
        placeholder="Selecione"
      >
        <option class="block text-gray-700 text-sm">Eletrônico</option>
        <option class="block text-gray-700 text-sm">Carteira</option>
        <option class="block text-gray-700 text-sm">Documento</option>
      </select>
      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6">
      <img
        src="../assets/icons/chevron-down.svg"
        alt=""
        class="w-[15px] h-[15px]"
      />
      </div>
    </p>

    <p class="block relative mb-4">
      <label for="location" class="block text-azul text-sm font-bold font-inter mb-2">Local</label>
      <select
        id="location"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="mainForm.value.location"
        name="location"
        placeholder="Selecione"
      >
        <option class="block text-gray-700 text-sm">UED</option>
        <option class="block text-gray-700 text-sm">UAC</option>
        <option class="block text-gray-700 text-sm">RU</option>
      </select>
      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6">
      <img
        src="../assets/icons/chevron-down.svg"
        alt=""
        class="w-[15px] h-[15px]"
      />
      </div>
    </p>

   <p class="block relative mb-4">
    <label for="color" class="block text-azul text-sm font-bold font-inter mb-2">Cor</label>
    <select
      id="color"
      class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      v-model="mainForm.value.color"
      name="color"
      placeholder="Selecione"
    >
      <option class="block text-gray-700 text-sm">Preto</option>
      <option class="block text-gray-700 text-sm">Rosa</option>
      <option class="block text-gray-700 text-sm">Colorido</option>
    </select>
    <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6">
      <img
        src="../assets/icons/chevron-down.svg"
        alt="chevron-down"
        class="w-[15px] h-[15px] fill-current text-white"
      />
    </div>
  </p>

<!-- 
    <p class="block relative mb-4">
      <label for="tamanho" class="block text-azul text-sm font-bold font-inter mb-2">Tamanho</label>
      <select
        id="tamanho"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="mainForm.value.tamanho"
        name="tamanho"
        placeholder="Selecione"
      >
        <option class="block text-gray-700 text-sm">Menos de 1cm</option>
        <option class="block text-gray-700 text-sm">1cm a 5cm</option>
        <option class="block text-gray-700 text-sm">5cm a 15cm</option>
        <option class="block text-gray-700 text-sm">15cm a 30cm</option>
        <option class="block text-gray-700 text-sm">30cm a 60cm</option>
        <option class="block text-gray-700 text-sm">Mais de 60cm</option>
      </select>
      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 mt-6">
      <img
        src="../assets/icons/chevron-down.svg"
        alt=""
        class="w-[15px] h-[15px]"
      />
      </div>
    </p> -->

    <p class="mb-4">
      <label for="foundLostDate" class="block text-azul text-sm font-bold font-inter mb-2">Data</label>
      <input
        id="foundLostDate"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="mainForm.value.foundLostDate"
        type="text"
        name="foundLostDate"
        placeholder="Escreva a data de quando encontrou"
      >
    </p>

    <p class="inline-flex items-center mb-4">
      <label class="flex items-center cursor-pointer relative" for="isValuable">
        <input id="isValuable" v-model="mainForm.value.isValuable"
          class="peer h-5 w-5 cursor-pointer transition-all appearance-none rounded border border-slate-300 checked:bg-slate-800 checked:border-slate-800"
          type="checkbox" name="isValuable"
           />
        <span class="absolute text-white opacity-0 peer-checked:opacity-100 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"
            stroke="currentColor" stroke-width="1">
            <path fill-rule="evenodd"
            d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
            clip-rule="evenodd"></path>
          </svg>
        </span>
      </label>
      <label class="cursor-pointer text-gray-700 text-sm font-bold ml-2" for="isValuable">
        Valioso
      </label>
    </p>

    <p class="mb-2">
      <div class="relative w-full min-w-[200px]">
        <textarea
        id="description" v-model="mainForm.value.description" 
          class="peer h-full min-h-[100px] w-full resize-none rounded-[7px] border border-slate-300 bg-transparent px-3 py-2.5 font-sans text-sm font-normal text-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-slate-300 placeholder-shown:border-t-slate-300 focus:border-2 focus:border-slate-300 focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 disabled:bg-blue-gray-50"
          placeholder=" " name="description"></textarea>
        <label
          class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-slate-300 transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-slate-300 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-gray-700 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-gray-700 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:before:border-slate-300 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-slate-300 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-700">
          Descrição
        </label>
      </div>
    </p>

    <input @change="onFileChange" type="file">

    <div>
      <input
        @click="save"
        value="Enviar"
        class="flex items-center rounded-full bg-laranja px-5 py-3 text-md text-white w-full"
      >
    </div>

  </form>
  </template>

<script>
import axios from "axios"

export default {
  name: 'Form',
  data() {
  return {
    mainForm: {
      value: {
        user: '', 
        name: '', 
        description: '', 
        category: null, 
        location: '', 
        color: null,
        brand: null, 
        isValuable: false, 
        status: 'lost', 
        foundLostDate: null, 
        createdAt: new Date(), 
        barcode: '', 
        images: []
      },
      errors: [],
    },
    entity: null
    
  };
},
  methods: {
    save: async function () {
    const formData = new FormData();
    const formValue = this.mainForm.value
    formData.append("name", formValue.name);
    formData.append("description", formValue.description);
    formData.append("category", 1);
    formData.append("location", 1);
    // formData.append("color", formValue.color);
    // formData.append("brand", formValue.brand);
    formData.append("is_valuable", 'true');
    formData.append("status", 'found');
   
    formValue.images.forEach((image, index) => {
      formData.append(`images`, image);
    });

    console.log(formData)

    try {
      const response = await axios.post("http://localhost:8000/api/items/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2NTc1NjIwLCJpYXQiOjE3MzY1NzIwMjAsImp0aSI6Ijc3Njg0OTA5Y2M1NDQ2OWQ4M2U0NTQyM2Y1ZDk3YjZkIiwidXNlcl9pZCI6MX0.nDH8lnHb2ao09fvtN3WDitC905x-orYEUm1sO7CBqdw"
        }
      });
      console.log('deu bom')
      
    } catch (error) {
      console.log('deu ruim', error)
    }
  },

  onFileChange(event) {
    const files = Array.from(event.target.files);
    this.mainForm.value.images.push(...files); 
  }
}
}

</script>

<style scoped></style>
