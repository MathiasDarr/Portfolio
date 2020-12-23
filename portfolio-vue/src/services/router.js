/* eslint-disable */

import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../components/Login'
import Register from '../components/Register'
import Confirm from '../components/Confirm'


Vue.use(VueRouter)

export default new VueRouter({
	mode: 'history',
	routes: [{
		path:'/login',
		name:'login',
		component: Login
	  },
	  {
		path:'/register',
		name:'register',
		component: Register
	  },
	  {
		path:'/confirm',
		name:'confirm',
		component: Confirm
	  }
	,]
})