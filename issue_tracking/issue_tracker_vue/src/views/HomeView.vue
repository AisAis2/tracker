<template>
  <div class="home">
    <div class="is-flex is-flex-direction-row m-5">
      <div class="is-flex" :style="{'font-size':'200px','width':'300px','cursor':'pointer'}">
        <i class="fa-solid fa-user"></i>
      </div>
      <div class="is-flex" :style="{'font-size':'200px','width':'300px','cursor':'pointer'}">
        <i class="fa-solid fa-user-secret" @click="demoLogin(demoadmin)"></i>
      </div>
    </div>
    <div class="is-flex is-flex-direction-row m-5">
      <div class="is-flex" :style="{'font-size':'200px','width':'300px','cursor':'pointer'}">
        <i class="fa-solid fa-user-tie"></i>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HomeView',
  data(){
    return{
      demoadmin:{'token':'e793f6f10e7e59136d1df756867535332ab0d322'},
      demomanager:{},
      cuser:{}
    }
  },
  methods:{
    demoLogin(user){
            const token = user.token
            this.$store.commit('setToken',token)

            axios.defaults.headers.common["Authorization"] = 'Token'+' '+token
            localStorage.setItem('token', token)
            this.getUser()

            const toPath = this.$route.query.to || '/'
            this.$router.push(toPath)
            this.getPerms();
            this.getRole();    
    },        async getUser(){
            await axios
                .get('/api/v1/users/me')
                .then(response=>{
                    const user=response.data
                    this.$store.commit('setUser',user)

                })
                .catch(error=>{
                    console.log(error)
                })
        },
        async getPerms(){
            await axios
                .get('api/v1/group/perms')
                .then((response)=>{
                    console.log(typeof(response.data))
                    this.$store.commit('setPermsList',response.data)
                })
                .catch((error)=>{
            if(error.response){
                // console.log(error.response.data.detail);
                // console.log(error.response.status);
                // console.log(error.response.headers);
                this.$store.commit('newErrMsg',error.response.data.detail)
              }
              else if(error.request){
                console.log(error.request)
              }
              else{
                console.log('Error',error.message)
              }
              console.log(error.config)
          })
        }, 
        async getRole(){
      await axios
              .get('/api/v1/group/group')
              .then((response)=>{
                this.$store.commit('setRole',response.data)
   
              })
              .catch((error)=>{
            if(error.response){
                // console.log(error.response.data.detail);
                // console.log(error.response.status);
                // console.log(error.response.headers);
                this.deleteModal=false;
                this.$store.commit('newErrMsg',error.response.data.detail)
              }
              else if(error.request){
                console.log(error.request)
              }
              else{
                console.log('Error',error.message)
              }
              console.log(error.config)
          })
    },
        
  }
}
</script>
