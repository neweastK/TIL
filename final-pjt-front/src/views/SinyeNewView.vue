<template>
  <div>
    <h1>신예</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>


<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'SinyeNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          category: 'sinye',
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
