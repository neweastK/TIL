<template>
  <div class=container>
    <div class='row col-4 ms-auto rounded' style='border: solid 1px black;'>
      <div>
        <b-avatar style="width: 70%; height: 100%;"></b-avatar>
      </div>
      <div>
        <h6 class='text-center'>{{ profile.nickname }}</h6>
        <h6>{{ profile.point ? profile.point : 0 }} point</h6>
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