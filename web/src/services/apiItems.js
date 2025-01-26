import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/items';

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
