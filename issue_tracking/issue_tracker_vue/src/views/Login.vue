<template>
    <div class="is-flex is-justify-content-center is-flex-direction-row" :style="{'margin-top':'50px','width':'auto','height':'auto','margin-left':'400px'}">
                                <div class="is-flex is-flex-direction-column " :style="{'max-width':'400px','border-style':'solid','border-width':'1px','padding':'30px','border-color':'hsl(0, 0%, 48%)'}">
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

                                    <span :style="{'cursor':'pointer'}" @click="login_as_demo">No account? Click here to sign in as <span class="has-text-weight-bold">Demo User</span>.</span>
                                </form>
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
            demoUserFormData:{
            }
        }
    },
    mounted(){
        document.title = 'Log In | IT'
    },
    methods:{
        async login_as_demo(){
            this.username='demouser'
            this.password='Doom234?'
            await this.submitForm();
            
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
        async submitForm(){
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }
            await axios
                .post('/api/v1/login/', formData)
                .then(response =>{
                    const token = response.data.token
                    this.$store.commit('setToken',token)
                    axios.defaults.headers.common["Authorization"] = 'Token'+' '+token
                    localStorage.setItem('token', token)
                    this.getUser()
                    this.$router.push('/kanban')
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