<template>
  <div>
    칼럼
    <router-link :to="{ name: 'event_article' }">이벤트</router-link> |
    <router-link :to="{ name: 'column_article' }">칼럼</router-link> |
    <router-link :to="{ name: 'news_article' }">뉴스</router-link> |
    <router-link :to="{ name: 'board_article' }">자유게시판</router-link> |
    <hr>
    <br>
    <router-link :to="{ name: 'columnnew' }">NEW</router-link>
    <ul>

      <li v-for="article in column_article" :key="article.pk">
        {{ article.user.nickname }} :
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>

      </li>
    </ul>
  </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "ColumnView",
  computed: {
      ...mapGetters(['column_article'])
    },
    methods: {
      ...mapActions(['fetchColumn'])
    },
    created() {
      this.fetchColumn()
    },
}
</script>

<style>

</style>