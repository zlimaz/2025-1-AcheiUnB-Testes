import api from '@/services/api';

export const fetchAllItems = async () => {
  try {
    const response = await api.get('/items');
    return response.data.results; // Retorna apenas os resultados
  } catch (error) {
    console.error('Erro ao buscar itens:', error);
    return [];
  }
};
