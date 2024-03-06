<template>
    <div class="users">
        <div 
        v-for="user in usersList"
        :key=user.name
        >
        {{user.username}}</div>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    data(){
        return{
            usersList:[]
        }
    },
    mounted(){
        this.getUserList()
    },
    methods:{
        async getUserList(){
            await axios
                .get('/api/v1/users/')
                .then(response=>{
                    this.usersList=response.data
                })
                .catch(errors=>{
                    console.log(errors)
                    console.log(axios.defaults.headers)

                })
        }
    }
}
</script>