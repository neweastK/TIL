<template>
  <div> 
    <div class='container'>
      <div class='row col-12 my-3'>
        <img :src='imgUrl' alt="POSTER" class='col-3'>
        <span class='col-8 mt-auto'>
          <h1 class='col-12 text-start'>{{ movie.title }}({{ year }})</h1>
          <p class='fw-bold text-start'> 한국  가족/코미디  1시간 30분 </p>
        </span>
      </div>
      <div class='mt-5 text-start'>
        <router-link :to="{ name: 'movieinfo', params: { moviePk } }">
          정보
        </router-link> 
        | 
        <router-link :to="{ name: 'moviereviews', params: { moviePk } }">
          리뷰
        </router-link>        
        <hr />
        <router-view></router-view>
      </div>

    </div>

    
    <!-- movie Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'movieEdit', params: { moviePk } }">
        <button>Edit</button>
      </router-link>
      |
    </div>

    <!-- movie Like UI -->
    <div>
      Likeit:
      <button
        @click="likeMovie(moviePk)"
      >{{ likeCount }}</button>
    </div>
    <hr />
  </div>  

</template>


<script>
  import { mapGetters, mapActions } from 'vuex'
  
  export default {
    name: 'MovieDetail',
    components: {
    },
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