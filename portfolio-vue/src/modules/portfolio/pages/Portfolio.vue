<template>
  <v-container>
    <v-layout>
      <v-flex md4>
        <ProjectList />
      </v-flex>
      <v-flex md5>
        <h1> This is the portfolio </h1>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>


import ProjectList from './ProjectList'

export default {
    
    components:{
      ProjectList
    },

    data(){
        return {
        }
    }

}
</script>