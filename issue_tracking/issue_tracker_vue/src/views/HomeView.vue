<template>
  <div class="is-flex is-justify-content-center is-family-monospace">

    <div class="box mt-6" :style="{'width':'700px','height':'700px','border-style':'dotted'}">
      <div class="is-flex">
            <div class="is-flex-direction-column m-5">
              <div class="is-flex " :style="{'font-size':'200px','width':'300px','cursor':'pointer'}">
              <i class="fa-solid fa-user" @click="submitForm(cuser)"></i>
            </div>

                <p class="is-size-3">Demo User</p>
            </div>
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
      cuser:{'username':'demouser','password':'Diablo234?'},
      errors:[]
    }
  },
    methods:{
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
        async getPerms(){
            await axios
                .get('api/v1/group/perms')
                .then((response)=>{
                    this.$store.commit('setPermsList',response.data)
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
        async submitForm(user){
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            const formData = {
                username: user.username,
                password: user.password
            }
            await axios
                .post('/api/v1/login/', formData)
                .then(response =>{
                    const token = response.data.token
                    this.$store.commit('setToken',token)

                    axios.defaults.headers.common["Authorization"] = 'Token'+' '+token
                    localStorage.setItem('token', token)
                    this.getUser()

                    const toPath = this.$route.query.to || '/kanban'
                    this.$router.push(toPath)
                    this.getPerms();
                    this.getRole();


                })
                .catch(error =>{
                    if(error.response){
                        for(const property in error.response.data){
                            this.errors.push(`${error.response.data[property]}`)
                            console.log(`${error.response.data[property]}`)
                        } 
                    } else {
                            this.errors.push('Something went wrong. Please try again')
                            console.log(JSON.stringify(error))
                        }
                    setTimeout(()=>{this.errors=[]},3000)
                })
        },
        async getUser(){
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

    }
}
</script>
