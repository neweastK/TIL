import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    events: [],
    article: {},

  },

  getters: {
    event: state => state.events,
    article: state => state.article,
  },

  mutations: {
    SET_EVENTS: (state, events) => state.events = events,
    SET_ARTICLE: (state, article) => state.article = article,

  },

  actions: {
    fetchEvents({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.events(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_EVENTS', res.data))
        .catch(err => console.error(err.response))
    },
    createEvent({ commit, getters }, event) {
      /* 게시글 생성
      POST: articles URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      
      axios({
        url: drf.articles.events(),
        method: 'post',
        data: event,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_EVENTS', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },
    createArticle({ commit, getters }, article) {
      /* 게시글 생성
      POST: articles URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

  },

  






}