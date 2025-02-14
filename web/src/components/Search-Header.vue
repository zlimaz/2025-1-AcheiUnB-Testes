<template>
  <div
    class="h-[100px] bg-verde shadow-md rounded-b-xl flex items-center justify-between text-white gap-x-9 p-4"
    :class="{ visible: isVisible, invisible: !isVisible }"
  >
    <div class="flex-1">
      <SearchBar />
    </div>
    <button>
      <router-link to="/about" class="no-underline text-white"
        ><Logo class="pr-4" sizeClass="text-2xl"
      /></router-link>
    </button>
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";
import Logo from "./Logo.vue";

export default {
  name: "SearchHeader",
  props: {
    disabled: Boolean,
  },
  components: {
    SearchBar,
    Logo,
  },
  data() {
    return {
      isVisible: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.isVisible = true;
    }, 1);
  },
};
</script>

<style scoped>
.visible {
  opacity: 1;
  transform: translateY(0);

  transition:
    opacity 0.3s ease-in-out,
    transform 0.3s ease-in-out;
}

.invisible {
  opacity: 0;
  transform: translateY(-45px);
}
</style>
