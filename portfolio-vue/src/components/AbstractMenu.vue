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
            <h4> {{ menu_title }} </h4>
          </v-list-item-title>
          <v-list-item-subtitle>
            
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      
      <v-list-group
        :value="false"
        :prepend-icon="item.icon"
        v-for="item in menu_items" :key="item.title">
          <template v-slot:activator>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </template>
          
          <v-list-group
            :value="false"
            :prepend-icon="project.icon"
            sub-group
            v-for="project in item.admins"
            @click="navigate_to_route_name(project.route)"
            :key="project.title">

            <template v-slot:activator>
              <v-list-item-title>{{project.title}}</v-list-item-title>
            </template>

        </v-list-group>


      </v-list-group>

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
        menu_items: Array,
        menu_title: String
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