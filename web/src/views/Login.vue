<template>
    <div class="telaInteira flex flex-col justify-between bg-azul text-white h-screen">
      <div class="titulo flex space-x-1 mt-20 ml-10 md:justify-center">
        <h1 class="text-5xl italic font-light md:text-6xl">Achei</h1>
        <h1 class="text-5xl font-bold md:text-6xl">UnB</h1>
      </div>
      <div class="slogan max-w-72 mb-40 ml-10 md:max-w-none md:w-auto md:text-center">
        <p class="text-5xl font-bold md:text-6xl">Perdeu algo no campus?</p>
        <p class="text-5xl italic font-light md:text-6xl">A gente te ajuda!</p>
      </div>

      <div class="flex justify-center  mb-40">
        <button 
        @click="redirectToLoginMicrosoft"
        class="flex items-center rounded-full bg-gray-50 px-5 py-3 text-md font-medium text-azul ring-1 ring-inset ring-gray-500/10">
          <img src="../components/icons/Microsoft_logo2.svg" alt="Logo Microsoft" class="h-6 w-auto mr-2">
          Entre com a conta da Microsoft
        </button>
      </div>
    </div>
</template>

<script setup>
  function redirectToLoginMicrosoft(){
    window.location.href = "http://localhost:8000/accounts/microsoft/login/callback/?code=1.AQoAoZs17AtjK024M8jm1I-AWaQndEAgaUlFgMa8dyuNqUUKAEsKAA.AgABBAIAAADW6jl31mB3T7ugrWTT8pFeAwDs_wUA9P9MZdKMoEzV5HiWul9EpMcaWKfGBT0keLmk9c-rCvbWkOxjVSGoUAMeU6cAae8lWykGXY-tzhlJL6cUPo_1F1vEPTJPL-vd3xiMZhexpdE1KrfxPUJaUfkyZf83gIq6lH5iY8rjmPDncnEGE-QiawLZBcUGrUbCd6yeBV1N2v5tJcUIL0qnOPX55XDo22hEKnC-AGK-PimzMAB66TIfwOmMEmoA-3Oga80t8c6Y3h0fVCbx5znZHoziSu1xaG9f0ZeptIAuZUn_GStwiBVua8wstZ7ETcqmauX6KJIIl2TIUZ_UGDmzlOM-5cAyl6X8K0d-qjQ6ojSppdPt5ZuMXjFJO7uTqxpFfz6z5QoU_JxlG264WmVlGOwZ6LlMVHv29zSeE__3siJqpsnnvqnhMEbsIpxxwHi54esBWwhTEtp70fmDo9QdOzALuUyiCXm09ucno-2c4Xbf7v1NQgbWlzEhzrDVAOM-OKD19B5UMRhqHYbjUwQjjmXm390DoYKNDX3OZbvY5RHiV48Xlw3pH9TtTlyLGgOeX4TkGFSpaorkoRKpf7Ra05vD5pWkY2-w3X0zkWwvjK_CPkqn-6Noj-KNGtAmdzc7CZDY8CkjV7malOf8qHw2JgPP7M2a9jzjk6hNOi0ZKBe1WQBTXDzxzykjHZt1_5Mruo2FDo6mSIr4UcftjCgLf1b7Asd9yIHWSmCA8YhXFWBG8wlI6bNLMj-ytwOcjKYlTdkRTeKT&state=Zay5NfY4tSn7JgvO&session_state=22111dff-b57b-4d45-97be-8c7ffaf3d2b7#"
  }
</script>

<style scoped>

</style>