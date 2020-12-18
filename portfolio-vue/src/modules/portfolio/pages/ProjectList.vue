<template>
  <div>
  <v-card
    class="mx-auto"
    width="300"
  >
    <v-list>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-home</v-icon>
        </v-list-item-icon>

        <v-list-item-title>Home</v-list-item-title>
      </v-list-item>

      <v-list-group :value="true" prepend-icon="mdi-account-circle">
        <template v-slot:activator>
          <v-list-item-title>Users</v-list-item-title>
        </template>

        <v-list-group
          :value="true"
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Admin</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in admins"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>

        <v-list-group
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Actions</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in cruds"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
      </v-list-group>
    </v-list>
  </v-card>





    <!-- <v-card  height="900"  flat>

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

    </v-card> -->
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