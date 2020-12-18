import Store from '../../../services/store'
import Router from '../../../services/router'
import siteModule from '../../site/module'
import blogModule from '../../blog/module'


export default {
	namespaced: true,
	
	state: {},
	
	getters: {},
	
	mutations: {},
	
	actions: {
		initializeBlogModule({dispatch}){
			console.log("BLOG INITIALIZING")
			dispatch('initializeBlogModule', blogModule)
		},
		
		initialize ({ dispatch }) {
			console.info('System initializing...')
			console.info('System initialized.')
			dispatch('initializeModule', siteModule)
		},
		initializeModule ({ dispatch }, module) {
			Store.registerModule(module.name, module.store)
			Router.addRoutes(module.routes)
			dispatch(module.name + '/initialize', null, { root: true })
		}
	}
}
