<template>
<div id='wrapper'> 
  <div class="columns is-gapless">

    <div class="column">
              <nav class="navbar is-light p-1" :style="{'border-style':'none','box-shadow':'1px 1px'}">
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
          <div class="column is-2 has-background-primary-on-scheme " :style="{'height':'1000px','position':'sticky'}">
              <router-link to='/kanban' class="navbar-item p-4 is-family-monospace ml-6">Kanban</router-link>

              <router-link to="/ticket/all" class="navbar-item  p-4 is-family-monospace ml-6">Tickets</router-link>
              <router-link to="/projects/" class="navbar-item  is-family-monospace p-4 ml-6">Projects</router-link>
          </div>
          <div class="column is-10 has-background-primary-light" :style="{'height':'1000px','overflow':'auto'}">
            <router-view/>

          </div>  
        </div>
        <!-- <section class="section pt-1 is-link" :style="{'height':'900px','overflow':'auto'}">
        </section> -->
        <!-- <section class="section">
          test
        </section> -->
      <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2023</p>
  </footer>

    </div>
  </div>




</div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      showMobileMenu:false,
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = 'Token '+token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>



<style lang="scss">
@import '../node_modules/bulma';
</style>