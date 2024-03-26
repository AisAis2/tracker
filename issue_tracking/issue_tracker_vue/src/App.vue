<template>
<div id='wrapper'> 
  <div class="columns is-gapless">

    <div class="column">
              <nav class="navbar is-link is-light p-1" :style="{'border-style':'none','box-shadow':'1px 1px'}">
          <div class="navbar-brand">
            <router-link to='/' class="navbar-item"><i class="fa-solid fa-house"></i></router-link>
            <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click ="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            </a>
          </div>

          <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
            <div class="navbar-end">
              <!-- <router-link to='/project/create/' class="navbar-item">Create Project</router-link> -->
              <div class="navbar-item">
                <div class="buttons">
                  <template v-if="!$store.state.isAuthenticated">
                      <router-link to='/login' class="button is-light">
                          <span class="icon"><i class="fa-solid fa-right-to-bracket"></i></span>
                          <span>Log in</span>
                      </router-link>
                  </template>
                  
                  <template v-else>
                    <router-link to='/my-account' class="button is-light">
                    <span class="icon"><i class="fa-solid fa-user"></i></span>
                      <span class="is-family-monospace">My Account</span>
                    </router-link>
   
                  </template>

                </div>
              </div>
            </div>
          </div>
        </nav>
        <div class="columns is-gapless" >
          <div class="is-flex-direction-column  has-background-info-light " :style="{'position':'sticky','width':'300px'}">
              <router-link to='/kanban' class="navbar-item p-4 is-family-monospace ml-6 has-text-weight-bold">Kanban</router-link>

              <router-link to="/ticket/all" class="navbar-item  p-4 is-family-monospace ml-6 has-text-weight-bold">Tickets</router-link>
              <router-link to="/projects/" class="navbar-item  is-family-monospace p-4 ml-6 has-text-weight-bold">Projects</router-link>
          

            </div>
          <div class="is-flex-direction-row mx-5 my-2" :style="{'height':'1000px','overflow-x':'hidden'}">
            <router-view/>

          </div>  
        </div>
      <footer class="footer">
        <p class="has-text-centered">Copyright (c) 2023</p>
      </footer>
    </div>
    <ToastMessage
    v-if="errMsg"
    :message="errMsg"
    />

  </div>




</div>
</template>

<script>
import axios from 'axios'
import ToastMessage from './/components/ToastMessage.vue';
import { mapState } from 'vuex';
export default {
  data(){
    return {
      showMobileMenu:false,
      errorMsg:'test',
      opacity:1,          
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    this.$store.commit('getPermsList')
    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = 'Token '+token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
components:{
  ToastMessage
},
computed:mapState({
  errMsg:state=>state.errorMsg
}),
methods:{

}

}
  
</script>



<style lang="scss">
@import '../node_modules/bulma';
</style>
