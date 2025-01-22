<template>
    <div class="fixed w-full top-0" style="z-index: 1">
        <AboutHeader />
    </div>
    <div class="pt-[120px] flex justify-center my-6 text-azul">
        <Logo />
    </div>
    <span class="font-inter text-azul text-center flex justify-center items-center mx-auto max-w-3xl">
        Somos um grupo da disciplina Métodos de Desenvolvimento de Software da Universidade de Brasília.<br>
        Temos como objetivo solucionar um dos problemas da faculdade, que é a falta de ferramentas para organizar itens
        achados e perdidos pelos estudantes.<br>
        Com o AcheiUnB você consegue de forma simples e intuitiva procurar pelo seu item perdido ou cadastrar um item
        que você encontrou.
    </span>

    <div class="max-w-3xl mx-auto mt-10 p-5 pb-[120px]">
        <div class="text-azul text-lg text-center font-semibold mb-8">Criado por:</div>

        <div class="space-y-6">
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/anaelisaramos" target="_blank" class="text-center">
                    <img src="https://github.com/anaelisaramos.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Ana Elisa Ramos</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/DaviCamilo23" target="_blank" class="text-center">
                    <img src="https://github.com/DaviCamilo23.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Davi Camilo</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/potatoyz908" target="_blank" class="text-center">
                    <img src="https://github.com/potatoyz908.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Euller Júlio da Silva</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/leoramiroo" target="_blank" class="text-center">
                    <img src="https://github.com/leoramiroo.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Leonardo Ramiro</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/pedroeverton217" target="_blank" class="text-center">
                    <img src="https://github.com/pedroeverton217.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Pedro Everton</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/314dro" target="_blank" class="text-center">
                    <img src="https://github.com/314dro.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Pedro Martins Silva</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
            <div class="flex items-center space-x-4 justify-center">
                <a href="https://github.com/TiagoBalieiro" target="_blank" class="text-center">
                    <img src="https://github.com/TiagoBalieiro.png"
                        class="w-20 h-20 rounded-full hover:scale-110 transition-transform" />
                    <p class="font-inter text-sm mt-2">Tiago Balieiro</p>
                    <p class="text-xs text-cinza3">Engenharia de Software</p>
                </a>
            </div>
        </div>
    </div>

    <ButtonAdd />
    <div class="fixed bottom-0 w-full">
        <MainMenu activeIcon="info" />
    </div>
</template>

<script setup>
import AboutHeader from "../components/Header-About.vue";
import MainMenu from "../components/Main-Menu.vue";
import Logo from "../components/Logo.vue";
</script>

<style scoped></style>
