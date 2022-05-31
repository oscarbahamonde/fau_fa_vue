<template>
  <div class="drawer cursor-move z-50 fixed top-0 left-0 dark:bg-black">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content ">
      <div class="main_menu shadow-gray-500 shadow-md hover:shadow-lg">
        <label for="my-drawer">
          <img src="/favicon.svg" class="main_logo dark:invert" /></label>
        <i class="menu_icon mdi-home "
           @click="$router.push('/')"
        ></i>
        <i class="menu_icon mdi-rss "  @click="$router.push('/blog')"></i>
        <a href="https://api.smartpro.cloud"><i class="menu_icon mdi-account "></i></a>

           <i class="menu_icon " @click="toggleDark()">
      <i v-if="isDark.value" i-carbon-moon />
      <i v-else i-carbon-sun />
    </i>
      </div>
         <slot />
    </div>
 
    <div class="drawer-side">
      <label for="my-drawer" class="drawer-overlay"></label>
      <ul class="menu p-8 overflow-y-auto w-100 text-base-content">
        <li><a>Sidebar Item 1</a></li>
        <li><a>Sidebar Item 2</a></li>
      </ul>
    </div>
  </div>
    
</template> 
<style scoped lang="scss">
.main_menu {
  @apply navbar align-middle justify-evenly w-96 h-12 rounded ;
}
.menu_icon {
  @apply  cursor-pointer hover:scale-125 transition-all ease-in-out text-lg;
}
.main_logo {
  @apply w-32 h-32 cursor-pointer;
  @apply hover:animate-pulse;
}
.drawer-overlay {
  @apply cursor-move absolute top-0 left-0 w-full h-full bg-black opacity-75;
}
</style>