<template>
  <div>
  <v-card
    class="mx-auto"
    width="400"
    flat 
  >
    <v-list>
      
        <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            <h4> Menu Items </h4>
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
        
        <v-btn color="primary" @click="navigate_to_route_name('post_article')"> Post New Article </v-btn>
        </v-list-item>
      
    </v-list>
    



  </v-card>

  </div>
</template>

<script>

import router from '../services/router'


export default {
    created(){

    },
    props: {
        menu_items: Array
    },


    methods:{

        navigate_to_route_name(route_name){
        router.push({name:route_name})
        },
        navigate(route){
        if(route != this.$route.path){
            router.push(route)
        }
            
        }
    },

        data(){
            return {

            }
        }
  
}
</script>