<template>
  <v-container>
      <v-layout>
          <v-flex md4>
              <AbstractMenu :menu_items="menu_items"/>
          </v-flex>
          <v-flex md6>

          </v-flex>
      </v-layout>
      
  </v-container>
</template>

<script>

import AbstractMenu from './AbstractMenu'

export default {
    components:{
        AbstractMenu
    },
    data(){
        return {
            menu_items: [
                    {title:'Data Pipelines', icon: 'mdi-database-arrow-down-outline', 
                    
                    admins: [['USDA Snowpack Pipeline', 'mdi-snowflake', '/portfolio/snotel'],
                            ['Twitter Streaming Pipeline', 'mdi-twitter', '/portfolio/twitter/pipeline'],], },
                    
                    {title:'Serverless Applications',  icon: 'mdi-lambda', 
                    admins: [['Serverless ECommerce ', 'mdi-cart', '/portfolio/serverless/ecommerce'],
                        ['Serverless Upload API', 'mdi-cloud-upload-outline', '/portfolio/serverless/upload'], 
                        ['Serverless Data Processing ', 'mdi-database-export-outline', '/portfolio/serverless/data-processing']], }
            ],
        }
    }
 
}
</script>