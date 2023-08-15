<template>
<div class="box is-flex">
    <div class="tickets">
    <table class="table">
        <thead>
            <tr>
                <th class="px-6">Title</th>
                <th class="px-6">Creator</th>
                <th class="px-6">Project</th>
                <th class="px-6">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(ticket,index) in ticketList"
            v-bind:key="ticket.id">
                <td class="px-6"><router-link :to="{path:'/ticket/'+ticket.id}">{{ticket.title}}</router-link></td>
                <td class="px-6">Creator</td>
                <td class="px-6" v-if='ticket.project'>{{ticket.project.name}}</td>
                <td class="px-6" v-else></td>
                <td class="px-6">
                    <button class="button is-outlined is-small is-info mr-2" data-target="modal-ter" aria-haspopup='true' @click='initEditticket(index)'>
                        Edit 
                    </button>
                    <button class="button is-outlined is-small is-danger" data-target="modal-del" aria-haspopup='true' @click='initDeleteticket(project.id)'>
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

</div>
    
</template>


<script>
import axios from 'axios'
export default {
    data(){
        return{
         ticketList:[],
        }
    },
    mounted(){
        this.getTicketList()
    },

    methods:{
        async getTicketList() {
                await axios
                .get("/api/v1/ticket/all/")
                .then((response) => {
                    this.ticketList = response.data;
                    console.log('sucess')
                    });
                
        }
    }
}
</script>



