import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import store from '../store'
import Projects from '../views/Projects.vue'
import Project from '../views/Project.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import AccountPage from '../views/AccountPage.vue'
import CreateProject from '../views/CreateProject.vue'
import Ticket from '../views/Ticket.vue'
import Kanban from '../views/Kanban.vue'
import CreateTicket from '../views/CreateTicket.vue'
import TicketList from '../views/TicketList'
import UsersList from '../views/Users.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/project/:id/',
    name: 'Project',
    component: Project
  },
  {
    path:'/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path:'/login',
    name: 'Login',
    component: Login
  },
  {
    path:'/my-account',
    name: 'MyAccount',
    component: AccountPage,
    meta:{
      requireLogin:true
    }
  },
  // {
  //   path:'/project/create/',
  //   name: 'CreateProject',
  //   component: CreateProject,
  //   meta:{
  //     requireLogin:true
  //   }
  // },
  {
    path:'/ticket/:id/',
    name: 'Ticket',
    component: Ticket
  },
  {
    path:'/kanban',
    name: 'Kanban',
    component: Kanban,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/ticket/create',
    name: 'CreateTicket',
    component: CreateTicket
  },
  {
    path:'/ticket/all',
    name: 'TicketList',
    component: TicketList,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/users/all',
    name: 'Users',
    component: UsersList
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next)=>{
  if(to.matched.some(record=>record.meta.requireLogin) && !store.state.isAuthenticated){//Is it a good practice?
    next({name: 'Login', query:{to:to.path}});
  } else{
    next()
  }
})
export default router
