<template>
    <div>
      <ItemHeader 
      :title="tituloHeader"
      :itemId="itemId" 
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

      <Alert v-if="submitError" type="error" :message="alertMessage" @closed="submitError = false" />
  </template>
  
  <script>
  import ItemHeader from '@/components/Item-Header.vue';
  import FormLost from '@/components/Form-Lost.vue';
  import FormFound from '@/components/Form-Found.vue';
  import api from '@/services/api';
  import { ref } from 'vue';
  import Alert from "@/components/Alert.vue";
  
  export default {
    components: { ItemHeader, FormLost, FormFound },
    props: {
    id: {
      type: [String, Number], // Pode ser string (valor bruto) ou number (se converter)
      required: true
    },
  },
    data() {
      return {
        itemId: null,
        item: {},
        currentUser: null,
        alertMessage: "",
        submitError: false,
      };
    },

    computed: {
    tituloHeader() {
      return `Editar Item ${this.item.status === 'found' ? 'Achado' : 'Perdido'}`;
    }
  },

    async created() {
      this.itemId = this.$route.params.id;
      await this.loadItem();

      try {
        const response = await api.get(`/auth/user/`);
        this.currentUser = response.data;  // Atribuindo o valor de currentUser
      } catch (error) {
        console.error("Erro ao buscar usuário:", error);
        this.alertMessage = "Erro ao buscar usuário.";
        this.submitError = true;
      }

      try {
        const response = await api.get(`/items/${this.itemId}/`);
        this.item = response.data;
      } catch (error) {
        console.error('Erro ao carregar item:', error);
        this.alertMessage = "Erro ao carregar item.";
        this.submitError = true;
      }

      if (this.currentUser && this.item.user_id !== this.currentUser.id) {
        this.$router.push(`/${this.item.status}`)
      }

    },
    methods: {
      async loadItem() {
        try {
          const response = await api.get(`/items/${this.itemId}/`);
          this.item = response.data;
        } catch (error) {
          console.error('Erro ao carregar item:', error);
          this.alertMessage = "Erro ao carregar item.";
          this.submitError = true;
        }
      }
    },
  }
  </script>