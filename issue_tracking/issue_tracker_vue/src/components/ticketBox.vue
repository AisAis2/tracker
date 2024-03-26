<template>
    <div :class="{'box':true, 'm-3':true, bgColor:true }" :style="{'height':'110px','overflow':'hidden'}" >
        <div class="is-flex is-flex-direction-column ">
            <div class="is-flex is-flex-direction-row" :style="{'height':'50px','overflow':'hidden'}">
                <div class="is-flex" :style="{'width':'200px'}">
                    <span class="is-size-6 has-text-weight-semibold is-align-content-center is-clipped is-family-monospace">{{ticket.title}}</span>
                </div>
                    <div class="is-flex ml-5">
                        <a  @click="this.$store.dispatch('checkPerms',['change_ticket',emitClick,'You have no permission to edit ticket(s).'])"><span class=" is-size-7"><i class="fa-solid fa-square-plus"></i></span></a>
                    </div>
            </div>
            <div class="is-flex is-flex-direction-row ">
                <span class="is-size-7 has-text-weight-bold is-family-monospace" :class="{'has-text-danger':textColor()[0],'has-text-warning':textColor()[1],'has-text-info':textColor()[2]}"
               >
                    {{ ticket.priority }}
                </span>
            </div>
        </div>
    </div>
</template>



<script>
export default {
    name:"TicketBox",
    data(){
        return{
            background_colors:{'Low':'has-background-primary','Medium':'has-background-info','High':'has-background-danger'}
        }

    },
    computed:{
        bgColor(){
            return 'has-background-primary'//this.background_colors[this.ticket.priority]
        }
    },
    props:{
        ticket:Object
    },

    methods:{
        emitClick(){
            this.$emit('clicked',true)
        },
        textColor(){//didnt work
            if(this.ticket.priority ==='High'){
                return [true,false,false]
            }
            else if(this.ticket.priority ==='Medium'){
                return [false,true,false]
            }
            else{
                return [false,false,true]
            }
        }
    },
}
</script>