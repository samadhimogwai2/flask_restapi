<template>
  <router-link v-bind:to="{name: 'home'}" class="btn btn-primary mx-2">
    Home
  </router-link>
  <router-link v-bind:to="{name: 'create'}" class="btn btn-primary mx-2">
    Recognition
  </router-link>
  <router-link v-bind:to="{name: 'get'}" class="btn btn-primary mx-2">
    Get
  </router-link>

  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
}
</script>
