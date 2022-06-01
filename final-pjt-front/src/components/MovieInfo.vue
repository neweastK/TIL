<template>
  <div class='container'>
    <div class='row'>
      <h5 class='fw-bold text-start'>줄거리</h5>  
    </div>
    <br>
    <h5 class='fw-bold text-start mb-3'>출연 배우</h5>  
      <div class='d-flex justify-content-between mx-3'>
        <div v-for='movieActor in movieActors'
        :key='movieActor.name'
        >
          <div class='box'>
            <img class='profile' :src="`https://image.tmdb.org/t/p/w200${ movieActor.profile }`" :alt=path>
          </div>
          <p class='text-center'>{{ movieActor.name }}</p>
        </div>
      </div>
    <h5 class='fw-bold text-start mt-5'>트레일러</h5>
    <div class='d-flex my-4 justify-content-center'>
      <iframe class='mb-5' :src="videourl" frameborder="0" width='900' height='400' allowfullscreen></iframe>
    </div>
    <div class='mt-4'>
      <h5 class='mt-4 fw-bold text-start'>스틸컷</h5>
      
      <div>
        <b-carousel
          id="carousel-fade"
          style="text-shadow: 0px 0px 2px #000"
          fade
          :controls='true'
          label-next='>'
          label-prev='<'
          img-width="1024"
          img-height="480"
        >
          <b-carousel-slide
          v-for="path in backDrops"
          :key=path>
            <template #img>
              <img
                class="d-block mx-auto img-fluid w-50"
                width="700"
                height="480"
                :src="`https://image.tmdb.org/t/p/w500${path.substring(1,path.length-1)}`"
                alt="image slot"
              >
            </template>
          </b-carousel-slide>
        </b-carousel>
        
      </div>


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
      videoId:'',
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'movie']),
    likeCount() {
      return this.movie.like_users?.length
    },
    imgUrl() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w500'
      return BASE_URL
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
    },
    backDrops(){
      const backDrops = this.movie.backdrops
      const imsi = backDrops.replaceAll(',','')
      const paths = imsi.substring(1,imsi.length-1).split(' ')
      return paths
    }
    },
    
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
  .box {
    width: 100px;
    height: 100px; 
    border-radius: 70%;
    overflow: hidden;
  }
  .profile {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }
</style>