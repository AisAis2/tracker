<template>
    <div class="projects" :style="{'font-family':'monospace'}">
    <h1 class="is-size-2 is-family-primary has-text-grey mx-6">Project List</h1>
    <table class="table is-fullwidth">
        <thead>
            <tr>
                <th class="px-6">Project Name</th>
                <th class="px-6">Creator</th>
                <th class="px-6">Member</th>
                <th class="px-6">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(project,index) in projectsList"
            v-bind:key="project.id">
                <td class="px-6"><router-link :to="{path:'/project/'+project.id}">{{project.name}}</router-link></td>
                <td class="px-6" v-if="!project.submitter">Creator</td>

                <td class="px-6" v-else>{{project.submitter.username}}</td>
                <td class="px-6">Member</td>
                <td class="px-6">
                    <button class="button is-outlined is-small is-info mr-2 has-text-weight-bold" data-target="modal-ter" aria-haspopup='true' @click="this.$store.dispatch('checkPerms',['change_project',initEditProject,'You have no permission to edit project(s).',index])">
                        Edit 
                    </button>
                    <button class="button is-outlined is-small is-danger has-text-weight-bold" data-target="modal-del" aria-haspopup='true' @click="this.$store.dispatch('checkPerms',['delete_project',initDeleteProject,'You have no permission to delete project(s).',project.id])">
                            <span>Delete</span>
                                <span class="icon is-small">
                                    <i class="fas fa-times"></i>
                                </span>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>







    <div :class="{'is-active':isActive,'modal':true}" id='modal-ter'>
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Edit Project</p>
                <button class="delete" aria-label="close" @click="isActive=false,editDesc=true,editName=true"></button>
            </header>
            <section class="modal-card-body">
                <label class="has-text-weight-bold">Project Name</label>
                <p v-if='editName'><span class="mr-5">{{editedProject.name}}</span><a @click='editName=!editName'><i class="fa-solid fa-pen-to-square"></i></a></p>
                <p v-else><input type="text" v-model='editedProject.name' class="input"></p>
                <hr>
                <label class="has-text-weight-bold">Project Description</label> 
                <p v-if='editDesc'><span class="mr-5">{{editedProject.description}}</span><a @click="editDesc=!editDesc"><i :class="{'fa-solid':true,'fa-pen-to-square':true,'pointer-events':'fill'}"></i></a></p>
                <p v-else><textarea v-model='editedProject.description' class="textarea"></textarea></p>
            </section>
            <footer class="modal-card-foot">
                <button class="button is-success" @click='editProject(editedProject.id)'>Save</button>
                <button class="button" @click="isActive=false,editDesc=true,editName=true">Cancel</button>
            </footer>
        </div>
    </div>
    
    <div :class="{'is-active':isActiveDelete,'modal':true}" id='modal-del'>
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Delete Project</p>
                <button class="delete" aria-label="close" @click="isActiveDelete=false"></button>
            </header>
            

            <footer class="modal-card-foot">
                <button class="button is-danger" @click="deleteProject()">Delete</button>
                <button class="button" @click="isActiveDelete=false">Cancel</button>
            </footer>
        </div>

    </div>






</div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'Projects',
    data(){
        return {
            projectsList:[],
            isActive:false,
            editedProject:{},
            isActiveDelete:false,
            id_id:'',
            editDesc:true,
            editName:true,
        }
    },
    mounted(){
        this.getProjectList()
    },

    methods:{
        getProjectList(){
            axios
                .get('/api/v1/two_projects/')
                .then(response => {
                    this.projectsList = response.data
                })
                .catch(error =>{
                    console.log(error)
                })
        },
        initEditProject(key){
            this.isActive=!this.isActive
            this.editedProject=this.projectsList[key]
            console.log(this.editedProject)
        },
        initDeleteProject(id){
            this.isActiveDelete = !this.isActiveDelete
            this.id_id=id
        },
        deleteProject(){
            const id=this.id_id
            axios
                .delete(`/api/v1/project/${id}/delete`)
                .then(response =>{
                    // this.$router.push({path:'/projects/'})
                    this.$router.go('/projects/')
                    console.log(response)
                })
                .catch(error=>{
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
                this.isActiveDelete=false;
        },
        editProject(id){
            const ids = id
            axios
                .put(`/api/v1/project/${ids}/edit`,this.editedProject)
                .then(response =>{
                    this.$router.go('/projects/')
                })
                .catch(error=>{
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
            this.isActive=false;
        }
        
    }
}
</script>