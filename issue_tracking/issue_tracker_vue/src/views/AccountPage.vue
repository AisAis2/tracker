<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
            </div>
            <div class="column is-12">
                <label class="is-size-4 has-text-weight-bold">Username</label>
                <div class="is-size-5">{{user.username}}</div>
            </div>
            <div class="column is-12">
                <label class="is-size-4 has-text-weight-bold">Email</label>
                <div class="is-size-5" v-if="user.email">{{user.email}}</div>
                <div class="is-size-5" v-else>No Email</div>
            </div>
            <!-- <div class="column is-12">
                <label class="is-size-4 has-text-weight-bold">Role</label>
                <div class="is-size-5">{{user.username}}</div>
            </div> -->
            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
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