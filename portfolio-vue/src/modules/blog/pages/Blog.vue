<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <BlogMenu />
      </v-flex>
      <v-flex md9>
        <h1> Dakobed Blog </h1>
        <ArticleList />
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>


import BlogMenu from './BlogMenu'
import ArticleList from './articles/ArticleList'
export default {
    
    components:{
      BlogMenu,
      ArticleList
    },

    data(){
        return {
        }
    }

}
</script>