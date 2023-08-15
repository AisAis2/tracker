<template>
    <div class="create_Ticket">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">
                    Create Ticket
                </h1>
                <form @submit.prevent="createTicket()">
                    <div class="field">
                        <label for="">Ticket Title</label>
                        <div class="control">
                            <input type="text" class="input" v-model='ticket.title'>
                        </div>
                    </div>

                    <div class="field">
                        <label for="">Ticket description</label>
                        <div class="control">
                            <textarea type="text" class="textarea" v-model='ticket.description'></textarea>
                        </div>
                    </div>
                    <button class="button is-primary">Create</button>
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
            ticket:{
            title:null,
            description:null,
            status:'Open',
            type:'Other Comments',
            priority:'Low',
            },
        }
    },
    methods:{
        createTicket(){
            axios
                .post('/api/v1/ticket/create/',this.ticket)
                .then(response =>{
                    this.$router.push('/tickets/')
                })
                .catch(error =>{
                    console.log(error)
                })
        }
    }
}
</script>