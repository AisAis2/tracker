<template >
    <div class="is-flex is-flex-direction-column" :style="{'font-family':'monospace'}" v-if="project.assignees">
        <div class="is-flex">
            <h1 class="title">{{project.name}}</h1>
        </div> 
        <div class="is-flex is-flex-direction-column my-5" :style="{'width':'350px'}">
            <label class="is-size-4 has-text-weight-semibold">Description<i class="fa-solid fa-pen-to-square is-size-5 mx-2" :style="{'cursor':'pointer'}" @click="edit_desc=!edit_desc"></i></label>
            <p v-if="project.description && !edit_desc" class="mt-2" >{{project.description}}</p>
            <textarea  class="textarea is-link" v-else-if="edit_desc" v-model="tmp_project.description"></textarea>
            <p v-else class="has-text-weight-light">Description is missing</p>
        </div>
        <div class="is-flex-directopm-column my-5">
            <label class="is-size-4 has-text-weight-semibold">Creator</label>
            <p v-if="project.submitter">{{project.submitter.username}}</p>
        </div>
        <div class="is-flex-directopm-column my-5">
            <label class="is-size-4 has-text-weight-semibold">Assignees</label>
            <p v-if="this.project.assignees.length>0">{{project.assignees[0].username}}</p>
            <p v-else>No Assignees</p>
        </div>

        <button class="button is-primary" :style="{'width':'200px'}">
            <router-link to="/projects">
            <span>Back to Projects</span></router-link>
        </button>
        <button class="button is-info" @click="editProject">
            edit
        </button>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'Project',
    data(){
        return{
            project:{},
            tickets:[],
            tmp_project:{},
            edit_desc:false,
            user:''
        }
    },
    async mounted(){
        await this.getProject()
    },
    computed:{
        assigness(){
            console.log(this.project.assigness==null)
            return ~this.project.assigness===null 
        }
    },
    methods:{
        async editProject(){
            const  id = this.$route.params.id
            this.user = {
                'email':'',
                'id':24,
                'username':'Aisultan3'
            }
            this.tmp_project.assignees=[this.user]
            await axios
                .put(`/api/v1/project/${id}/edit`,this.tmp_project)
                .then((response)=>{
                    console.log('success')
                    
                })
        },
        async  getProject(){

            const id = this.$route.params.id
            
             await axios
                .get(`/api/v1/project/${id}/`)
                .then(response => {
                    this.project = response.data
                    this.tmp_project = response.data
                    console.log(this.project)
                    console.log(Object.keys(this.project.assignees).length)
                    
                })
                .catch(error =>{
                    console.log(error)
                    
                })
        },
        async getTickets(){

            const id = this.$route.params.id
            await axios
                .get(`/api/v1/project/${id}/tickets/`)
                .then(response=>{
                    this.tickets=response.data
                    console.log(this.tickets)
                })
                .catch(error =>{
                    console.log(error)
                })
        },
        // async addUser(){

        //     await axios 
        //             .put('')
        // }
    }
}
</script>
