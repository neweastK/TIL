<template>
  <div>
    <div class="card">
      <img :src="imgUrl" class="card-img-top" alt="POSTER">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  name: "MovieCard",
  props: {
    movie : Object
  },
  computed: {
    imgUrl(){
      const baseUrl = "https://image.tmdb.org/t/p/w500"
      const videoId = this.movie.poster_path
      return baseUrl + videoId
    }
  }
} 
</script>

<style>
  p {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
  }
</style>