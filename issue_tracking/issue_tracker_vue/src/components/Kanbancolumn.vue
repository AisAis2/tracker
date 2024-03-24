<template>
            <div class="column has-background-info-light mx-5" :style="{'height':'650px','overflow':'auto'}">
                <div class="is-flex is-family-monospace" :stlye="{'position':'sticky'}">
                    {{status}}({{ ticket_list.length }})
                    <a @click="$emit('initCreateTicket',status)"><span class="has-background-info-light"><i class="fa-solid fa-plus"></i></span></a>
                    
                </div>
                <div class="drop-zone" draggable="false">
                    <div class="drag-el" v-for="ticket in ticket_list" :key="ticket.id">
                            <ticketBoxVue :ticket="ticket" draggable=true @dragstart="startDrag($event,ticket)" @clicked="$emit('ticketClick',ticket.id)"/>
                    </div>
                </div>
        </div>
</template>



<script>
import ticketBoxVue from './ticketBox.vue'
export default {
    props:{
        ticket_list:{
            type: Array,
            default:[]
        },
        status:'',

    },
    components:{
        ticketBoxVue,
    },
    mounted(){
    },
    methods:{
 
        startDrag(evt, item) {
            if (item.status) {
                evt.dataTransfer.dropEffect = "move";
                evt.dataTransfer.effectAllowed = "move";
                evt.dataTransfer.setData("itemID", item.id);
            }
        },
        initCreate(status) {
            console.log(status);
            this.createTicket = true;
            this.createdTicket.status = status;
        },
        // clickedEmit(id){

        //     this.$emit('ticketClick',id)
        // }
    }
}
</script>