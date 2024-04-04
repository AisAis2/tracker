<template>
    <div :class="{'box':true, 'my-5':true,'mx-4':true, bgColor:true,'is-family-monospace':true  }" :style="{'height':'130px','overflow':'hidden','border':'solid','box-shadow':'1px 1px','border-width':'1px'}" >
        <div class="is-flex is-flex-direction-column ">
            <div class="is-flex is-flex-direction-row" :style="{'height':'40px','overflow':'hidden'}">
                <div class="is-flex" :style="{'width':'200px'}">
                    <span class="is-size-6 has-text-weight-semibold is-align-content-center is-clipped is-family-monospace">{{ticket.title}}

                    
                    </span>
                </div>
                
                    <div class="is-flex ml-5">
                        <a  @click="this.$store.dispatch('checkPerms',['change_ticket',emitClick,'You have no permission to edit ticket(s).'])"><span class=" is-size-7"><i class="fa-solid fa-square-plus"></i></span></a>
                    </div>
            </div>
            <div class="is-flex-direction-row mb-3">
                <i v-if="ticket.type=='Bugs/errors'" class="fa-solid fa-bug"></i>
                        <i v-else-if="ticket.type=='Feature Requests'" class="fa-solid fa-code-pull-request"></i>
                        <i v-else class="fa-solid fa-comment"></i>
            </div>
            <div class="is-flex-direction-row ">
                <div class="is-size-7 has-text-weight-bold is-family-monospace" :class="{'has-text-danger':textColor()[0],'has-text-warning':textColor()[1],'has-text-info':textColor()[2]}"
               >
                    {{ ticket.priority }}
            </div>

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