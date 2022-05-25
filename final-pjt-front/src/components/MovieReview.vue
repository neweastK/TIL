<template>
  <div class='container'>
    <div class='row'>
      <h5 class='fw-bold text-start'>리뷰</h5>  
      <p> {{ movie.reviews }}</p>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {

  name: 'MovieInfo',

  data() {
    return {
      moviePk: this.$route.params.moviePk,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'movie']),
    likeCount() {
      return this.movie.like_users?.length
    },
    imgUrl() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w500/'
      return BASE_URL + this.movie.poster_path
    },
    year() {
      const movie_date = this.movie.release_date
      return movie_date.substr(0,4)
    }
  },
  methods: {
    ...mapActions([
      'fetchMovie',
      'likeMovie',
    ])
  },
  created() {
    this.fetchMovie(this.moviePk)
  },
}
</script>

<style>

</style>