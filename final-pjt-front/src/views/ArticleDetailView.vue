<template>
  <div>
    <h1>{{ article.title }}</h1>

    <p>
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>


    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

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
