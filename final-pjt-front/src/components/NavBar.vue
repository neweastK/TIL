<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <div class="d-grid gap-2 d-md-flex justify-content-md-between">
        <div>
          <a class="navbar-brand" href="#"><router-link class="fw-bold text-decoration-none" :to="{ name: 'index' }">SINYEMA</router-link></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
      <div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="navbar-nav me-auto mb-2 mb-lg-0">
            <div class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <router-link class="fw-bold text-decoration-none" :to="{ name: 'community' }">Community</router-link>
              </a>
              <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#"><router-link style="color:white;" class="text-decoration-none" :to="{ name: 'event_article' }">이벤트</router-link></a></li>
                <!-- <li><hr class="dropdown-divider"></li> -->
                <li><a class="dropdown-item" href="#"><router-link style="color:white;" class="text-decoration-none" :to="{ name: 'column_article' }">칼럼</router-link></a></li>
                <!-- <li><hr class="dropdown-divider"></li> -->
                <li><a class="dropdown-item" href="#"><router-link style="color:white;" class="text-decoration-none" :to="{ name: 'news_article' }">뉴스</router-link></a></li>
                <!-- <li><hr class="dropdown-divider"></li> -->
                <li><a class="dropdown-item" href="#"><router-link style="color:white;" class="text-decoration-none" :to="{ name: 'board_article' }">자유게시판</router-link></a></li>
              </ul>
            </div>
          
            <div class="nav-item" v-if="!isLoggedIn">
              <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" :to="{ name: 'login' }">Login</router-link></a>
            </div>
            <div class="nav-item" v-if="!isLoggedIn">
              <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" :to="{ name: 'signup' }">Signup</router-link></a>
            </div>
            <div class="nav-item" v-if="isLoggedIn">
              <a class="nav-link" href="#">        <router-link class="fw-bold text-decoration-none" :to="{ name: 'mypage', params: { username } }">
            {{ currentUser.username }}'s page
          </router-link></a>
            </div>     
            <div class="nav-item" v-if="isLoggedIn">
              <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" :to="{ name: 'logout' }">Logout</router-link></a>
            </div>  
          </div>
          <!-- <search-bar @input-change="onInputChange">

          </search-bar> -->
          <!-- <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form> -->
          
        </div>
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
