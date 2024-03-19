<template>
    <div :class="{'box':true, 'my-3':true, bgColor:true }" :style="{'height':'100px','overflow':'hidden'}">
        <div class="columns is-flex">
            <div class="column is-10">
                <span class="is-size-6 has-text-weight-semibold is-align-content-center">{{ticket.title}}</span>
            </div>
            <div class="column">
                <a  @click="emitClick()"><span class=" is-size-7 is-align-content-center "><i class="fa-solid fa-square-plus"></i></span></a>
            </div>
        </div>
        <div class="columns is-flex">
            <div class="column">
                <span class="is-size-7 has-text-weight-bold" :class="{'has-text-danger':textColor()[0],'has-text-warning':textColor()[1],'has-text-info':textColor()[2]}">
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