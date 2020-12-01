import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'
import Advert from './views/Advert'
import Users from './views/Users'
import UserDetail from './views/UserDetail'
UserDetail

const router = new Router({
  mode: 'history',
  routes:
  [
    {
      path:'/',
      name:'home',
      component: Home
    },
    {
      path:'/advert/:advert_id',
      name:'advert',
      component: Advert
    },
    {
      path:'/users',
      name:'users',
      component: Users
    },
    {
      path:'/users/:user_id',
      name:'user_detail',
      component: UserDetail
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})


Vue.use(Router)


export default router