<template>
  <div>
    <h1>New Column</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>


<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'ColumnNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          category: 'column',
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
