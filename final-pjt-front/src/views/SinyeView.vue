<template>
  <div>

    <router-link :to="{ name: 'sinyenew' }">NEW</router-link>
    <ul>

      <li v-for="article in sinye_article" :key="article.pk">
        {{ article.user.nickname }} :
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>

      </li>
    </ul>
  </div>
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: "SinyeView",
    computed: {
      ...mapGetters(['sinye_article'])
    },
    methods: {
      ...mapActions(['fetchSinye'])
    },
    created() {
      this.fetchSinye()
    },

  }
</script>

<style>

</style>