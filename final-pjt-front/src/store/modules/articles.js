import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    event_article: [],
    news_article: [],
    column_article: [],
    board_article: [],
    sinye_article: [],
    article: {},
    
  },

  getters: {
    sinye_article: state => state.sinye_article,
    news_article: state => state.news_article,
    event_article: state => state.event_article,
    column_article: state => state.column_article,
    board_article: state => state.board_article,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.id === getters.currentUser.id
    },
    isArticle: state => !_.isEmpty(state.article),
    
    
  },

  mutations: {
    SET_SINYE_ARTICLE: (state, article) => state.sinye_article = article,
    SET_NEWS_ARTICLE: (state, article) => state.news_article = article,
    SET_EVENT_ARTICLE: (state, article) => state.event_article = article,
    SET_COLUMN_ARTICLE: (state, article) => state.column_article = article,
    SET_BOARD_ARTICLE: (state, article) => state.board_article = article,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
    
  },

  actions: {
    fetchSinye({ commit, getters }) {
      axios({
        url: drf.articles.sinye(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_SINYE_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },
    creatSinye({ commit, getters }, article) {
      axios({
        url: drf.articles.sinye(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SINYE_ARTICLE', res.data)
          router.push({
            name: 'sinye_article',
            params: { articlePk: getters.article.pk }
          })
        })
    },

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
            name: 'article',
            params: { articlePk: getters.article.pk }
          })
        })
    },
    fetchArticle({ commit, getters }, articlePk) {

      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    updateArticle({ commit, getters }, { pk, category, title, content}) {
      axios({
        url: drf.articles.article(pk),
        method: 'put',
        data: { category, title, content },
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

    deleteArticle({ commit, getters }, articlePk) {
      /* 게시글 삭제
      사용자가 확인을 받고
        DELETE: article URL (token)
          성공하면
            state.article 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articles' })
          })
          .catch(err => console.error(err.response))
      }
    },

		createComment({ commit, getters }, { articlePk, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.articles.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.articles.comment(articlePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { articlePk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.articles.comment(articlePk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_ARTICLE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },

  },

  






}