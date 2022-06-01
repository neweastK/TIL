<template>
  <div>
    <h1>{{ profile.nickname }}</h1>
    <p style='font-size: 1.5rem; font-weight: bold;' class='text-start'>좋아요 누른 영화</p>
    <ul>

    </ul>

    <div class='container'>
      <div class='row col-4 ms-auto'>
        <profile-view
        :key='profile.id'
        :profile='profile'
        ></profile-view>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ProfileView from '@/components/ProfileView.vue'

// import ProfileMovie from '@/components/ProfileMovie.vue'

export default {
  name: 'MypageView',
  components:{
    ProfileView,

    // ProfileMovie,
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
