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
                      <span class="is-family-monospace">Actions</span>
                    </router-link>
   
                  </template>

                </div>
              </div>
            </div>
          </div>
        </nav>
        <div class="is-flex" >
          <div class="is-flex-direction-column  has-background-info-light px-3 pt-3" :style="{'position':'sticky','width':'250px'}">
              <router-link to='/dashboard' class="navbar-item is-family-monospace has-text-weight-bold">Dashboard</router-link>
              <router-link to='/kanban' class="navbar-item is-family-monospace has-text-weight-bold">Kanban</router-link>
              <router-link to="/projects/" class="navbar-item  is-family-monospace   has-text-weight-bold">Projects</router-link>
              <router-link to="/users/" class="navbar-item  is-family-monospace   has-text-weight-bold" v-if="$store.state.role=='admin'">User Management</router-link>
            </div>
          <div class="mx-5 my-2" :style="{'height':'1000px','width':'1500px','overflow-x':'hidden'}">
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
    this.$store.commit('getRole')

    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = 'Token '+token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted(){
    if(this.$store.state.role === 'admin'){
      this.getUsersList()
    }
  },
components:{
  ToastMessage
},
computed:mapState({
  errMsg:state=>state.errorMsg
}),
methods:{

    async getUsersList(){
      await axios
          .get('/api/v1/users/')
          .then((response)=>{
            this.$store.commit('setUserList',response.data)
            this.$store.commit('getUserList')
          })
    },
    closeModal(){
             const modal = document.querySelector('.modal')
             modal.addEventListener('keydown',()=>{
              console.log('ESC')
              modal.classList.remove('is-active')
             })
}
}

}

</script>



<style lang="scss">
@import '../node_modules/bulma';
</style>
