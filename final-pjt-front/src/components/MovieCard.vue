<template>
  <div>
    <div class="card">
      <!-- <img :src="imgUrl" class="card-img-top" alt="POSTER"> -->
      <div class="card-body">
        <!-- <h5 class="card-title">{{ movie.title }}</h5> -->
        <router-link :to="{ name: 'movie', params: {moviePk: movie.id} }"><img :src="imgUrl" class="card-img-top" alt="POSTER"></router-link>
      </div>
    </div>

    <movie-modal
     :mbutton="mbutton">
    </movie-modal> 
  </div>    
</template>

<script>
import axios from 'axios'
import MovieModal from '@/components/MovieModal.vue'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyBEJh8x8bkj3C08Tliu8ks3ShkeKdQh09s'
export default{
  name: "MovieCard",
  props: {
    movie : Object
  },
  components: {
    MovieModal
  },
  data(){
    return {
      title : "한글",
      trailer: null,
      mbutton : false,
    }
  },
  computed: {
    imgUrl(){
      const baseUrl = "https://image.tmdb.org/t/p/w300/"
      const imageId = this.movie.poster_path
      return baseUrl + imageId
    },
    videourl(){
      const videoBaseUrl = 'https://youtube.com/embed/'
      const videoId = (this.trailer.id.videoId ? this.trailer.id.videoId : this.trailer.id)
      return videoBaseUrl + videoId
  }
 },
 methods: {
  onInputChange(){
    axios({
      method:'get',
      url : API_URL,
      params : {
        key : API_KEY,
        part : 'snippet',
        type : 'video',
        q : `공식 예고편 ${ this.movie.movieNm }`,
        maxResults: 1,
      }
    })
      .then(res => {
        this.trailer = res.data.items[0]
        this.mbutton = true
      })
      .catch(err=>{
        console.log(err)
      })
    } 
  }
}
</script>

<style>
  /* p {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
  } */
</style>