<template>
  <div>
    <p v-show='false'>{{ profile }}</p>
    
    <h4 class='fw-bold'>박스오피스</h4>
    <movie-card-list
    :movies='boxoffices'
    class='d-flex justify-content-center'>
    </movie-card-list>
        <br>
        <hr>

    <h4 class='fw-bold'> 유니크한 당신을 위한 작품 모음 </h4>
    <movie-card-list
    :movies='indboxoffices'
    class='d-flex justify-content-center'>
    </movie-card-list>
        <br>
        <hr>


    <h4 class='fw-bold' v-if="inwatch">최근 {{ profile.watch_movie[profile.watch_movie.length-1].title }}를 본 당신! 이 영화는 어떠신가요?</h4>
    <h4 class='fw-bold' v-else>최근 본 영화를 체크하세요! 더 정확한 추천을 받을 수 있습니다!</h4>
  
    <movie-card-list
    :movies='fromwatch'
    class='d-flex justify-content-center'>
    </movie-card-list>
        <br>
        <hr>

    <h4 class='fw-bold' v-if="inlike">{{ profile.nickname }}님이 가장 좋아하시는 장르로 준비해봤어요</h4>
    <h4 class='fw-bold' v-else>영화에 좋아요를 눌러주세요! 더 정확한 추천을 받을 수 있습니다!</h4>
    <movie-card-list
    :movies='fromlike'
    class='d-flex justify-content-center'>
    </movie-card-list>
        <br>
        <hr>


    <h4 class='fw-bold' v-if="innetflix">넷플릭스를 구독하고 계시군요! 저두요~</h4>
    <h4 class='fw-bold' v-else>넷플릭스에 구독하시면 아래 영화들을 보실 수 있습니다!</h4>    
    <movie-card-list
    :movies='netflix'
    class='d-flex justify-content-center'>    
    </movie-card-list>
        <br>
        <hr>

    <h4 class='fw-bold' v-if="inwatcha">왓챠챠~ 왓챠를 구독중인 자네! 이런 영화는 어떠신가?</h4>
    <h4 class='fw-bold' v-else>왓챠에선 이런 영화들을 서비스하고 있어요</h4>
    <movie-card-list
    :movies='watcha'
    class='d-flex justify-content-center'>    
    </movie-card-list>
        <br>
        <hr>

    <h4 class='fw-bold' v-if="inwavve">WAVVE 서비스 영화</h4>
    <h4 class='fw-bold' v-else>WAVVE 구독 시 볼 수 있는 영화</h4>
    <movie-card-list
    :movies='wavve'
    class='d-flex justify-content-center'>    
    </movie-card-list>   
        <br>
        <hr>

    <h4 class='fw-bold' v-if="indisney">당신을 위한 디즈니+</h4>
    <h4 class='fw-bold' v-else>디즈니 구독하고 동신(심) 찾자!</h4>
    <movie-card-list
    :movies='disney'
    class='d-flex justify-content-center'>    
    </movie-card-list>   
  </div>
</template>

<script>
  // import MovieCard from "@/components/MovieCard.vue"
  import MovieCardList from "@/components/MovieCardList.vue"

  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'IndexView',
    components : {
      // MovieCard,
      MovieCardList,
    },
    data() {
      return {
      }
    },
    computed: {
      ...mapGetters(['boxoffices','indboxoffices', 'fromwatch', 'fromlike', 'netflix', 'watcha', 'wavve', 'disney', 'currentUser', 'profile']),
      inwatcha () {
        return this.profile.using_ott.includes('왓챠')
      },
      innetflix () {
        return this.profile.using_ott.includes('넷플릭스')
      },
      inwavve () {
        return this.profile.using_ott.includes('웨이브')
      },
      indisney () {
        return this.profile.using_ott.includes('디즈니+')
      },
      inwatch () {
        return this.profile.watch_movie.length
      },
      inlike () {
        return this.profile.like_movie.length
      },
  

      // inWatch() {
      //   this.inwatcha = this.currentUser.ott_using.include("왓챠")
      //   return this.inwatcha
      // }
    },
    methods: {
      ...mapActions(['fetchIndMovies','fetchProfile','fetchBoxoffices', 'WatchMovies', 'LikeMovies', 'NetflixMovies', 'WatchaMovies', 'WavveMovies', 'DisneyMovies', 'fetchCurrentUser', 'fetchMypage']),
      
    },
    created() {
      this.fetchBoxoffices()
      this.WatchMovies()
      this.LikeMovies()
      this.NetflixMovies()
      this.WatchaMovies()
      this.WavveMovies()
      this.DisneyMovies()
      this.fetchIndMovies()
      this.fetchCurrentUser()
      const payload = { username: this.currentUser.username }
      this.fetchMypage(payload)
      // this.fetchProfile(payload)

    },
  }
</script>

<style></style>
