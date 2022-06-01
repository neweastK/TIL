<template>


  <div class="mb-3">
    <form @submit.prevent="onSubmit" class="comment-list-form">
      <label for="comment" class="form-label"></label>
      <input type="text" class="form-control" id="comment" placeholder="comment" v-model="content" required>
      <div class="m-1 d-grid gap-2 d-md-flex justify-content-md-end">
        <button class="btn btn-light">comment</button>
      </div>
    </form> 
    <br>

    <hr> 
  </div>


</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>