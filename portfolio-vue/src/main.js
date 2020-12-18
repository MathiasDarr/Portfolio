import Vue from 'vue'
import vuetify from './plugins/vuetify';
import Router from './services/router'
import Store from './services/store'
import App from './App.vue'
import cognitoAuth from './cognito'

import system from './modules/system/module'

/* Initialize System Module */
Store.registerModule('system', system.store)
Router.addRoutes(system.routes)
Store.dispatch('system/initialize', null, { root: true })



Vue.config.productionTip = false

new Vue({
  vuetify,
	router: Router,
	store: Store,
  cognitoAuth,
  render: h => h(App)
}).$mount('#app')
