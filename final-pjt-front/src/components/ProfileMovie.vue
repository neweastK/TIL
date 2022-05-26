<template>
  <div class="card">
    <img :src="imgUrl" class="card-img-top" alt="POSTER">
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
    
  },
  computed: {
    imgUrl(){
      const baseUrl = "https://image.tmdb.org/t/p/w300/"
      const imageId = this.movie.poster_path
      return baseUrl + imageId
    },
  }

}
</script>

<style>

</style>