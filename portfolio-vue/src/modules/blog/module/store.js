/* eslint-disable */

export default {
	namespaced: true,
	state: {
		articles: []
	},
	getters: {
		getArticles: state => state.articles,
	},
	mutations: {
		setArticles: (state, articles) => (state.articles = articles)
	},
	actions: {
		initialize ({ commit }) {
			console.info('Blog initializing...')
			console.info('Blog initialized...')
		},

		async setArticles({commit}, articles){
			commit('setArticles', articles)
		},

	}
}

