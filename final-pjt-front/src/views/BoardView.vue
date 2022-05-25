<template>
  <div>
    자유게시판
    <router-link :to="{ name: 'event_article' }">이벤트</router-link> |
    <router-link :to="{ name: 'column_article' }">칼럼</router-link> |
    <router-link :to="{ name: 'news_article' }">뉴스</router-link> |
    <router-link :to="{ name: 'board_article' }">자유게시판</router-link> |
    <hr>
    <br>
    <router-link :to="{ name: 'boardnew' }">NEW</router-link>
    <ul>

      <li v-for="article in board_article" :key="article.pk">
        {{ article.user.nickname }} :
        {{ article.title }}

      </li>
    </ul>
  </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "BoardView",
  computed: {
      ...mapGetters(['board_article'])
    },
    methods: {
      ...mapActions(['fetchBoard'])
    },
    created() {
      this.fetchBoard()
    },
}
</script>

<style>

</style>