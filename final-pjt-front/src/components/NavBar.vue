<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#"><router-link :to="{ name: 'index' }">Home</router-link></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#"><router-link :to="{ name: 'sinyema' }">Sinyema</router-link></a>
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
            <a class="nav-link" href="#"><router-link :to="{ name: 'login' }">Login</router-link></a>
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
            <a class="nav-link" href="#"><router-link :to="{ name: 'signup' }">Signup</router-link></a>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <a class="nav-link" href="#"><router-link :to="{ name: 'community' }">Community</router-link></a>
          </li>              
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <router-link :to="{ name: 'community' }">Community</router-link>
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="#"><router-link :to="{ name: 'event_article' }">이벤트</router-link></a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#"><router-link :to="{ name: 'column_article' }">칼럼</router-link></a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#"><router-link :to="{ name: 'news_article' }">뉴스</router-link></a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#"><router-link :to="{ name: 'board_article' }">자유게시판</router-link></a></li>
            </ul>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <a class="nav-link" href="#">        <router-link :to="{ name: 'mypage', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link></a>
          </li>     
          <li class="nav-item" v-if="isLoggedIn">
            <a class="nav-link" href="#"><router-link :to="{ name: 'logout' }">Logout</router-link></a>
          </li>  
        </ul>
        <!-- <search-bar @input-change="onInputChange">

        </search-bar> -->
        <!-- <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form> -->
        
      </div>
    </div>
  </nav>




</template>

<script>
  import { mapGetters } from 'vuex'
  // import SearchBar from '@/components/SearchBar'

  export default {
    name: 'NavBar',
    // components: {
    //   SearchBar,
    // },
    // data(){
    //   return {
    //     inputValue: null,
    //   }
    // },
    // method:{
    //   onInputChange(data){
    //   this.inputValue = data
    //   }

    // },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>



</style>
