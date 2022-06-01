<template>
  <div>
    <movie-card
      v-for="movie in movies"
      :movie='movie'
      :key="movie.id"
      class='row col-3'>
    </movie-card>
  </div>
</template>

<script>
  import MovieCard from "@/components/MovieCard.vue"

  export default {
    name: 'MovieCardList',
    components : {
      MovieCard,
    },
    props: {
      movies:Array
    }
  }
</script>

<style>

</style>