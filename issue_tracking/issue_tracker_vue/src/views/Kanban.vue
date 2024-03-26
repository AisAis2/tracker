<template>
  <div class="kanban columns is-multiline">
    <div class="column is-12 pl-5 is-flex-direction-column mx-3">
      <div class="is-family-monospace">Project Filter</div>
        <div class="select is-info">
            <select v-model='project_filter' @change = "filterTicketList()" class="is-family-monospace">
              <option >General</option>
              <option
              v-for='project in projectList'
              :key = 'project.name'
              :class="{'is-family-monospace':'true'}"
              >{{project.name}}</option>
            </select>
        </div>
        <span class="has-background-primary-light"><button class="button is-white" @click="createNewProject=!createNewProject"><i class="fa-solid fa-plus"></i></button></span>
    </div>
      <kanbancolumnVue
      v-for='(status,counter) in cols'
      :key =status
      :status="status" 
      :ticket_list="ll[counter]"
      @drop="onDrop($event,status)"
      @dragover.prevent 
      @dragenter.prevent 
      draggable="false"
      @ticketClick='clickedEmit'
      @initCreateTicket='initCreate'
      />


<!-- Delete Bin -->

    <!-- Update Modal -->
    <div :class="{ 'is-active': editTicket, modal: true}" id="modal-del">
      <div class="modal-background"></div>
      <div class="modal-card" >

        <header class="modal-card-head">
          <p class="modal-card-title">Edit Ticket</p>
          <button
            class="delete"
            aria-label="close"
            @click="editTicket = false"
          ></button>
        </header>

        <section class="modal-card-body">
          <div class="field pb-2">
            <label class="is-size-5 has-text-weight-bold">Title</label>
            <div class="control" v-if="!editTitle">
              {{ editedTicket.title }}
              <a @click="editTitle = !editTitle"
                ><i class="fa-solid fa-pen-to-square"></i
              ></a>
            </div>
            <div class="control" v-else>
              <input type="text" class="input" v-model="editedTicket.title" />
            </div>

            <div class="field py-5">
              <label class="is-size-5 has-text-weight-bold">Description</label>
              <div class="control" v-if="!editDesc">
                {{ editedTicket.description }}
                <a @click="editDesc = !editDesc"
                  ><i class="fa-solid fa-pen-to-square"></i
                ></a>
              </div>
              <div class="control" v-else>
                <textarea
                  class="textarea"
                  v-model="editedTicket.description"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="is-size-5 has-text-weight-bold">Type</label>
            <div class="control">
              <div class="select my-2 is-info is-rounded">
                <select v-if="!editedTicket.type" v-model="editedTicket.type">
                  <option v-for="select in selectList" :key="select">
                    {{ select }}
                  </option>
                </select>
                <select v-else v-model="editedTicket.type">
                  <option v-for="select in selectList" :key="select">
                    {{ select }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label class="is-size-5 has-text-weight-bold">Priority</label>
            <div class="control">
              <div class="select my-2 is-info is-rounded">
                <select
                  v-if="!editedTicket.priority"
                  v-model="editedTicket.priority"
                >
                  <option v-for="select in priorityList" :key="select">
                    {{ select }}
                  </option>
                </select>
                <select v-else v-model="editedTicket.priority">
                  <option v-for="select in priorityList" :key="select">
                    {{ select }}
                  </option>
                </select>
              </div>
            </div>
          </div>


          <div class="field">
            <label class="is-size-5 has-text-weight-bold">Project</label>
            <div class="control">
              <div class="select my-2 is-info is-rounded" >
                <select  v-model='ticketProject'>
                    <option v-if="editedTicket.project" value=''>{{editedTicket.project.name}}</option>
                    <option v-for="select in project_name_list" :key="select">
                      {{select}}
                    </option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="is-size-5 has-text-weight-bold">Submitter</label>
            <div class="control" v-if="editedTicket.submitter ">
              {{editedTicket.submitter.username}}
            </div>
          </div>

        </section>
        <footer class="modal-card-foot">
          <button class="button is-info" @click="toEditTicket(editedTicket)">
            Save
          </button>
          <button class="button" @click="editTicket = false">Cancel</button>
        </footer>
      </div>
    </div>
    <!-- Create Modal Ticket -->
    <div :class="{ 'is-active': createTicket, modal: true }" id="modal-tic">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Create Ticket</p>
          <button
            class="delete"
            aria-label="close"
            @click="createTicket = false"
          ></button>
        </header>

        <section class="modal-card-body">
          <div class="field">
            <label class="is-size-5 has-text-weight-bold">Title</label>
            <div class="control">
              <input type="text" class="input" v-model="createdTicket.title" />
            </div>
          </div>

          <div class="field">
            <label class="is-size-5 has-text-weight-bold">Description</label>
            <div class="control">
              <textarea
                type="text"
                class="textarea"
                v-model="createdTicket.description"
              ></textarea>
            </div>
          </div>
          <div class="field">
            <div class="select my-2 is-success is-rounded">
              <select v-model="createdTicket.priority">
                <option v-for="select in priorityList" :key="select">
                  {{ select }}
                </option>
              </select>
            </div>
          </div>



        </section>
        <footer class="modal-card-foot">
          <button class="button is-primary" @click="createTicketF()">
            Save
          </button>
          <button class="button" @click="createTicket = false">Cancel</button>
        </footer>
      </div>
    </div>


    <!-- Delete Modal -->
    <div :class="{ 'is-active': deleteModal, modal: true }" id="modal-tic" >
      <div class="modal-background"></div>
      <div class="modal-card" :style="{'width':'350px'}">
        <header class="modal-card-head">
          <p class="modal-card-title">Delete Ticket</p>
          <button
            class="delete"
            aria-label="close"
            @click="deleteModal = false"
          ></button>
        </header>

        <footer class="modal-card-foot">
          <button class="button is-danger" @click="deleteTicket()">
            Delete
          </button>
          <button class="button" @click="deleteModal = false">Cancel</button>
        </footer>
      </div>
    </div>
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
          <button class="button is-success" @click="createProject()">
            Create
          </button>
          <button class="button" @click="createNewProject = false">Cancel</button>
        </footer>
      </div>
    </div>
  </div>
  <a
      class="is-size-1 column is-12 pl-5"
      @drop="onDropDelete($event)"
      @dragover.prevent="binColor='red'"
      @dragleave.prevent="binColor='blue'"
      @dragenter.prevent
      :style="{'width':'100px','color':binColor}"
      ><i class="fa-solid fa-trash"></i
    ></a>
</template>


<script>
import axios from "axios";
import ticketBoxVue from "../components/ticketBox.vue";
import KanbancolumnVue from '../components/Kanbancolumn.vue';
export default {
  data() {
    return {
      ticketList: [],
      editTicket: false,
      editedTicket: {},
      selectList: ["Bugs/errors", "Feature Requests", "Other Comments"],
      priorityList: ["Low", "Medium", "High"],
      editTitle: false,
      editDesc: false,
      createTicket: false,
      createdTicket: { title: "", description: "", priority: "", status: "",submitter:""},
      deleteModal: false,
      deleted_id:'',
      cols:['Backlog','Open','In Progress','Done'],
      projectList:[],
      ticketProject:'',
      project_filter:'General',
      filtered_ticket_list:[],
      createNewProject:false,
      tmpProject:{'name':'','description':'','submitter':''},
      binColor:false,
    };
  },
  components: {
    ticketBoxVue,
    KanbancolumnVue,
  },
  mounted() {
    this.getTicketList(),
    this.getprojectList(),
    this.getPfilter()
  },
  computed: {
    ll(){
      return [this.list_backlog,this.list_open,this.list_ip,this.list_done]
    },
    list_backlog() {
      //filter for tickets which are in backlog
      return this.filtered_ticket_list.filter((item) => item.status === "Backlog");
    },
    list_open() {
      //filter for tickets which are open
      return this.filtered_ticket_list.filter((item) => item.status === "Open");
    },
    list_done() {
      //filter for tickets which are done
      return this.filtered_ticket_list.filter((item) => item.status === "Done");
    },
    list_ip() {
      //filter for tickets which are In Progress
      return this.filtered_ticket_list.filter((item) => item.status === "In Progress");
    },
    notNull(smth) {
      return smth != null;
    },
    project_name_list(){
      const p = [];
      for(let i = 0;i<this.projectList.length;i++){
        if(!this.editedTicket.project){
           p.push(this.projectList[i].name)
        } else if(this.editedTicket.project.name!=this.projectList[i].name){
             p.push(this.projectList[i].name)
        }
      };
      return p;
    }
  },
  methods: {
  
      async createProject(){
        this.tmpProject.submitter = JSON.parse(localStorage.getItem('user'))
        await axios
                  .post('api/v1/project/create/',this.tmpProject)
                  .then((response)=>{
                    console.log(response)
                    this.$router.go('/kanban')
                  })
                  .catch((error)=>{
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
                  this.tmpProject.title=''
                  this.tmpProject.description=''
                  this.tmpProject.submitter=''
                  this.createNewProject=false
      },          
    getPfilter(){
      if(localStorage.getItem('project_filter')===null){
        this.project_filter = this.$store.state.project_filter
      }
      else{
        this.project_filter = localStorage.getItem('project_filter')
      }
      
    },
    clickedEmit(id) {
      id= Number(id)
      this.editTicket = true;
      this.editedTicket = this.ticketList.find((x) => x.id === id);
      console.log(this.editedTicket)
    },
    async getTicketList() {
      await axios
                .get("/api/v1/ticket/all/")
                .then((response) => {
                  this.ticketList = response.data;
                })
                .catch((error)=>{
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
                });
            this.filterTicketList();
    },
    filterTicketList(){
      if(this.project_filter!='General'){
        this.filtered_ticket_list = this.ticketList.filter((ticket)=>ticket.project!=null && ticket.project.name===this.project_filter)
      } else if(this.project_filter ==='General'){
        this.filtered_ticket_list = this.ticketList.filter((ticket)=>ticket.project===null)
      }
      localStorage.setItem('project_filter',this.project_filter)
    },
    startDrag(evt, item) {
      if (item.status) {
        evt.dataTransfer.dropEffect = "move";
        evt.dataTransfer.effectAllowed = "move";
        evt.dataTransfer.setData("itemID", item.id);
      }
    },
    onDrop(evt, status) {
      const itemID = Number(evt.dataTransfer.getData("itemID"));
      const item = this.ticketList.find((x) => x.id === itemID);
      try {
        if (item.status) {
          item.status = status;
          axios
            .put(`/api/v1/ticket/${item.id}/update`, item)
            .then((response) => {
              console.log(response.data)
            });
        }
      } catch (error) {
        console.error(error);
      }
    },
    async toEditTicket(ticket) {
      const pp = this.projectList.find((p)=>p.name===this.ticketProject)
      ticket.project = pp
      console.log(ticket)
      await axios
        .put(`/api/v1/ticket/${ticket.id}/update`, ticket)
        .then((response) => {
          console.log(response);
          this.editTicket = false;
        })
        .catch((error)=>{
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
         
        });
      this.editTitle = false;
      this.editDesc = false;
      this.editedTicket ={};
      this.getTicketList();
      this.ticketProject='';
       this.$router.push("/kanban");
      },



    async createTicketF() {
      this.createdTicket.project = this.projectList.find((p)=>p.name===this.project_filter)
      this.createdTicket.submitter=JSON.parse(localStorage.getItem('user'))
      
      await axios
        .post(`/api/v1/ticket/create/`, this.createdTicket) //clear fields in created ticket after done
        .then((response) => {
          console.log(response);
          this.createTicket = false;
          this.$router.go("/kanban");

        })
        .catch((error)=>{
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
        });
      this.createTicket=false

      // for(const key of Object.entries(this.createdTicket)){
      //     key=''
      // }
    },
    initCreate(status) {
      
      this.createTicket = true;
      this.createdTicket.status = status;
    },
    onDropDelete(event) {
      this.binColor='blue'
      this.deleted_id = Number(event.dataTransfer.getData("itemID"));
      this.deleteModal = true;
    },

    deleteTicket() {
        axios
            .delete(`/api/v1/ticket/${this.deleted_id}/delete`)
            .then(response=>{
                console.log(response)
                this.$router.go('/kanban')
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
    },
    async getprojectList(){
       await axios
          .get('/api/v1/two_projects/')
          .then(response=>{
              this.projectList=response.data
          })
          .catch((error)=>{
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
    }
  },
};
</script>


