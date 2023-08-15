<template>
    <div class="ticket">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Ticket Title</h1>
                <p>{{ticket.title}}</p>
                <hr>
                <h1 class="title">Ticket description</h1>
                <p>{{ticket.description}}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            ticket:{},
        }
    },
    mounted(){
        this.getTicket()
    },
    methods:{
        getTicket(){
            const id = this.$route.params.id
            axios
                .get(`/api/v1/ticket/${id}`)
                .then(response =>{
                    this.ticket = response.data
                })
                .catch(error =>{
                    console.log(error)
                })
        }
    }
}
</script>