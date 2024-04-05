<template>
<div id="myChart" style="max-width:700px; height:400px"></div>

    
</template>
<script>
export default{
    beforeCreate(){


    },
    mounted(){
        let graphScript = document.createElement('script')
        graphScript.setAttribute('src',"https://www.gstatic.com/charts/loader.js")
        document.head.appendChild(graphScript)
        if(google){
            google.charts.load('current', {'packages':['corechart']});
        }
    }
}

</script>