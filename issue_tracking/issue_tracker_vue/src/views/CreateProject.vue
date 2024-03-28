<template>
    <div class="create-project">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Create Project</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="">Project Title</label>
                        <div class="control">
                            <input type="text" class="input" v-model='name'>
                        </div>
                    </div>
                    <div class="field">
                        <label for="">Description</label>
                        <div class="control">
                            <textarea  class="textarea" placeholder="Description" v-model='description'></textarea>
                        </div>
                    </div>
                    <!-- <div class="field">
                        <select>Select User</select>
                        <option v-for="option in selecList"
                        v-bind:key="option.id">option.username</option>
                    </div> -->
                    <div class="field">
                        <div class="control">
                            <button class="button is-link">
                                Create
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    data(){
        return{
            name:'',
            description:'',
            submitter:{},
            errors : [],
            selecList:[],
        }
    },
    mounted(){
        this.retrieveUserList()
    },
    methods:{
        submitForm(){
            this.errors = []

            if(this.name ===''){
                this.errors.push('Project title is too short')
            }
            if(!this.errors.length){
                const formData = {
                    name:this.name,
                    description:this.description,
                    submitter: null
                }
                axios
                    .post('/api/v1/project/create/',formData)
                    .then(response =>{
                        console.log(formData)
                        this.$router.push("/projects/")//TODO:push works here, but not in case of delete

                    })
                    .catch(error =>{
                        if(error.response){
                            console.log(error.response)
                        }
                    })
            }
        },
        retrieveUserList(){
            axios
                .get('/api/v1/users/')
                .then(response=>{
                    this.selecList = response.data
                })
                .catch(error =>{
                    if(error.response){
                        console.log(error.response)
                    }
                })
        }
    }

}
</script>