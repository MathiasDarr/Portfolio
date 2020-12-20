<template>
  <v-container>
      <v-card
    class="mx-auto"
    width="400"
    flat 
  >
    <v-list>
      
        <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            <h4> Post Article </h4>
          </v-list-item-title>
          <v-list-item-subtitle>
            
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      
      <v-list-group
        :value="false"
        :prepend-icon="item.icon"
        v-for="item in categories" :key="item.title">
          <template v-slot:activator>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </template>
          
          <v-list-group
            :value="false"
            :prepend-icon="project[1]"
            sub-group
            v-for="project in item.admins"
            @click="navigate(project[2])"
            :key="project[0]">

            <template v-slot:activator>
              <v-list-item-title>{{project[0]}}</v-list-item-title>
            </template>

      </v-list-group>


      </v-list-group>
      <v-list-item>
        
        <v-btn color="primary" @click="navigate_to_route_name('post_article')"> New Article </v-btn>
        </v-list-item>
      
    </v-list>
    



  </v-card>

  </v-container>
</template>

<script>

import router from '../../../../services/router'

export default {
    methods:{
        navigate_to_route_name(route_name){
            router.push({name:route_name})
        },
    },
    data(){
        return {
          pipeline_projects: [['Management', 'mdi-account-multiple-outline'], ['Settings', 'mdi-cog-outline'],], 
          categories: [{title:'Data Pipelines', icon: 'mdi-database-arrow-down-outline', admins: [['USDA Snowpack Pipeline', 'mdi-snowflake', '/portfolio/snotel'], ['Twitter Streaming Pipeline', 'mdi-twitter', '/portfolio/twitter/pipeline'],], },
          ],

        }
    }
}
</script>