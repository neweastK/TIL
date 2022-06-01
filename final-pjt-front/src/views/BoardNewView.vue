<template>
  <div class="container">
    <ul class="nav nav-tabs">
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

    <article-form :article="article" action="create"></article-form>
  </div>
</template>


<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'BoardNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          category: 'board',
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
