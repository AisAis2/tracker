<template>
    <div class="log-in">
            <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4" :style="{'width':'600px'}">
                <h1 class="title">Log in</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="">Username</label>
                            <div class="control">
                                <input type="text" class="input" v-model="username">
                            </div>
                    </div>
                    <div class="field">
                        <label for="">Password</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password">
                            </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for= "error in errors" v-bind:key="error">
                            {{error}}
                        </p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Login</button>
                        </div>
                    </div>


                    <hr>

                    No account? <router-link to="/signup">Click here</router-link> to sign up.
                </form>
            </div>
        </div>
    </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'Login',
    data(){
        return{
            username:'',
            password:'',
            errors:[],
        }
    },
    mounted(){
        document.title = 'Log In | IT'
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
                    console.log(typeof(response.data))
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
        async submitForm(){
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            const formData = {
                username: this.username,
                password: this.password
            }
            await axios
                .post('/api/v1/token/login/', formData)
                .then(response =>{
                    const token = response.data.auth_token
                    this.$store.commit('setToken',token)

                    axios.defaults.headers.common["Authorization"] = 'Token'+' '+token
                    localStorage.setItem('token', token)
                    this.getUser()

                    const toPath = this.$route.query.to || '/'
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