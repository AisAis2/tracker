<template>
    <!-- <div :class="{'box':true, 'my-2':true,'mx-4':true, bgColor:true,'is-family-monospace':true  }" :style="{'height':'130px','overflow':'hidden','border':'solid','box-shadow':'1px 1px','border-width':'1px'}" >
        <div class="is-flex is-flex-direction-column ">
            <div class="is-flex is-flex-direction-row" :style="{'height':'45px','overflow':'hidden'}">
                <div class="is-flex" :style="{'max-width':'250px'}">
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
    </div> -->
    <div class="is-flex is-flex-direction-column" :style="{'width':'250px','border-style':'solid','height':'120px','border-width':'1px','margin-left':'10px','margin-top':'10px','margin-right':'15px'}">
        <div :style="{'margin':'10px','max-width':'auto','max-height':'auto'}" class="is-flex is-flex-direction-column">
            <div class="is-size-7 is-family-monospace is-clipped" :style="{'max-width':'auto','word-break':'break-all','height':'50px','margin-bottom':'5px'}">{{ticket.title}}</div>
            <span class="is-size-6 " :style="{'display':'inline-block','margin-bottom':'3px'}">
                <span :style="{'padding':'2px'}" class="has-background-success is-uppercase has-text-weight-semibold is-size-7">{{project}}</span>
            </span>
            <div class="is-size-7 has-text-weight-bold is-uppercase" :class="{'has-text-danger':textColor()[0],'has-text-warning':textColor()[1],'has-text-info':textColor()[2]}">
                    {{ ticket.priority }}
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
    mounted(){
        console.log(this.project)
    },
    props:{
        ticket:Object,
        project:String,
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