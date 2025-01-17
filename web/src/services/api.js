import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api",
  Authorization:
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3MTM3MTE3LCJpYXQiOjE3MzcxMzM1MTcsImp0aSI6ImRkZTg0Y2UyNzcwMTRhMTRhMzA2ZWY0OGQ1OGVjYjkxIiwidXNlcl9pZCI6MX0.5xrB27Ww6v9t4-riMmRtFTWoU-lb3R0hX6X_Unw3eVE",
});

export default api;
