<template>
  <div>
    <div class='container' style='border: solid 1px black;'>
      <div class='row'>
        <b-avatar class='d-flex' src="https://placekitten.com/300/300" size="6rem"></b-avatar>
        {{ profile.nickname }}<br>
        {{ profile.point ? profile.point : 0 }} point
      </div>
    </div>
    
    
  </div>

  
</template>

<script>
// import { mapGetters } from 'vuex'
export default {
  name: 'ProfileView',
  props: {
    profile:Object
  }}

</script>

<style>

</style>