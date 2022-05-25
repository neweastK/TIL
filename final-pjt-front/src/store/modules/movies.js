// import _ from 'lodash'
import drf from '@/api/drf'
import axios from 'axios'
import router from '@/router'
// import drf from '@/api/drf'


export default {
  state: {
    // 영화 데이터들
    movies : [],
    movie:{},
    poster_path:''

  },

  getters: {
    movies : state => state.movies,
    movie: state => state.movie,


  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,

  },

  actions: {
    fetchMovies ({ commit,getters }) {    
      axios({
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
  }
}