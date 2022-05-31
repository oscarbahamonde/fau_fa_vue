<script setup lang="ts">
import { onMounted, ref, Ref } from 'vue'
import { Media }from '~/types'
const route = useRoute()
const token:any = route.query.token || localStorage.getItem('token')
localStorage.setItem('token', token.toString())
const user = ref<User | null>(null)
const image = ref<string | null>(null)
const file: Ref<File | null> = ref(null)
const picture: Ref<Media | null> = ref(null)
type User = {
    id: string
    username: string
    email: string
}
const bgUrl = ref("https://unsplash.it/1200/300/?grayscale")
onMounted(async () => {
    user.value = await fetch('/api/token?access_token=' + token, {
        method: 'POST'
    }).then(res => res.json())
    image.value = await fetch('/api/avatar').then(res=>res.text())
})
const handleClick = async () => {
    bgUrl.value = await fetch("https://unsplash.it/1200/300").then(res => res.url)
}
const onChange = async (e: Event) => {
    const f = (e.target as HTMLInputElement).files![0]
    image.value = await fetch(URL.createObjectURL(f)).then(res => res.url)
    file.value = f
}
const uploadFile = async(e:any)=>{
    e.preventDefault()
    const formData = new FormData()
    formData.append('file', file.value!)
    const media:Media = {
        id: await fetch('/api/id').then(res=>res.text()),
        uid: user.value!.id,
        file: await fetch(URL.createObjectURL(file.value!)).then(res=>res.url),
        filename: file.value!.name,
        content_type: file.value!.type,
        size: file.value!.size.toString(),
        last_modified: file.value!.lastModified.toString(),
    }
    const res = await fetch('/api/upload?access_token=' + token, {
        method: 'POST',
        body: formData
    })
    if(res.status === 200){
        alert('upload success')
        picture.value = media
    }
    else{
        alert('upload failed')
    }
    const response = JSON.stringify(await res.json())
    console.log(response)
    alert(response)
    return response
}

const GET_TOKEN = (e:any)=>{
    e.preventDefault()
    localStorage.setItem('token', token.toString())
    window.location.href = "/user?token=" + token
}



</script>
<template>
<div v-if="token">
        <div class="h-72 rounded
        w-full justify-start row dark:grayscale contrast-150" :style="{
            'background-image': 'url(' + bgUrl + ')',
            'background-size': 'cover',
            'background-position': 'center',
            'background-repeat': 'no-repeat',
            'background-attachment': 'fixed'      
        }"> <i class="mdi-repeat text-3xl dark:text-white cursor-pointer fixed z-50 right-4 top-20" @click="handleClick">
            </i>
            <div class="user_info backdrop-brightness-100 dark-backdrop-brightness-50" v-if="user">
            <span class="user_name">{{ user.username }}</span>
            <span class="user_email">{{ user.email }}</span>
        </div>
        </div>
        
        <div class="avatar  online fixed -translate-y-48 ">
            <img :style="{
                'background-image': 'url(' + image + ')',
                'background-size': 'cover',        
            }" class="gravatar" />
        
               <span  v-if="!file" class="badge p-3 rounded bottom-0 left-0 fixed" @click="GET_TOKEN">Random Avatar </span>
        </div>
        <div class="col">
            <label for="picture"  class="dropzone"><i class="mdi-upload upload" @click="uploadFile" v-if="file"></i>
                <div class="col items-center text-lg" v-if="!file">
                    <h2>Elige tu foto de perfil</h2>
                </div>
                <div class="col items-center" v-else>
                    <h2>{{ file.name }}</h2>
                    </div>
                    <div v-if="file" class="col items-center">
                    <i class="mdi-close-circle-outline" @click.prevent="file = null"></i>
                </div>
            </label>
            <input type="file" id="picture" name="picture" accept="image/*" multiple="false" class="hidden"
                @change="onChange">
        </div>
        <div class="flex justify-evenly">       <pre class="debug">{{JSON.stringify(picture)}}</pre>
</div>
</div>
<div v-if="user?.email.endsWith('cloud')">
<Google /></div>
<div v-else>
<Cart />

</div>
 </template>
<style scoped>
.gravatar {
    @apply rounded-full w-48 h-48 cursor-pointer inline-block border-transparent shadow-md shadow-gray-500 border-2 border-gray-500 ml-4 px-4 -translate-y-1;
}</style>