import Vue from 'vue'
import Router from 'vue-router'

import posts from './components/posts'
import users from './components/users'


Vue.use(Router)

var routes=[

    {
      path: '/',
      name: 'Posts',
      component: posts
    },
    {
      path: '/users',
      name: 'Users',
      component: users
    },

  ]

  const router = new Router({mode:'history',routes});

  export default router