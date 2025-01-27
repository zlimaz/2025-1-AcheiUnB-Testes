import axios from 'axios';
import { filtersState } from '@/store/filters';

const API_BASE_URL = 'http://localhost:8000/api/items';

// Função para buscar itens perdidos com filtros opcionais
export const fetchLostItems = async ({ page = 1, search = "", category_name = "", location_name = "" }) => {
  const params = {
    page,
    ...(filtersState.searchQuery && { search: filtersState.searchQuery }),
    ...(filtersState.activeCategory && { category_name: filtersState.activeCategory }),
    ...(filtersState.activeLocation && { location_name: filtersState.activeLocation }),
  };

  const response = await axios.get(`${API_BASE_URL}/lost/`, { params });
  return response.data;
};

// Função para buscar itens encontrados com filtros opcionais
export const fetchFoundItems = async ({ page = 1, search = "", category_name = "", location_name = "" }) => {
  const params = {
    page,
    ...(filtersState.searchQuery && { search: filtersState.searchQuery }),
    ...(filtersState.activeCategory && { category_name: filtersState.activeCategory }),
    ...(filtersState.activeLocation && { location_name: filtersState.activeLocation }),
  };

  const response = await axios.get(`${API_BASE_URL}/found/`, { params });
  return response.data;
};

export const fetchMyItemsFound = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/found/my-items/`);
    console.log("Foi")
    return response.data; // Retorna os dados da resposta
  } catch (error) {
    console.error("Erro ao buscar itens encontrados:", error);
    throw error; // Lança o erro para ser tratado onde a função for chamada
  }
};