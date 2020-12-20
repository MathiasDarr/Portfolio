/* eslint-disable */


import Home from '../pages/Home.vue'
import Contact from '../pages/Contact.vue'
import FAQ from '../pages/FAQ.vue'
import Landing from '../pages/Landing'


import AbstractArticle from '../../../components/AbstractArticle'

export default [
	{ path: '', component: Landing },
	{ path: '/abstract', component: AbstractArticle },
	{ path: '/faq', component: FAQ }
]
