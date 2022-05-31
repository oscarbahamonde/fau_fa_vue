<template>
<div class="bg-transparent" v-if="!user">
  <Icon icon="logos:google-icon" class="dark:grayscale rounded-full cursor-pointer hover:scale-125  text-3xl fixed top-4 right-4 hover:bg-transparent transition-all ease-in-out animate__animated animate__fadeIn bg-transparent shadow-gray-500 shadow-lg p-1 dark:brightness-150"
  
  @click="handleClick"
  
  />

</div>
<div v-else>
<div class="dark:grayscale rounded-full cursor-pointer hover:scale-125  text-3xl fixed top-4 right-4 hover:bg-transparent transition-all ease-in-out animate__animated animate__fadeIn bg-transparent shadow-gray-500 shadow-lg p-1 dark:brightness-150 dropdown dropdown-end"
  
  @click="handleClock"
  
  >
  <label tabindex="0" class="dropdown-toggle" for="dropdown-menu"><
  <img :src="user.picture" class="rounded-full w-12 h-12" />
  </div>

</div>
</template>
<script setup lang="ts">
import { Icon } from '@iconify/vue'
import { onMounted } from 'vue';
import { getAuth, signInWithPopup, signOut, GoogleAuthProvider } from 'firebase/auth';
import { initializeApp } from 'firebase/app';

const token = localStorage.getItem('token')
const config = ref(null)
const user = ref(null)
onMounted(async()=>{
  config.value = await fetch('/api/config?access_token='+token,
    {
      method: 'POST'
    }).then(res=>res.json()
  )
})
const handleClick = async()=>{
  const auth = getAuth(initializeApp(config.value))
  const res = await signInWithPopup(auth, new GoogleAuthProvider())
  const usr =  {
    'id': res.user.uid,
    'name': res.user.displayName,
    'email': res.user.email,
    'picture': res.user.photoURL,
  }
  alert(JSON.stringify(usr))
  user.value = usr
}

const handleClock = ()=>{
  alert("handleclock")
}

</script>