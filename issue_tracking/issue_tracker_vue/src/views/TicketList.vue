<template>
<div class="is-flex is-flex-direction-column">
    <div :style="{'height':'500px'}">
    <table class="table is-fullwidth">
        <thead>
            <tr>
                <th class="px-6 is-family-monospace">Title</th>
                <th class="px-6 is-family-monospace">Creator</th>
                <th class="px-6 is-family-monospace">Project</th>
                <th class="px-6 is-family-monospace">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(ticket,index) in ticketList"
            v-bind:key="ticket.id" :style="{'height':'50px'}">
                <td class="px-6 is-family-monospace"><router-link :to="{path:'/ticket/'+ticket.id}">{{ticket.title}}</router-link></td>
                <td class="px-6 is-family-monospace" v-if="ticket.submitter">{{ticket.submitter.username}}</td>
                <td class="px-6 is-family-monospace" v-else>Admin</td>
                <td class="px-6 is-family-monospace" v-if='ticket.project'>{{ticket.project.name}}</td>
                <td class="px-6 is-family-monospace" v-else></td>
                <td class="px-6">
                    <button class="button is-outlined is-small is-info mr-2 is-family-monospace" data-target="modal-ter" aria-haspopup='true' @click='initEditticket(index)'>
                        Edit 
                    </button>
                    <button class="button is-outlined is-small is-danger is-family-monospace" data-target="modal-del" aria-haspopup='true' @click='initDeleteticket(project.id)'>
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
    <nav class="pagination mx-6 mt-3" role="navigation" aria-label="pagination">
  <a class="pagination-previous is-disabled" title="This is the first page"
    >Previous</a
  >
  <a href="#" class="pagination-next">Next page</a>

  <ul class="pagination-list">
    <li  v-for="index in totalLength" :key="index">
      <a
        :class="{'pagination-link':true,  'is-current':currentPage==index}"
        aria-label="Page 1"
        aria-current="page"
        @click="currentPage=index,getTicketList()"
        >{{ index }}</a
      >
    </li>
  </ul>
</nav>

</div>
</div>

    
</template>


<script>
import axios from 'axios'
export default {
    data(){
        return{
         ticketList:[],
         totalLength:'',
         currentPage:1,
        }
    },
    mounted(){
        this.getTicketList()
    },

    methods:{
        async getTicketList() {

                await axios
                .get("/api/v1/ticket/all/",{params:{'page':this.currentPage}})
                .then((response) => {
                    this.ticketList = response.data[0];
                    if(Number(response.data[1])%10===0){
                        this.totalLength = Number(response.data[1])/10
                    }
                    else{
                        this.totalLength = Math.floor(Number(response.data[1])/10)+1
                    }

                    });
                
        }
    }
}
</script>



