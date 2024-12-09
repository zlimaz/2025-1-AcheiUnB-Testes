<template>
  <div
    id="transition-screen"
    class="fixed inset-0 flex items-center justify-center z-50"
  >
    <div class="fixed inset-0 flex items-center justify-center z-50">
      <Logo customClass="text-azul" />
    </div>
  </div>

  <div
    id="main-content"
    class="telaInteira bg-azul text-white p-4 h-screen hidden"
  >
    <div
      class="titulo flex space-x-1 mt-20 mb-20 ml-8 md:flex md:justify-center md:mb-52"
    >
      <Logo />
    </div>
    <div
      class="slogan max-w-72 ml-8 md:mr-8 md:max-w-none md:w-auto md:text-center"
    >
      <p class="text-5xl font-bold mb-4 md:text-6xl">Perdeu algo no campus?</p>
      <p class="text-5xl italic font-light mb-4 md:text-6xl">
        A gente te ajuda!
      </p>
    </div>

    <div class="flex justify-center mt-52 lg:">
      <button
        @click="redirectToLoginMicrosoft"
        class="flex items-center rounded-full bg-gray-50 px-5 py-3 text-md font-medium text-azul ring-1 ring-inset ring-gray-500/10"
      >
        <img
          src="../components/icons/Microsoft_logo.svg"
          alt="Logo Microsoft"
          class="h-6 w-auto mr-2"
        />
        Entre com a conta da Microsoft
      </button>
    </div>
  </div>
</template>

<script setup>
import Logo from "../components/Logo.vue";

window.addEventListener("load", () => {
  const transitionScreen = document.getElementById("transition-screen");
  const mainContent = document.getElementById("main-content");

  setTimeout(() => {
    transitionScreen.classList.add("fade-out");
  }, 500);

  transitionScreen.addEventListener("animationend", () => {
    transitionScreen.classList.add("hidden");
    mainContent.classList.remove("hidden");
    mainContent.classList.add("fade-in");
  });
});

function redirectToLoginMicrosoft() {
  window.location.href =
    "http://localhost:8000/accounts/microsoft/login/callback/?code=1.AQoAoZs17AtjK024M8jm1I-AWaQndEAgaUlFgMa8dyuNqUUKAEsKAA.AgABBAIAAADW6jl31mB3T7ugrWTT8pFeAwDs_wUA9P9MZdKMoEzV5HiWul9EpMcaWKfGBT0keLmk9c-rCvbWkOxjVSGoUAMeU6cAae8lWykGXY-tzhlJL6cUPo_1F1vEPTJPL-vd3xiMZhexpdE1KrfxPUJaUfkyZf83gIq6lH5iY8rjmPDncnEGE-QiawLZBcUGrUbCd6yeBV1N2v5tJcUIL0qnOPX55XDo22hEKnC-AGK-PimzMAB66TIfwOmMEmoA-3Oga80t8c6Y3h0fVCbx5znZHoziSu1xaG9f0ZeptIAuZUn_GStwiBVua8wstZ7ETcqmauX6KJIIl2TIUZ_UGDmzlOM-5cAyl6X8K0d-qjQ6ojSppdPt5ZuMXjFJO7uTqxpFfz6z5QoU_JxlG264WmVlGOwZ6LlMVHv29zSeE__3siJqpsnnvqnhMEbsIpxxwHi54esBWwhTEtp70fmDo9QdOzALuUyiCXm09ucno-2c4Xbf7v1NQgbWlzEhzrDVAOM-OKD19B5UMRhqHYbjUwQjjmXm390DoYKNDX3OZbvY5RHiV48Xlw3pH9TtTlyLGgOeX4TkGFSpaorkoRKpf7Ra05vD5pWkY2-w3X0zkWwvjK_CPkqn-6Noj-KNGtAmdzc7CZDY8CkjV7malOf8qHw2JgPP7M2a9jzjk6hNOi0ZKBe1WQBTXDzxzykjHZt1_5Mruo2FDo6mSIr4UcftjCgLf1b7Asd9yIHWSmCA8YhXFWBG8wlI6bNLMj-ytwOcjKYlTdkRTeKT&state=Zay5NfY4tSn7JgvO&session_state=22111dff-b57b-4d45-97be-8c7ffaf3d2b7#";
}
</script>

<style scoped>
.fade-out {
  animation: fadeOut 1s forwards;
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.fade-in {
  animation: fadeIn 1s forwards;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>
