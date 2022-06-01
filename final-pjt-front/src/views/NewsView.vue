<template>
   <div class="container">
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link "  href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'event_article' }">이벤트</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link "  href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'column_article' }">칼럼</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#"><router-link class="fw-bold text-decoration-none" style="color:navy;" :to="{ name: 'news_article' }">뉴스</router-link></a>
      </li>
      <li class="nav-item">
        <a class="nav-link "  href="#"><router-link class="fw-bold text-decoration-none" style="color:gray;" :to="{ name: 'board_article' }">자유게시판</router-link></a>
      </li>
    </ul>

      <table class="table table-hover">
        <thead class="table-light">
        <tr>
          <th scope="col-11">제목</th>
          <th scope="col-1">작성자</th>
        </tr>
        </thead>
        <tbody>
          <tr v-for="article in news_article" :key="article.pk">
            <td>
              <router-link class="text-decoration-none" style="color:black;" 
                :to="{ name: 'article', params: {articlePk: article.pk} }">
                {{ article.title }}
              </router-link>
              <!-- <span class="badge bg-primary rounded-pill">{{ article.comment_count }}</span>               -->
            </td>
            <td>
              {{ article.user.nickname }}
            </td>
          </tr>
        </tbody>


      </table>

      
      <div class="d-grid gap-2 d-md-flex justify-content-md-end">
        <button class="btn" style="background-color: MidnightBlue;" type="button"><router-link :to="{ name: 'newsnew' }" class="text-decoration-none" style="color:white;">글쓰기</router-link></button>
      </div>

      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
          <li class="page-item disabled">
            <a class="page-link">Prev</a>
          </li>
          <li class="page-item"><a class="page-link" style="color:DarkOrange;" href="#">1</a></li>
 
          <li class="page-item disabled">
            <a class="page-link" href="#">Next</a>
          </li>
        </ul>
      </nav>

  </div>
  
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
      name: "NewsView",
      computed: {
        ...mapGetters(['news_article'])
      },
      methods: {
        ...mapActions(['fetchNews'])
      },
      created() {
        this.fetchNews()
    },
  }
</script>

<style>

</style>