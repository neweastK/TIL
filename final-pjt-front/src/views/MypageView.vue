<template>
  <div>
    <div>
      <profile-view
      :key='profile.id'
      :profile='profile'
      ></profile-view>
    </div>
    <p style='font-size: 1.5rem; font-weight: bold;' class='text-start ms-5'>좋아요 누른 영화</p>

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

    <p style='font-size: 1.5rem; font-weight: bold;' class='text-start mt-5 ms-5'>선호장르</p>
    <div class='d-flex'>
      <div class='my-5 mx-5'>
        <b-icon icon='hammer' font-scale="5"> </b-icon>
        <h5 class='mt-2'> 범죄 </h5>
      </div>
      <div class='my-5'>
        <b-icon icon='music-note-beamed' font-scale="5"> </b-icon>
        <h5 class='mt-2'> 음악 </h5>
      </div>
    </div>
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
    ...mapGetters(['profile'])},  
  methods: {
    ...mapActions(['fetchMypage','totalGenres'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchMypage(payload)
  },
}
</script>
