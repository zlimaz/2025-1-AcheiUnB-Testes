/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/views/Login.vue",
    "./src/views/About.vue",
    "./src/components/Logo.vue",
    "./src/components/Main-Menu.vue",
    "./src/icons/Search-Icon.vue",
  ],
  theme: {
    extend: {
      colors: {
        azul: "#133E78",
        laranja: "#F59E0B",
        verde: "#008940",
      },
    },
  },
  plugins: [],
};
