<template>
<i class="mdi-cart dark:grayscale rounded-full cursor-pointer hover:scale-125  text-3xl fixed top-4 right-4 hover:bg-transparent transition-all ease-in-out animate__animated animate__fadeIn bg-transparent shadow-gray-500 shadow-lg p-1 dark:brightness-150 w-10 h-10"

@click = "handleClick"

></i>
</template>
<script setup lang="ts">
const token = localStorage.getItem('token')
const handleClick=()=>{
    alert("This is the shopping cart not implemented yet" + token)
}

</script>