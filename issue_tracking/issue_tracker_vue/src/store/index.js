import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated:false,
    token:'',
    project_filter:'General',
    user:'',
    errorMsg:'',
    perms_list:[],
    user_list:[],
    role:'',
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
    setRole(state,role){
      state.role = role
      localStorage.setItem('role',role)
    },
    getRole(state,role){
      if(~state.role){
        state.role =  localStorage.getItem('role')
      }
    },
    setPfilter(state,filter){
      state.project_filter=filter
      localStorage.setItem('project_filter',filter)
    },
     newErrMsg(state,msg){
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
    },
    setPermsList(state,list){
        state.perms_list=list
        localStorage.setItem('perms_list',list)
    },
    getPermsList(state){
      if(localStorage.getItem('perms_list')){
        state.perms_list= localStorage.getItem('perms_list').split(',')
      }
    },
    setUserList(state,list){
      state.user_list=list
      localStorage.setItem('user_list',JSON.stringify(list))
    },
    getUserList(state){
      if(localStorage.getItem('user_list')){
        state.user_list= JSON.parse(localStorage.getItem('user_list'))
      }

    }


  },
  actions: {
    checkPerms(context,arr){
      for(let i=0;i<context.state.perms_list.length;i++){
        
        if(context.state.perms_list[i]===arr[0]){
          if(arr.length==4){
            arr[1](arr[3]);

          }
          else{
            arr[1]()
          }
          return;
        }
      }
      context.commit('newErrMsg',arr[2])
    }
  },
  modules: {
  }
})
