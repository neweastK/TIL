<template>
  <div>
    <h1>Home</h1>
    <div>
     <div class='container'>
        <div class='row justify-content-center mx-5'>
          <movie-card
            v-for="movie in movies" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
        </div> 
    </div>
</div>   
    <!-- 글 이동 링크 (제목) -->
    <!-- <router-link 
      :to="{ name: 'movie', params: {moviePk: movie.pk} }">
      {{ movie.title }}
    </router-link> -->   
  </div>
</template>

<script>
  import MovieCard from "@/components/MovieCard.vue"
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'MovieList',
    components : {
      MovieCard,
    },
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style></style>
