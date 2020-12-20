/* eslint-disable */


import Home from '../pages/Home.vue'
import Contact from '../pages/Contact.vue'
import FAQ from '../pages/FAQ.vue'
import Landing from '../pages/Landing'


import AbstractArticle from '../../../components/AbstractArticle'

export default [
	{ path: '', component: Landing, name: "landing" },
	{ path: '/abstract', component: AbstractArticle, name: "abstract" },
	{ path: '/faq', component: FAQ }
]
