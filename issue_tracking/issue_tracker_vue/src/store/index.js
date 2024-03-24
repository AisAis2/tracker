import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated:false,
    token:'',
    project_filter:'General',
    user:'',
    errorMsg:'',
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }
      else{
        state.token = ''
        state.isAuthenticated = false
      }
    },
    async newErrMsg(state,msg){
      state.errorMsg=msg;
      setTimeout(()=>{state.errorMsg=''},4000)
    },
    setToken(state,token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state,user){
      state.user=user
      localStorage.setItem('user',JSON.stringify(user))
    },
    removeUser(state){
      state.user=''
      localStorage.removeItem('user')
    }

  },
  actions: {
  },
  modules: {
  }
})
