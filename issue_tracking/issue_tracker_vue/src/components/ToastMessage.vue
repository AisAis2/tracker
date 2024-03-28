<template >
    <div id="snackbar" :style="{opacity:opac,'background-color':'red'}">
        {{ message }}
    </div>
</template>
<script>
export default{
    props:{
        message:String,
    },
    data(){
        return{
            opac:1,
        }
    },
    mounted(){
        // this.fadeOut()
    },
    methods:{
        fadeOut(){
      let v = setInterval(()=>{
        this.opac-=0.1
        if(this.opac<=0){
          clearInterval(v)
          this.opac = 1;
        }
      },400)
    }
    }

}
</script>
<style>
#snackbar{
  min-width: 250px; /* Set a default minimum width */
  min-height:80px;
  border-radius:10px;
  margin-left: -125px; /* Divide value of min-width by 2 */
  color: #fff; /* White text color */
  text-align: left; /* Centered text */
  padding: 16px; /* Padding */
  position: fixed; /* Sit on top of the screen */
  z-index: 1; /* Add a z-index if needed */
  left: 92%; /* Center the snackbar */
  bottom: 30px; /* 30px from the bottom */
}
#snackbar.show {
  visibility: visible; /* Show the snackbar */
  /* Add animation: Take 0.5 seconds to fade in and out the snackbar.
  However, delay the fade out process for 2.5 seconds */
  -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

/* Animations to fade the snackbar in and out */
@-webkit-keyframes fadein {
  from {bottom: 0; opacity: 0;}
  to {bottom: 30px; opacity: 1;}
}

@keyframes fadein {
  from {bottom: 0; opacity: 0;}
  to {bottom: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
  from {bottom: 30px; opacity: 1;}
  to {bottom: 0; opacity: 0;}
}

@keyframes fadeout {
  from {bottom: 30px; opacity: 1;}
  to {bottom: 0; opacity: 0;}
}

</style>