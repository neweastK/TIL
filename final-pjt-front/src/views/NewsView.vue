<template>
  <div>
    뉴스
    <router-link :to="{ name: 'event_article' }">이벤트</router-link> |
    <router-link :to="{ name: 'column_article' }">칼럼</router-link> |
    <router-link :to="{ name: 'news_article' }">뉴스</router-link> |
    <router-link :to="{ name: 'board_article' }">자유게시판</router-link> |
    <hr>
    <br>
    <router-link :to="{ name: 'newsnew' }">NEW</router-link>
    <ul>

      <li v-for="article in news_article" :key="article.pk">
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
      name: "NewsView",
      computed: {
        ...mapGetters(['news_article'])
      },
      methods: {
        ...mapActions(['fetchNews'])
      },
      created() {
        this.fetchNews()
    },
  }
</script>

<style>

</style>