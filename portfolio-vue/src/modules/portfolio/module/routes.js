import Portfolio from '../pages/Portfolio.vue'
import SnotelProject from '../pages/projects/snotel/SnotelProject'


export default [
	{ path: '', component: Portfolio },
	{ path: '/portfolio', component: Portfolio },

	{ path: '/portfolio/snotel', component: SnotelProject },
]
