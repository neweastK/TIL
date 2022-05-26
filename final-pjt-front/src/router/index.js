import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import SinyemaView from '../views/SinyemaView.vue'
import CommunityView from '../views/CommunityView.vue'
import ProfileView from '@/views/ProfileView.vue'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

import BoardView from '@/views/BoardView.vue'
import BoardNewView from '@/views/BoardNewView.vue'
import EventView from '@/views/EventView.vue'
import EventNewView from '@/views/EventNewView.vue'
import ArticleNewView from '@/views/ArticleNewView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'
import ColumnView from '@/views/ColumnView.vue'
import ColumnNewView from '@/views/ColumnNewView.vue'
import NewsView from '@/views/NewsView.vue'
import NewsNewView from '@/views/NewsNewView.vue'
import MypageView from '@/views/MypageView.vue'
import NotFound404 from '../views/NotFound404.vue'

import MovieDetail from '@/components/MovieDetail.vue'
import MovieInfo from '@/components/MovieInfo.vue'
import MovieReview from '@/components/MovieReview.vue'
// import WordCloud from '@/components/WordCloud.vue'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [

  // {
  //   path: 'test/',
  //   name: 'test',
  //   component: WordCloud
  // },
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/sinyema',
    name: 'sinyema',
    component: SinyemaView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/mypage/:username',
    name: 'mypage',
    component: MypageView

  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  { path: '/movies/:moviePk',
    name: 'movie',
    props: true,
    component: MovieDetail,
    children: [
      { 
        path: 'info',
        name: 'movieinfo',
        component: MovieInfo
      },
      { 
        path: 'review',
        name: 'moviereviews',
        component: MovieReview
      },
    ]
  },
  {
    path: '/board_article',
    name: 'board_article',
    component: BoardView
  },
  {
    path: '/boardnew',
    name: 'boardnew',
    component: BoardNewView
  },
  {
    path: '/event_article',
    name: 'event_article',
    component: EventView
  },
  {
    path: '/eventnew',
    name: 'eventnew',
    component: EventNewView
  },
  {
    path: '/news_article',
    name: 'news_article',
    component: NewsView
  },
  {
    path: '/newsnew',
    name: 'newsnew',
    component: NewsNewView
  },
  {
    path: '/column_article',
    name: 'column_article',
    component: ColumnView
  },
  {
    path: '/columnnew',
    name: 'columnnew',
    component: ColumnNewView
  },
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
  
]})


export default router
