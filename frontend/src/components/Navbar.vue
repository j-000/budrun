<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link class="navbar-brand" :to="{name: 'home'}">Budrun</router-link>
    <router-link class="nav-link active" :to="{name: 'users'}">Users</router-link>
    </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>

</style>