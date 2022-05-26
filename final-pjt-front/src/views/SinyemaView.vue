<template>
  <div>
    <div class='container'>
      <router-link :to="{ name: 'sinye_article' }">신예</router-link>
      <div class='row justify-content-center mx-5'>
        <movie-card
            v-for="movie in sinyemovie" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
        </movie-card>

      </div>
    </div>
    

  </div>


</template>


<script>
  import MovieCard from "@/components/MovieCard.vue"
  import { mapActions, mapGetters } from 'vuex'
  export default {
    name: "SinyemaView",
    components : {
      MovieCard,
    },
    computed: {
      ...mapGetters(['sinyemovie'])
    },
    methods: {
      ...mapActions(['SinyeMovies'])
    },
    created() {
      this.SinyeMovies()

      }
  }
</script>

<style>

</style>