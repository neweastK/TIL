<template>
  <div>
    <!-- <div>
      <div v-if="'왓챠' in profile.using_ott">
        잘보임
      </div>
      <div v-else>
        안보임
      </div>
    </div> -->
    <div>
     <div class='container'>
        <p>박스오피스</p>
        <div class='row justify-content-center mx-5'>
            {{ typeof(profile) }}
            {{ currentUser }}
            {{ profile }}
            
          <movie-card
            v-for="movie in boxoffices" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p v-if="inwatch">최근 {{ profile.watch_movie[profile.watch_movie.length-1].title }}를 본 당신! 이 영화는 어떠신가요?</p>
          <p v-else>최근 본 영화를 체크하세요! 더 정확한 추천을 받을 수 있습니다!</p>
          <movie-card
            v-for="movie in fromwatch" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p v-if="inlike">{{ profile.nickname }}님이 가장 좋아하시는 장르로 준비해봤어요</p>
          <p v-else>영화에 좋아요를 눌러주세요! 더 정확한 추천을 받을 수 있습니다!</p>
          <movie-card
            v-for="movie in fromlike" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p v-if="innetflix">넷플릭스를 구독하고 계시군요!</p>
          <p v-else>넷플릭스에 구독하시면 아래 영화들을 보실 수 있습니다!</p>
          <movie-card
            v-for="movie in netflix" 
            :key="movie.pk"
            :movie="movie"
            class='col-12 col-sm-6 col-lg-3 mb-5 mx-1'
          >
          </movie-card>
          <br>
          <hr>
          <p v-if="inwatcha">보이냐?</p>
          <p v-else>노놓ㅎㅎ</p>
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
    data() {
      return {
      }
    },
    computed: {
      ...mapGetters(['boxoffices', 'fromwatch', 'fromlike', 'netflix', 'watcha', 'wavve', 'disney', 'currentUser', 'profile']),
      inwatcha () {
        return this.profile.using_ott.includes('왓챠')
      },
      innetflix () {
        return this.profile.using_ott.includes('넷플릭스')
      },
      inwatch () {
        return this.profile.watch_movie
      },
      inlike () {
        return this.profile.like_movie
      },

      // inWatch() {
      //   this.inwatcha = this.currentUser.ott_using.include("왓챠")
      //   return this.inwatcha
      // }
    },
    methods: {
      ...mapActions(['fetchProfile','fetchBoxoffices', 'WatchMovies', 'LikeMovies', 'NetflixMovies', 'WatchaMovies', 'WavveMovies', 'DisneyMovies', 'fetchCurrentUser', 'fetchMypage']),
      
    },
    created() {
      this.fetchBoxoffices()
      this.WatchMovies()
      this.LikeMovies()
      this.NetflixMovies()
      this.WatchaMovies()
      this.WavveMovies()
      this.DisneyMovies()
      this.fetchCurrentUser()
      const payload = { username: this.currentUser.username }
      this.fetchMypage(payload)
      // this.fetchProfile(payload)

    },
  }
</script>

<style></style>
