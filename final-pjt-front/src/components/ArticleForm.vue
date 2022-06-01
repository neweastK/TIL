<template>
  <div class="container">
    <div class="mb-3">
      <hr>

      <form @submit.prevent="onSubmit">
        <div v-if="false">
          <label for="category">category: </label>
          <input v-model="newArticle.category" type="text" id="category" />          
        </div>
        <div>
          <label for="title" class="form-label"></label>
          <input type="text" v-model="newArticle.title" class="form-control" id="title" placeholder="title">
        </div>
        <hr>
        <div class="mb-3">
          <label for="content" class="form-label"></label>
          <textarea class="form-control" v-model="newArticle.content" id="content" rows="20" placeholder="content"></textarea>
        </div>
        <div>
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <button class="btn text-white" style="background-color: MidnightBlue;">{{ action }}</button>
          </div>
        </div>
      </form>
    </div>
    
  </div>


  <!-- <form @submit.prevent="onSubmit">
    <div v-if="false">
      <label for="category">category: </label>
      <input v-model="newArticle.category" type="text" id="category" />
    </div>
    <div>
      <label for="title">title: </label>
      <input v-model="newArticle.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">content: </label>
      <textarea v-model="newArticle.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form> -->
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          category: this.article.category,
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style></style>
