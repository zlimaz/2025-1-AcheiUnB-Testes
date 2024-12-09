import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/api";
axios.defaults.timeout = 10000;
axios.defaults.headers["Content-Type"] = "application/json";
axios.defaults.headers["Accept"] = "application/json";

export default axios;
