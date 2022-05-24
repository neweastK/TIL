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
          <br>
          <hr>
          <p>추천추천</p>
          <movie-card
            v-for="movie in fromwatch" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p>넷플릭스</p>
          <movie-card
            v-for="movie in netflix" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p>왓챠챠!</p>
          <movie-card
            v-for="movie in watcha" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p>와~</p>
          <movie-card
            v-for="movie in wavve" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p>디즈니</p>
          <movie-card
            v-for="movie in disney" 
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
      ...mapGetters(['movies', 'fromwatch', 'netflix', 'watcha', 'wavve', 'disney'])
    },
    methods: {
      ...mapActions(['fetchMovies', 'WatchMovies', 'NetflixMovies', 'WatchaMovies', 'WavveMovies', 'DisneyMovies'])
    },
    created() {
      this.fetchMovies()
      this.WatchMovies()
      this.NetflixMovies()
      this.WatchaMovies()
      this.WavveMovies()
      this.DisneyMovies()
    },
  }
</script>

<style></style>
