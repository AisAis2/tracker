<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>
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
                    <div class="field">
                        <label for="">Repeat password</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password2">
                            </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for= "error in errors" v-bind:key="error">
                            {{error}}
                        </p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Sign up</button>
                        </div>
                    </div>


                    <hr>

                    Or <router-link to="/login">click here</router-link> to log in
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: "SignUp",
    data(){
        return{
            username:'',
            password:'',
            password2:'',
            errors:[]
        }
    },
    methods:{
        submitForm(){
            this.errors = []//reset if sent multiple times
            if(this.username ===''){
                this.errors.push('The username is missing')
            }
            if(this.password ===''){
                this.errors.push('The password is too short')
            }
            if(this.password !==this.password2){
                this.errors.push('Passwords do not match')
            }
            if(!this.errors.length){//no errors, it means we can fill in formdata and send it to backend
                const formData = {
                    username: this.username,
                    password: this.password,
                }
                axios
                    .post('/api/v1/users/',formData)//sending data to available endpoint
                    .then(response =>{
                        this.$router.push('/login')//redirect to log in page    
                        }
                    )
                    .catch(error =>{
                        if(error.response){

                        }
                    })
            }
        }
    }
}
</script>