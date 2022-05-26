<template>
  <div> 
    <div class='container'>
      <div class='row col-12 my-3'>
        <img :src='imgUrl' alt="POSTER" class='col-3'>
        <span class='col-8 mt-auto'>
          <div class='d-flex justify-content-between mt-3'>
            <span>
              <b-avatar v-if='movie.ott_service.toString().includes("넷플릭스")' class='mx-1' src="data:image/png;base64,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"></b-avatar>
              <b-avatar v-if='movie.ott_service.toString().includes("왓챠")' class='mx-1' src="https://play-lh.googleusercontent.com/vAkKvTtE8kdb0MWWxOVaqYVf0_suB-WMnfCR1MslBsGjhI49dAfF1IxcnhtpL3PnjVY"></b-avatar>
              <b-avatar v-if='movie.ott_service.toString().includes("디즈니+")' class='mx-1' src="https://img.wowtv.co.kr/wowtv_news/dnrs/20211112/B20211112084626560.jpg"></b-avatar>
              <b-avatar v-if='movie.ott_service.toString().includes("웨이브")' class='mx-1' src="https://blog.kakaocdn.net/dn/tcKJL/btqzxL8ScfL/85Tn0pptWTbRJKMyMplns1/img.jpg"></b-avatar>
            </span>
            <span class='d-flex me-4'>
              <b-icon v-if='movie.like.includes(currentUser.pk)' icon='heart-fill' class='h2 mx-2' variant="danger" @click="likeMovie(moviePk)"></b-icon>
              <b-icon v-else icon='heart' class='h2 mx-2' variant="danger" @click="likeMovie(moviePk)"></b-icon>
              <p class='fw-bold'> {{ likeCount }} </p>
              <b-icon v-if='movie.watch.includes(currentUser.pk)' icon='sunglasses' class='mx-2' font-scale="2" @click="watchedMovie(moviePk)"></b-icon>
              <b-icon v-else icon='eyeglasses' class='mx-2' font-scale="2" @click="watchedMovie(moviePk)"></b-icon>
              <p class='fw-bold'> {{ watchedCount }} </p>
            </span>
          </div>
          <h1 class='col-12 text-start my-3'>{{ movie.title }}({{ year }})</h1>
          <p class='fw-bold text-start my-1'> 장르 : {{ movie.genres.substring(1,movie.genres.length-1).replace(/,/gi,"/").replace(/'/gi,"") }}</p>
          <p class='fw-bold text-start my-1'> 러닝타임 : {{ movie.runtime }}분</p>
        </span>
      </div>
      <div class='mt-5 text-start'>
        <router-link :to="{ name: 'movieinfo', params: { moviePk } }" class='h5 text-decoration-none text-black fw-bold'>
          정보
        </router-link> 
        | 
        <router-link :to="{ name: 'moviereviews', params: { moviePk } }" class='h5 text-decoration-none text-black fw-bold'>
          리뷰
        </router-link>        
        <hr />
        <router-view></router-view>
      </div>

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
      ...mapGetters(['isAuthor', 'movie', 'watchedmovie', 'currentUser']),
      likeCount() {
        return this.movie.like?.length
      },
      watchedCount() {
        return this.movie.watch?.length
      },
      imgUrl() {
        const BASE_URL = 'https://image.tmdb.org/t/p/w500/'
        return BASE_URL + this.movie.poster_path
      },
      year() {
        const movie_date = this.movie.release_date.substr(0,4)
        return movie_date
      },
      },
    methods: {
      ...mapActions([
        'fetchMovie',
        'likeMovie',
        'watchedMovie',
      ])},
    created() {
      this.fetchMovie(this.moviePk)
    }
  }
</script>

<style>

</style>