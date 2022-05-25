<template>
  <div>
    <h1>자유게시판</h1>
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
