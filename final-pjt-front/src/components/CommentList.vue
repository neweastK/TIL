<template>
  <table class="table table-sm comment-list">
    
    <tbody>
      <tr>
        <comment-list-item 
          v-for="comment in comments" 
          :comment="comment" 
          :key="comment.pk">
        </comment-list-item>
      </tr>
    </tbody>

    <comment-list-form></comment-list-form>
  </table>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>