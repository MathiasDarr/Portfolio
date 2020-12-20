<template>
  <v-container>
      <v-layout>
          <v-flex md4>
              <AbstractMenu :menu_items="menu_items" :menu_title="menu_title"/>
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
            menu_title: "Abstract Menu",
            menu_items: [
                    
                    {title:'Menu Item 2',  icon: 'mdi-lambda', 
                    admins: [
                        {title:'SubMenu Item 1', icon:'mdi-database-export-outline', route:'landing'},
                        {title:'SubMenu Item 2', icon:'mdi-music', route:'abstract'},
                    ]
                }
            ],
        }
    }
 
}
</script>