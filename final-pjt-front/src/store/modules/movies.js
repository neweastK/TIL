// import _ from 'lodash'
import axios from 'axios'
// import router from '@/router'
// import drf from '@/api/drf'


export default {
  state: {
    // 영화 데이터들
    movies : []

  },

  getters: {
    movies : state => state.movies

  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies
  },

  actions: {
    fetchMovies ({ commit,getters }) {    
      axios({
        url: 'http://127.0.0.1:8000/api/v1/movies/',
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
  }
  }

  






}