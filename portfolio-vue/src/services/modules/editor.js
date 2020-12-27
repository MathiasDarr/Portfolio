/* eslint-disable */

// import axios from 'axios';
import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
import axios from 'axios';


const state = {
    editor_content: false,
};

const getters = {
    getJwtAccessToken: state => state.access_token,

};

const actions = {


    async setJWT({commit}, tokens){

        commit('setAccessToken', tokens)
    },


    async setEmail({commit}, email){

    }
};



const mutations = {
    setLoggedIn: (state, newValue) => { state.loggedIn = newValue;},

};

export default {
  state,
  getters,
  actions,
  mutations
};
