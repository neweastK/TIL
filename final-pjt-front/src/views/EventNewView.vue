<template>
  <div>
    <h1>New Article</h1>
    <article-form :event="event" action="create"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'EventNewView',
    components: { ArticleForm },
    data() {
      return {
        event: {
          category: 'event',
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
