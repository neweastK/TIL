<template>
  <div class='container'>
    <div class='row'>
      <h5 class='fw-bold text-start'>리뷰</h5>  
    </div>
    <review-list-form></review-list-form>
    
    <ul>
      <review-list-item 
        v-for="review in reviews" 
        :review="review" 
        :key="review.pk">
      </review-list-item>        
    </ul>

  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'
import { mapGetters } from 'vuex'

export default {

  name: 'MovieReview',
  components: { ReviewListForm, ReviewListItem },
  data() {
  return {
    moviePk: this.$route.params.moviePk,
  }
  },
  computed: {
      ...mapGetters(['isAuthor', 'movie']),
      reviews(){
        return this.movie.reviews
      }
  }
}

</script>

<style>

</style>