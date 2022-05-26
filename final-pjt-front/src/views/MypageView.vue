<template>
  <div>
    <div>
      <profile-view
      :key='profile.id'
      :profile='profile'
      ></profile-view>
    </div>
    <p style='font-size: 1.5rem; font-weight: bold;' class='text-start'>좋아요 누른 영화</p>

    <div class='container'>
      <div class='row'>
        <profile-movie
          v-for="movie in profile.like_movie" 
          :key="movie.id"
          :movie="movie"
          class='col-4'
        >
        </profile-movie>
      </div>
    </div>

    <p style='font-size: 1.5rem; font-weight: bold;' class='text-start'>선호장르</p>
    <h2>{{ likeGenre }}</h2>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ProfileView from '@/components/ProfileView.vue'
import ProfileMovie from '@/components/ProfileMovie.vue'

export default {
  name: 'MypageView',
  components:{
    ProfileView,
    ProfileMovie,
  },
  computed: {
    ...mapGetters(['profile']),
    likeGenre () {
      let likegenres = []
      const movies = this.profile.like_movie
      movies.forEach(movie => {
        let tmp = movie.genres.replace(/"/gi,'')
        likegenres.push(tmp.replace(/"/gi,""))
      }) 
      return likegenres
    }
  },
  methods: {
    ...mapActions(['fetchMypage','totalGenres'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchMypage(payload)
  },
}
</script>
