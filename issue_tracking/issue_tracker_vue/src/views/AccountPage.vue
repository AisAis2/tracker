<template>
        <div class="is-flex  is-family-monospace">
            <div :style="{'width':'600px'}">

            </div>
            <div class="is-flex-direction-column " :style="{'width':'600px'}">
                <div class="field">
                    <label for="" class="label  is-size-4">Name</label>
                    <div class="control  is-size-5">{{ user.username }}</div>
                </div>
                <div class="field">
                    <label for="" class="label  is-size-4">Email</label>
                    <div class="control  is-size-5" v-if="user.email">{{ user.email }}</div>
                    <div class="control  is-size-5" v-else>{{ user.username }}@tracker.com</div>
                </div>
                <div class="field">
                    <div class="control"><button class="button is-danger is-family-monospace is-size-6" @click='logout()'>Log Out</button></div>
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
            localStorage.removeItem('user_list')
            localStorage.removeItem('project_filter')
            localStorage.removeItem('perms_list')

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