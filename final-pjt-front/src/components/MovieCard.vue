<template>
  <div class="card col-4 col-lg-2 justify-content-center">
    <router-link :to="{ name: 'movie', params: {moviePk: movie.id} }" >
      <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" class="card-img-top" alt="POSTER">
    </router-link>
  </div>
</template>

<script>

export default {
  name: "MovieCard",
  props: {
    movie : Object
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
  /* p {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
  } */
</style>