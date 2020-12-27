import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import uploads from './modules/uploads'

Vue.use(Vuex)

export default new Vuex.Store({
    modules:{
        auth,
        uploads
    }
})