<template>
  <div>
    이벤트
    <router-link :to="{ name: 'event' }">이벤트</router-link> |
    <router-link :to="{ name: 'column' }">칼럼</router-link> |
    <router-link :to="{ name: 'news' }">뉴스</router-link> |
    <router-link :to="{ name: 'board' }">자유게시판</router-link> |
    <hr>
    <br>
    <router-link :to="{ name: 'eventnew' }">NEW</router-link>
    <ul>

      <li v-for="event in events" :key="event.pk">
        {{ event.user.username }} :
        {{ event.title }}

      </li>
    </ul>
  </div>
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: "EventView",
    computed: {
      ...mapGetters(['events'])
    },
    methods: {
      ...mapActions(['fetchEvents'])
    },
    created() {
      this.fetchEvents()
    },

  }
</script>

<style>

</style>