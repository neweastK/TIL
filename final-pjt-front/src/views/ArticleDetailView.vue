<template>
  <div class="container">
    <ul v-if="article.category==='board'" class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'event_article' }">이벤트</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'column_article' }">칼럼</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'news_article' }">뉴스</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#"><router-link class="fw-bold text-decoration-none" style="color:navy;" :to="{ name: 'board_article' }">자유게시판</router-link></a>
      </li>
    </ul>
    <ul v-if="article.category==='news'" class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'event_article' }">이벤트</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'column_article' }">칼럼</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#"><router-link class="fw-bold text-decoration-none" style="color:navy;" :to="{ name: 'news_article' }">뉴스</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link "  href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'board_article' }">자유게시판</router-link></a>
      </li>
    </ul>
    <ul v-if="article.category==='event'" class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#"><router-link class="fw-bold text-decoration-none" style="color:navy;" :to="{ name: 'event_article' }">이벤트</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'column_article' }">칼럼</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'news_article' }">뉴스</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'board_article' }">자유게시판</router-link></a>
      </li>
    </ul>
    <ul v-if="article.category==='column'" class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'event_article' }">이벤트</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#"><router-link class="fw-bold text-decoration-none" style="color:navy;" :to="{ name: 'column_article' }">칼럼</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'news_article' }">뉴스</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link "  href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'board_article' }">자유게시판</router-link></a>
      </li>
    </ul>
    <!-- <h5 v-if="article.category==='event'">이벤트</h5>
    <h5 v-if="article.category==='column'">칼럼</h5>
    <h5 v-if="article.category==='news'">뉴스</h5>
    <h5 v-if="article.category==='board'">자유게시판</h5>
    <router-link :to="{ name: 'event_article' }">이벤트</router-link> |
    <router-link :to="{ name: 'column_article' }">칼럼</router-link> |
    <router-link :to="{ name: 'news_article' }">뉴스</router-link> |
    <router-link :to="{ name: 'board_article' }">자유게시판</router-link> | -->
    <hr>
    <div class="text-start">
      <h1>{{ article.title }}</h1>
      <br>
      <p>
        {{ article.content }}
      </p>
      <br>


    </div>

    <hr>
    <div class="text-start fw-bold">comment list</div>
    <comment-list :comments="article.comments"></comment-list>
    <br>
    <div class="d-grid gap-2 d-md-flex justify-content-md-between">
      <div v-if="article.category==='event'" class="d-grid gap-2 d-md-flex justify-content-md-start">
        <button class="btn" style="background-color:SlateGray;" type="button"><router-link :to="{ name: 'event_article' }" class=" text-decoration-none" style="color:white;">목록</router-link></button>
      </div>
      <div v-if="article.category==='news'" class="d-grid gap-2 d-md-flex justify-content-md-start">
        <button class="btn" style="background-color:SlateGray;" type="button"><router-link :to="{ name: 'news_article' }" class=" text-decoration-none" style="color:white;">목록</router-link></button>
      </div>
      <div v-if="article.category==='column'" class="d-grid gap-2 d-md-flex justify-content-md-start">
        <button class="btn" style="background-color:SlateGray;" type="button"><router-link :to="{ name: 'column_article' }" class=" text-decoration-none" style="color:white;">목록</router-link></button>
      </div>    
      <div v-if="article.category==='board'" class="d-grid gap-2 d-md-flex justify-content-md-start">
        <button class="btn" style="background-color:SlateGray;" type="button"><router-link :to="{ name: 'board_article' }" class=" text-decoration-none" style="color:white;">목록</router-link></button>
      </div>
      <div v-if="isAuthor">
        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
          <button class="btn me-md-2 " style="background-color: MidnightBlue;" type="button"><router-link class="text-decoration-none" style="color:white; " :to="{ name: 'articleEdit', params: { articlePk } }">수정</router-link></button>
          <button @click="deleteArticle(articlePk)" class="btn text-white" type="button" style="background-color: MidnightBlue;">삭제</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
