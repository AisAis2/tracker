<template>
    <div class="single_project">
        <div class="columns">
            <div class="column">
                        <h1 class="title">{{project.name}}</h1>
                        <label class="is-size-4 has-text-weight-semibold">Description</label>
                        <p v-if="project.description" class="py-5">{{project.description}}s</p>
                        <p v-else class="py-5 has-text-weight-light">Description is missing</p>
                        <button class="button is-primary">
                            <router-link to="/projects">
                            <span>Back to Projects</span></router-link>
                        </button>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Tilte</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="ticket in tickets"
                                v-bind:key='ticket.id'>
                                    <th>{{ticket.title}}</th>
                                    <th>{{ticket.description}}</th>
                                </tr>
                            </tbody>
                        </table>
            </div>
        </div>

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
        }
    },
    beforeMount(){  
        this.getTickets()
    },
    methods:{
        async getProject(){

            const id = this.$route.params.id
            
            await axios
                .get(`/api/v1/project/${id}`)
                .then(response => {
                    console.log('project')
                    this.project = response.data
                    console.log(this.project)

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
        }
    }
}
</script>