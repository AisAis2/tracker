<template>
    <div class="page-my-account">
        <div class="is-flex is-justify-content-center">
            <div class="box" :style="{'width':'400px'}">
                <div class="field">
                    <label for="" class="label">Name</label>
                    <div class="control">{{ user.username }}</div>
                </div>
                <div class="field">
                    <label for="" class="label">Email</label>
                    <div class="control" v-if="user.email">{{ user.email }}</div>
                    <div class="control" v-else>{{ user.username }}@tracker.com</div>
                </div>
                <div class="field">
                    <div class="contro"><button class="button is-danger" @click='logout()'>Log Out</button></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {

    name:'AccountPage',
    data(){
        return{
            user:'',
        }
    },
    methods:{
        logout(){

            axios.defaults.headers.common["Authorization"] = 'Token '+this.$store.state.token
            axios
            .post('/api/v1/token/logout/',this.$store.state.token)
            .catch(error=>{
                console.log(error)
            })
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')
            this.$store.commit('removeUser')
            this.$router.push('/')

        },
        getUserStore(){
            this.user=JSON.parse(localStorage.getItem('user'))
        }
    },
    mounted(){
        this.getUserStore()
    }
}
</script>