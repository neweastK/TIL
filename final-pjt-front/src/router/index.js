import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import SinyemaView from '../views/SinyemaView.vue'
import CommunityView from '../views/CommunityView.vue'
import MypageView from '../views/MypageView.vue'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import BoardView from '@/views/BoardView.vue'
import EventView from '@/views/EventView.vue'
import EventNewView from '@/views/EventNewView.vue'
import ColumnView from '@/views/ColumnView.vue'
import NewsView from '@/views/NewsView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
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
    path: '/mypage',
    name: 'mypage',
    component: MypageView
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
    path: '/mypage',
    name: 'mypage',
    component: MypageView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/news',
    name: 'news',
    component: NewsView
  },
  {
    path: '/board',
    name: 'board',
    component: BoardView
  },
  {
    path: '/event',
    name: 'event',
    component: EventView
  },
  {
    path: '/eventnew',
    name: 'eventnew',
    component: EventNewView
  },
  {
    path: '/column',
    name: 'column',
    component: ColumnView
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
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
