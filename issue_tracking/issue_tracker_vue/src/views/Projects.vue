<template>
    <div class="is-flex-direction-column " :style="{'font-family':'monospace'}">
        <nav class="breadcrumb mt-4 mx-6" aria-label="breadcrumbs">
            <ul>
                <li><a href="/">Home</a></li>
                <li class="is-active"><a href="#" aria-current="page">Projects</a></li>
            </ul>
        </nav>
        <h1 class="is-size-2 is-family-primary has-text-grey mx-6">Project List
            <i class="fa-solid fa-plus is-size-5 has-text-info" @click="createProject=!createProject" :style="{'cursor':'pointer','margin-top':'20px'}"></i>
        </h1>
        <div :style="{'width':'1300px','height':'520px'}">
            
            <table class="table" :style="{'width':'1300px'}">
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
                    v-bind:key="project.id" :style="{'height':'50px'}">
                        <td class="px-6"><router-link :to="{path:'/kanban/'}" @click="goKanban(project.name)">{{project.name}}</router-link></td>
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


        </div>
        <div class="is-flex">
                    <nav class="pagination mx-6 mt-5" role="navigation" aria-label="pagination">
                        <a class="pagination-previous" title="This is the first page"
                        :style="{'pointer-events': isDisabled}"
                        :class="{'is-disabled':isDisabled==='none'}"
                        @click="currentPage=currentPage-1,getProjectList()"
                        v-if="projectListLength!==1"
                        >Previous</a
                        >
                        <a href="#" class="pagination-next"
                        :style="{'pointer-events': isDisabled2}"
                        :class="{'is-disabled':isDisabled2==='none'}"
                        @click="currentPage=currentPage+1,getProjectList()"
                        v-if="projectListLength!==1"
                        >Next page</a>
                            <ul class="pagination-list">
                                    <li v-for="index in projectListLength" :key='index'>
                                        <a
                                        :class="{'pagination-link':true,  'is-current':currentPage==index}"
                                        aria-label="Page 1"
                                        aria-current="page"
                                        @click = "currentPage=index,getProjectList()"
                                        >{{ index }}</a
                                        >
                                    </li>

                            </ul>
                    </nav>
            </div>






    <div :class="{'is-active':isActive,'modal':true}" id='modal-ter' v-if="userList">
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

                <div class="is-flex-direction-column">

                <label class="has-text-weight-bold">Assignees</label>
                <br>
                <div class="select is-small is-multiple">
                    <select @click="pushToArr()" multiple size="4" v-model ="tmp_usr">
                        <option v-for="user in userList"
                        :key="user.username"
                        >{{ user.username }}</option>
                    </select>
                </div>
                <div class="is-flex-direction-row" v-if="assignees">
                    <div v-for="user in assignees" :key="user">{{ user }}</div>
                </div>


                </div>
            </section>
            <footer class="modal-card-foot">
                <button class="button is-success" @click='editProject(editedProject.id)'>Save</button>
                <button class="button" @click="isActive=false,editDesc=true,editName=true">Cancel</button>
            </footer>
        </div>
    </div>
    <createProjectVue
    :createNewProject="createProject"
    @projectCreated = "this.$router.go('/projects/')"
    />
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
import createProjectVue from '../components/createProject.vue';
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
            createProject:false,
            tmp_usr:[],
            lll:false,
            currentPage:1,
            projectListLength:''
            
        }
    },
    mounted(){
        this.getProjectList()
    },
    components:{
        createProjectVue,
    },
    computed:{

        assignees(){
            return []
        },
        userList(){
            return this.$store.state.user_list
        },
        isDisabled(){
                if(this.currentPage<=1){
                return 'none'
            }
            return 'auto'
        },
        isDisabled2(){
                if(this.currentPage>=this.projectListLength){
                return 'none'
            }
            return 'auto'


        }
    },
    methods:{
        pushToArr(){
            this.assignees.push(this.tmp_usr[0])//TODO add filters 
            this.lll=true
            console.log(this.assignees)
        },
        goKanban(pname){
            this.$store.commit('setPfilter',pname)
        },
        getProjectList(){
            axios
                .get('/api/v1/two_projects/',{
                    params:{
                        'page':this.currentPage,
                    }
                })
                .then(response => {
                    this.projectsList = response.data[0]
                    if(Number(response.data[1])%10===0){
                        this.projectListLength = Number(response.data[1])/10
                    }
                    else{
                        this.projectListLength = Math.floor(Number(response.data[1])/10)+1
                    }
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