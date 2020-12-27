<template>

  <v-container>
    <v-layout>
      <v-flex md3>
        <!-- <BlogMenu /> -->
      </v-flex>
      <v-flex md9>
      
        <v-row>
          <v-col cols="12" sm="10">
            <h1> Portfolio</h1>
          </v-col>
          <v-col cols="12" sm="2">
            <div v-if="getIdToken">
               <v-btn color="primary" @click="navigate_to_route_name('post_portfolio_article')">POST PORTFOLIO ARTICLE </v-btn>
            </div>
          </v-col>
        </v-row>
      
      </v-flex>
    </v-layout>
  </v-container>
  <!-- <v-container>
    <v-layout>
      <v-flex md4>
        <ProjectList />
      </v-flex>
      <v-flex md5>
        <h1> This is the portfolio </h1>
      </v-flex>
    </v-layout>
  </v-container> -->
</template>

<script>

/* eslint-disable */


import router from '../../../services/router'
import { mapGetters, mapActions } from "vuex";


import ProjectList from './ProjectList'

export default {
    
    methods:{
      navigate_to_route_name(route_name){
        router.push({name:route_name})
      },
    },

    components:{
      ProjectList
    },

        computed: {
        ...mapGetters(["getIdToken"]),
    },

    data(){
        return {
        }
    }

}
</script>