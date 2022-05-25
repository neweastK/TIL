<template>
  <div>
    <h1>New News</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>


<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'NewstNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          category: 'news',
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
