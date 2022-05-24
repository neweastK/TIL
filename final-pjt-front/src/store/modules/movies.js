// import _ from 'lodash'
import axios from 'axios'
// import router from '@/router'
import drf from '@/api/drf'


export default {
  state: {
    // 영화 데이터들
    movies : [],
    fromwatch : [],
    netflix : [],
    watcha : [],
    wavve : [],
    disney : [],

  },

  getters: {
    movies : state => state.movies,
    fromwatch : state => state.fromwatch,
    netflix : state => state.netflix,
    watcha : state => state.watcha,
    wavve : state => state.wavve,
    disney : state => state.disney,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
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
    },


  }

  






}