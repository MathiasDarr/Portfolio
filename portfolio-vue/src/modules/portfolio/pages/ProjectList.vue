<template>
  <div>
    <v-card  height="900"  flat>

      <v-navigation-drawer absolute permanent >
        <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            <h2> Projects </h2>
          </v-list-item-title>
          <v-list-item-subtitle>
            
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
        
        <v-list
          
          nav
          class="py-0">

              <v-list-item dense 
                v-for="item in items"
                :key="item.title"
                link >
              <v-list-item-content @click="navigate(item.route)">

              <v-list-item-title>{{ item.title }}</v-list-item-title>

          </v-list-item-content>
         </v-list-item>
        </v-list>
      </v-navigation-drawer>

    </v-card>
  </div>
</template>

<script>

import router from '../../../services/router'


export default {
  created(){

  },

  methods:{
    navigate(route){
      if(route != this.$route.path){
        router.push(route)
      }
          
    }
  },

    data(){
        return {
            items: [
                { title: 'Snotel Pipeline', icon: 'mdi-view-dashboard', route:'/portfolio/snotel' },
                { title: 'Serverless Ecommerce Application', icon: 'mdi-view-dashboard', route:'/portfolio/sam-ecommerce' },
                // { title: 'Serverless Upload Application', icon: 'mdi-image', route:'/portfolio/upload' },
                // { title: 'Spring RideShare Microservices', icon: 'mdi-image', route:'/portfolio/rideshare' },
                // { title: 'Spring ECommerce Microservices', icon: 'mdi-image', route:'/portfolio/spring-ecom' },
                // { title: 'Serverless Data Processing Applications', icon: 'mdi-view-dashboard', route:'/portfolio/serverless-data' },
                // { title: 'Music Information Retrieval', icon: 'mdi-view-dashboard', route:'/portfolio/mir' },
                // { title: 'Twitter Pipeline', icon: 'mdi-view-dashboard', route:'/portfolio/twitter/pipeline' },
                // { title: 'Twitter ElasticSearch API', icon: 'mdi-view-dashboard', route:'/portfolio/twitter/query-api' },

                // { title: 'Neural Machine Translation', icon: 'mdi-view-dashboard', route:'/portfolio/nmt' },
          ],
        }
    }
  
}
</script>