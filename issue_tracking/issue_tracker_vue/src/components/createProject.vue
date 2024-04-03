<template>
    <!-- Create Project Modal -->
    <div :class="{ 'is-active': createNewProject, modal: true }" id="modal-tic">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title is-family-monospace">Create Project</p>
          <button
            class="delete"
            aria-label="close"
            @click="createNewProject = false"
          ></button>
        </header>
        <section class="modal-card-body">
          <div class="field">
            <div class="my-2 is-success is-rounded">
              <label class="is-size-5 has-text-weight-bold">Title</label>
              <div class="control">
                <input type="text" class="input" v-model='tmpProject.name'>
              </div>

            </div>
          </div>
          <div class="field">
            <div class="my-2 is-success is-rounded">
              <label class="is-size-5 has-text-weight-bold">Description</label>
              <div class="control">
                <textarea type="text" class="textarea" v-model='tmpProject.description'></textarea>
              </div>
              
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-link" @click="createProject()">
            Create
          </button>
          <button class="button" @click="createNewProject = false">Cancel</button>
        </footer>
      </div>
    </div>


</template>
<script>
import axios from 'axios'

export default{
    data(){
        return{
            tmpProject:{'name':'','description':'','submitter':'','assignees':''},
            createNewProject:false
        }
    },
    props:{
        createNewProject: {
            type:Boolean,
        }
    },
    methods:{
      async createProject(){
        this.tmpProject.submitter = JSON.parse(localStorage.getItem('user'))
        this.tmpProject.assignees = []
        await axios
                  .post('api/v1/project/create/',this.tmpProject)
                  .then((response)=>{
                      this.tmpProject.title=''
                      this.tmpProject.description=''
                      this.tmpProject.submitter=''
                  })
                  .catch((error)=>{
                    if(error.response){
                // console.log(error.response.data.detail);
                // console.log(error.response.status);
                // console.log(error.response.headers);
                        this.$store.commit('newErrMsg',error.response.data.detail)
                    }
                    else if(error.request){
                        console.log(error.request)
                    }
                    else{
                        console.log('Error',error.message)
                    }
                    

                    console.log(error.config)})
                    
      },    
    }
}
</script>