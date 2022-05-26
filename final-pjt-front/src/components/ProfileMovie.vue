<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <router-link :to="{ name: 'movie', params: {moviePk: movie.id} }">DETAIL</router-link>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    movie:Object
  }

}
</script>

<style>

</style>