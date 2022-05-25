<template>
  <div class='container'>
    <div class='row'>
      <h5 class='fw-bold text-start'>줄거리</h5>  
      <p> {{ movie.overview }}</p>
    </div>
    <div class='row'>
      <h5 class='fw-bold text-start'>출연 배우</h5>  
      <ul>
        <li v-for='movieActor in movieActors'
        :key='movieActor.name'>
          {{ movieActor.name }}
        </li>
      </ul>
    </div>
    <div>
      <h5 class='fw-bold text-start'>트레일러</h5>
      <iframe :src="videourl" frameborder="0" width='900' height='400' allowfullscreen></iframe>
    </div>
    <div>
      <h5 class='fw-bold text-start'>스틸컷</h5>
      
      

    </div>


  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDfN3PYabbgHgso6PPs9j7gEzPSNfK6AO8'

export default {

  name: 'MovieInfo',

  data() {
    return {
      moviePk: this.$route.params.moviePk,
      trailer: '',
      videoId:''
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
    },
    movieActors() {
      const movieActors = this.movie.actors
      return movieActors
    },
    videourl(){
      const videoBaseUrl = 'https://youtube.com/embed/'
      // const videoId = (this.trailer.id.videoId ? this.trailer.id.videoId : this.trailer.id)
      return videoBaseUrl + this.videoId
    }},
  methods: {
    ...mapActions([
      'fetchMovie',
      'likeMovie',
    ]),
    onInputChange(){
      axios({
        method:'get',
        url : API_URL,
        params : {
          key : API_KEY,
          part : 'snippet',
          type : 'video',
          q : `공식 예고편 ${ this.movie.title }`,
          maxResults: 1,
        }
      })
        .then(res => {
          this.trailer = res.data.items[0]
          this.videoId = (this.trailer.id.videoId ? this.trailer.id.videoId : this.trailer.id)
        })
        .catch(err=>{
          console.log(err)
        })
      } 
    },
  created() {
    this.fetchMovie(this.moviePk),
    this.onInputChange()
  },
}
</script>

<style>

</style>