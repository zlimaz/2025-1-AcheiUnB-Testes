import axios from 'axios';
import api from '@/services/api';

const API_BASE_URL = 'http://localhost:8000/api/items';

export const fetchAllItems = async () => {
  try {
    const response = await api.get('/items');
    return response.data.results; // Retorna apenas os resultados
  } catch (error) {
    console.error('Erro ao buscar itens:', error);
    return [];
  }
}
export const fetchLostItems = async (page = 1) => {
  const response = await axios.get(`${API_BASE_URL}/lost/`, {
    params: { page },
  });
  return response.data;
};

export const fetchFoundItems = async (page = 1) => {
  const response = await axios.get(`${API_BASE_URL}/found/`, {
    params: { page },
  });
  return response.data;
};
