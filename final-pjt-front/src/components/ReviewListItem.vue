<template>
  
  <li class="review-list-item">
    <router-link :to="{ name: 'profile', params: { username: review.user.nickname } }">
      {{ review.user.username }}
    </router-link>: 
    <span v-if="!isEditing">{{ payload.content }}</span>
    <span v-if="!isEditing">{{ review.rate }}</span>
    <div class='d-flex justify-content-end'>
        좋아요:
        <button
          @click="likeReview(payload)"
        >{{ likeReviewCount }}</button>
    </div>
    <span v-if="isEditing">
      <label for="rate">rate: </label>
      <input type="text" v-model="payload.rate">
      <label for="review">review: </label>
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteReview(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie.id,
        reviewPk: this.review.id,
        content: this.review.content,
        rate: this.review.rate
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    likeReviewCount() {
      return this.review.like?.length
    },
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview', 'likeReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload,)
      this.isEditing = false
    },
    // created(){
    //   // this.fetchReviews(this.review.movie.id)
    //   this.$store.getters('reviews')
    // }
  },

}
</script>

<style>

</style>