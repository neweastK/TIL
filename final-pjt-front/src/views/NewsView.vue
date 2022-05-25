<template>
  <div>
    뉴스
    <router-link :to="{ name: 'event' }">이벤트</router-link> |
    <router-link :to="{ name: 'column' }">칼럼</router-link> |
    <router-link :to="{ name: 'news' }">뉴스</router-link> |
    <router-link :to="{ name: 'board' }">자유게시판</router-link> |
  </div>
  
</template>

<script>
export default {
    name: "NewsView",
}
</script>

<style>

</style>