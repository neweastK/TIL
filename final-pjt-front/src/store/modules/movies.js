// import _ from 'lodash'
import drf from '@/api/drf'
import axios from 'axios'
import router from '@/router'



export default {
  state: {
    // 영화 데이터들
    movies : [],
    movie:{},
    poster_path:'',
    fromwatch : [],
    netflix : [],
    watcha : [],
    wavve : [],
    disney : [],

  },

  getters: {
    movies : state => state.movies,
    movie: state => state.movie,


    fromwatch : state => state.fromwatch,
    netflix : state => state.netflix,
    watcha : state => state.watcha,
    wavve : state => state.wavve,
    disney : state => state.disney,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,

    SET_FROMWATCH: (state, movies) => state.fromwatch = movies,
    SET_NETFLIX: (state, movies) => state.netflix = movies,
    SET_WATCHA: (state, movies) => state.watcha = movies,
    SET_WAVVE: (state, movies) => state.wavve = movies,
    SET_DISNEY: (state, movies) => state.disney = movies,
  },

  actions: {
    fetchMovies ({ commit,getters }) {    
      axios({
        // url: 'http://127.0.0.1:8000/api/v1/movies/',
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
  },
    fetchMovie ({ commit,getters }, moviePk) {    
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })  
  },
    likeMovie({ commit, getters }, moviePk) {
      /* 좋아요
      POST: likeMovie URL(token)
        성공하면
          state.Movie 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    WatchMovies ({ commit, getters }) {
      axios({
        url: drf.movies.recommendationWatch(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_FROMWATCH', res.data))
      .catch(err => console.error(err.response))
    },

    NetflixMovies ({ commit, getters }) {
      axios({
        url: drf.movies.recommendationNetflix(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_NETFLIX', res.data))
      .catch(err => console.error(err.response))
    },

    WatchaMovies ({ commit, getters }) {
      axios({
        url: drf.movies.recommendationWatcha(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_WATCHA', res.data))
      .catch(err => console.error(err.response))
    },

    WavveMovies ({ commit, getters }) {
      axios({
        url: drf.movies.recommendationWavve(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_WAVVE', res.data))
      .catch(err => console.error(err.response))
    },

    DisneyMovies ({ commit, getters }) {
      axios({
        url: drf.movies.recommendationDisney(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_DISNEY', res.data))
      .catch(err => console.error(err.response))
    }
  }

}