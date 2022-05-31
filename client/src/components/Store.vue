<template><pre class="debug">{{auth.$state}}</pre></template>
<script setup lang="ts">
import useAuthStore from '~/store/userstore';

const auth = useAuthStore();


</script>