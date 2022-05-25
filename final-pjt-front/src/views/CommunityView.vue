<template>
  <div>
    커뮤니티
    <router-link :to="{ name: 'event_article' }">이벤트</router-link> |
    <router-link :to="{ name: 'column_article' }">칼럼</router-link> |
    <router-link :to="{ name: 'news_article' }">뉴스</router-link> |
    <router-link :to="{ name: 'board_article' }">자유게시판</router-link> |
  </div>
</template>

<script>
export default {
  name: "CommunityView",

}
</script>

<style>

</style>