<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <BlogMenu />
      </v-flex>
      <v-flex md9>
      
        <v-row>
          <v-col cols="12" sm="10">
            <h1> Dakobed Blog </h1>
          </v-col>
          <v-col cols="12" sm="2">
            <div v-if="getIdToken">
               <v-btn color="primary" @click="navigate_to_route_name('post_article')">POST Article </v-btn>
            </div>
          </v-col>
        </v-row>
      
        <ArticleList />
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>

/* eslint-disable */

import BlogMenu from './BlogMenu'
import ArticleList from './articles/ArticleList'
import router from '../../../services/router'
import { mapGetters, mapActions } from "vuex";
export default {
    
    components:{
      BlogMenu,
      ArticleList
    },

    computed: {
        ...mapGetters(["getIdToken"]),
    },

    methods:{
      navigate_to_route_name(route_name){
        router.push({name:route_name})
      },
    },
    
    created(){
      console.log("THE ID TOKEN IS " + this.getIdToken)
    },

    data(){
        return {
        }
    }

}
</script>