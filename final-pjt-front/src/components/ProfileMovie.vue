<template>
  <div class="card my-2 justify-content-center">
    <router-link :to="{ name: 'movie', params: {moviePk: movie.id} }">
      <img :src="imgUrl" class="card-img-top" alt="POSTER">
    </router-link>
    <div class="card-body">
      <h6 class="card-title">{{ movie.title }}</h6>
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