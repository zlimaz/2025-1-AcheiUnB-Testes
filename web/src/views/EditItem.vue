<template>
    <div>
      <ItemHeader 
        :title="'Editar Item'" :itemId="itemId" 
        class="fixed w-full top-0" style="z-index: 1"/>
      </div>

      <div class="px-6 py-[120px]" style="z-index: 2">
        <FormLost 
        v-if="item.id && item.status === 'lost'"
        :editMode="true"
        :existingItem="item"
      />
      
      <FormFound 
        v-if="item.id && item.status === 'found'"
        :editMode="true"
        :existingItem="item"
      />
      </div>
  </template>
  
  <script>
  import ItemHeader from '@/components/Item-Header.vue';
  import FormLost from '@/components/Form-Lost.vue';
  import FormFound from '@/components/Form-Found.vue';
  import api from '@/services/api';
  
  export default {
    components: { ItemHeader, FormLost, FormFound },
    props: {
    id: {
      type: [String, Number], // Pode ser string (valor bruto) ou number (se converter)
      required: true
    }
  },
    data() {
      return {
        itemId: null,
        item: {}
      }
    },
    async mounted() {
      this.itemId = this.$route.params.id;
      await this.loadItem();
      console.log(this.item)
    },
    methods: {
      async loadItem() {
        try {
          const response = await api.get(`/items/${this.itemId}/`);
          this.item = response.data;
        } catch (error) {
          console.error('Erro ao carregar item:', error);
        }
      }
    }
  }
  </script>