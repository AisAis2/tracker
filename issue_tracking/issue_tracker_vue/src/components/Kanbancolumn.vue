<template>
    <div class="column is-3">
            <div class="is-flex is-family-monospace has-text-weight-bold mx-5 mb-2" >
                    {{status}}({{ ticket_list.length }})
                    <a @click="$emit('initCreateTicket',status)"><span><i class="fa-solid fa-plus"></i></span></a>
            </div>
            <div class="is-flex mx-5" :style="{'height':'650px','width':'320px','overflow':'auto','box-shadow':'1px 1px'}" >
                <div class="drop-zone" draggable="false">
                    <div class="drag-el" v-for="ticket in ticket_list" :key="ticket.id">
                            <ticketBoxVue :ticket="ticket" draggable=true @dragstart="startDrag($event,ticket)" @clicked="$emit('ticketClick',ticket.id)"/>
                    </div>
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