import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'
import Advert from './views/Advert'


const router = new Router({
  mode: 'history',
  routes:
  [
    {
      path:'/',
      name:'home',
      component:Home
    },
    {
      path:'/advert/:advert_id',
      name:'advert',
      component:Advert
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})


Vue.use(Router)


export default router