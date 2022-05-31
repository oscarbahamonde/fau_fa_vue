<template>
  <nav text-xl mt-6 inline-flex gap-2>
    <Router-Link to="/">

      <div i-carbon-home />
</Router-Link>
    <a
      class="icon-btn"
      rel="noreferrer"
      href="https://api.smartpro.cloud"
      target="_blank"
      title="Login"
    >
    <Icon icon="mdi-account" color="#888888" />    
    </a>
      <div @click="toggleDark()" v-if="isDark" i-carbon-moon />
      <div @click="toggleDark()"  v-else i-carbon-sun />
      
  </nav>
</template>
<script setup lang="ts">
import { Icon } from '@iconify/vue'

</script>