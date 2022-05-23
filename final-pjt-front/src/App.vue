<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'index' }">MOVIE</router-link> |
      <router-link :to="{ name: 'sinyema' }">SINYEMA</router-link> |
      <router-link :to="{ name: 'community' }">COMMUNITY</router-link> |
      <router-link :to="{ name: 'mypage' }">MyPage</router-link>

    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
