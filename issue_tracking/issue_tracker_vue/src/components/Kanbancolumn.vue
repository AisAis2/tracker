<template>
    <div class="is-flex is-flex-direction-column" :style="{'margin-inline':'5px'}">
            <div class="is-flex is-flex-direction-column" :style="{'height':'650px','width':'285px','overflow-y':'auto','overflow-x':'hidden','border-style':'solid','border-width':'1px','border-radius':'1px'}" >
                    <div class="is-flex is-size-6 is-uppercase has-text-weight-semibold" :style="{'margin-left':'10px','margin-top':'10px'}">
                            <span :style="{'width':'50%'}">{{status}}({{ ticket_list.length }})</span>
                            <a @click="$emit('initCreateTicket',status)" :style="{'margin-left':'35%'}"><span><i class="fa-solid fa-plus"></i></span></a>
                    </div>
                <div class="drop-zone" draggable="false">
                    <div class="drag-el" v-for="ticket in ticket_list" :key="ticket.id">
                            <ticketBoxVue :ticket="ticket" :project='project'
                            draggable=true @dragstart="startDrag($event,ticket)" @clicked="$emit('ticketClick',ticket.id)"/>
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
            default:[],
        },
        project:String,
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
            this.createTicket = true;
            this.createdTicket.status = status;
        },
        // clickedEmit(id){

        //     this.$emit('ticketClick',id)
        // }
    }
}
</script>