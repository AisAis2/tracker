<template>
  <div class="home">
    <div class="is-flex is-flex-direction-row m-5">
      <div class="is-flex" :style="{'font-size':'200px','width':'300px'}">
        <i class="fa-solid fa-user"></i>
      </div>
      <div class="is-flex" :style="{'font-size':'200px','width':'300px'}">
        <i class="fa-solid fa-user-secret"></i>
      </div>
    </div>
    <div class="is-flex is-flex-direction-row m-5">
      <div class="is-flex" :style="{'font-size':'200px','width':'300px'}">
        <i class="fa-solid fa-user-tie"></i>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data(){
    return{

    }
  },
  mounted(){
    console.log('mounted')
  }
}
</script>
