/* eslint-disable */

// import axios from 'axios';
import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
import axios from 'axios';


const state = {
    image_url: false,
};

const getters = {
    getImageUrl: state => state.image_url,

};

const actions = {
    async setImageUploadUrl({commit}, image_url){
        commit('setImageUrl', image_url)
    },
};



const mutations = {
    setImageUrl: (state, imageURL) => { state.image_url = imageURL;},

};

export default {
  state,
  getters,
  actions,
  mutations
};
