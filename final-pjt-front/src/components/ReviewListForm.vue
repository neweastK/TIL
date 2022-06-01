<template>
  <form @submit.prevent="onSubmit" class="review-list-form">
    <label for="rate">rate: </label>
    <input type="text" id="rate" v-model="rate" required>
    <label for="review">review: </label>
    <input type="text" id="review" v-model="content" required>
    <button>Review</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListForm',
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      content: '',
      rate: '',
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.moviePk, content: this.content, rate: this.rate })
      this.content = ''
      this.rate = ''
    }
  }
}
</script>

<style>

</style>