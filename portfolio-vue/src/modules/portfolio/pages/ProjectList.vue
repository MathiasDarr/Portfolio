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
            <h4> Portfolio Projects </h4>
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

      
    </v-list>


  </v-card>

  </div>
</template>

<script>
/* eslint-disable */
import router from '../../../services/router'


export default {
  created(){

  },

  methods:{
    navigate(route){
      // if(route != this.$route.path){
      //   router.push(route)
      // }

    }
  },

    data(){
        return {


          pipeline_projects: [['Management', 'mdi-account-multiple-outline'], ['Settings', 'mdi-cog-outline'],], 

          categories: [{title:'Data Pipelines', icon: 'mdi-database-arrow-down-outline', admins: [['USDA Snowpack Pipeline', 'mdi-snowflake', '/portfolio/snotel'], ['Twitter Streaming Pipeline', 'mdi-twitter', '/portfolio/twitter/pipeline'],], },
          {title:'Serverless Applications',  icon: 'mdi-lambda', admins: [['Serverless ECommerce ', 'mdi-cart',  '/portfolio/serverless/ecommerce'], ['Serverless Upload API', 'mdi-cloud-upload-outline', '/portfolio/serverless/upload'], ['Serverless Data Processing ', 'mdi-database-export-outline', '/portfolio/serverless/data-processing']], },
          {title: 'MicroServices', icon: 'mdi-cloud-outline', admins: [['RideShare Microservices', 'mdi-kubernetes', '/portfolio/microservices/rideshare'], ['Ecommerce Microservices', 'mdi-cart','/portfolio/microservices/ecomm'], ['Health Care Scheduling Services', 'mdi-heart-outline', '/portfolio/microservices/healthcare'],], },
          {title : 'Deep Learning', icon: 'mdi-lan', admins: [['Music Information Retrieval', 'mdi-music','/portfolio/deep-learning/mir'], ['Neural Machine Translation', 'mdi-translate', '/portfolio/deep-learning/nmt'],], },
          {title: 'Analytics', icon: 'mdi-data-matrix', admins: [['Twitter NLP', 'mdi-twitter','/portfolio/analytics/twitternlp']], },
          
          ],

          admins: [
            ['Management', 'mdi-account-multiple-outline'],
            ['Settings', 'mdi-cog-outline'],
          ],
          cruds: [
            ['Create', 'mdi-plus-outline'],
            ['Read', 'mdi-file-outline'],
            ['Update', 'mdi-update'],
            ['Delete', 'mdi-delete'],
          ],
            

//             items: [
//                 { title: 'Snotel Pipeline', icon: 'mdi-view-dashboard', route:'/portfolio/snotel' },
//                 { title: 'Serverless Ecommerce Application', icon: 'mdi-view-dashboard', route:'/portfolio/serverless/ecommerce'},
                
//                 {title: 'Serverless Upload Application' ,route :'/portfolio/serverless/upload'},
//                 { title: 'Serverless Data Processing Applications', icon: 'mdi-view-dashboard', route:'/portfolio/serverless/data-processing' },
//                 { title: 'Spring RideShare Microservices', icon: 'mdi-image', route:'/portfolio/microservices/rideshare' },
// // { title: 'Serverless Upload Application', icon: 'mdi-image', route:'/portfolio/upload' },
              
//                 { title: 'Spring HealthCare Microservices', icon: 'mdi-image', route:'/portfolio/microservices/healthcare' },

//                 // { title: 'Spring ECommerce Microservices', icon: 'mdi-image', route:'/portfolio/spring-ecom' },
//                 // { title: 'Serverless Data Processing Applications', icon: 'mdi-view-dashboard', route:'/portfolio/serverless-data' },
//                 { title: 'Twitter Pipeline', icon: 'mdi-view-dashboard', route:'/portfolio/twitter/pipeline' },
//                 { title: 'Twitter ElasticSearch API', icon: 'mdi-view-dashboard', route:'/portfolio/twitter/query-api' },

//                 { title: 'Music Information Retrieval', icon: '', route: '/portfolio/deep-learning/mir'} ,

//                 { title: 'Neural Machine Translation', icon: 'mdi-view-dashboard', route:'/portfolio/deep-learning/nmt' },
          // ],
        }
    }
  
}
</script>