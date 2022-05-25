import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'


export default {
  state: {
    event_article: {},
    news_article: {},
    column_article: {},
    board_article: {},
    article: {},
    
  },

  getters: {
    news_article: state => state.news_article,
    event_article: state => state.event_article,
    column_article: state => state.column_article,
    board_article: state => state.board_article,
    article: state => state.article,
    
    
  },

  mutations: {
    SET_NEWS_ARTICLE: (state, article) => state.news_article = article,
    SET_EVENT_ARTICLE: (state, article) => state.event_article = article,
    SET_COLUMN_ARTICLE: (state, article) => state.column_article = article,
    SET_BOARD_ARTICLE: (state, article) => state.board_article = article,
    SET_ARTICLE: (state, article) => state.article = article,
    
  },

  actions: {
    fetchEvents({ commit, getters }) {
      axios({
        url: drf.articles.events(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_EVENT_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },
    createEvent({ commit, getters }, article) {
      axios({
        url: drf.articles.events(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_EVENT_ARTICLE', res.data)
          router.push({
            name: 'event_article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    fetchNews({ commit, getters }) {
      axios({
        url: drf.articles.news(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_NEWS_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },
    creatNews({ commit, getters }, article) {
      axios({
        url: drf.articles.news(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_NEWS_ARTICLE', res.data)
          router.push({
            name: 'news_article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    fetchColumn({ commit, getters }) {
      axios({
        url: drf.articles.column(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_COLUMN_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },
    creatColumn({ commit, getters }, article) {
      axios({
        url: drf.articles.column(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_COLUMN_ARTICLE', res.data)
          router.push({
            name: 'column_article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

    fetchBoard({ commit, getters }) {
      axios({
        url: drf.articles.board(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_BOARD_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },
    creatBoard({ commit, getters }, article) {
      axios({
        url: drf.articles.board(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_BOARD_ARTICLE', res.data)
          router.push({
            name: 'board_article',
            params: { articlePk: getters.article.pk }
          })
        })
    },


    createArticle({ commit, getters }, article) {
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'community',
            // params: { articlePk: getters.article.pk }
          })
        })
    },


  },

  






}