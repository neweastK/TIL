<template>
  <div>
    <b-modal v-model="modalBoolean">Hello From Modal!</b-modal>
  </div>
</template>

<script>
export default {
  name: "MovieModal",
  props : {
    mbutton : Boolean
  },
  data(){
    return {
      modalBoolean : (this.mbutton ? true : false) 
    }
  }
}
</script>

<style>

</style>