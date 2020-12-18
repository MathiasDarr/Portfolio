<template>
  <v-app>
    <nav>
      <div>
        </div>

      <v-toolbar flat dark class="py-0 mt">
        
        <v-app-bar-nav-icon class ="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title class="grey--text">
            <span class="font-weight-light">Dalinar</span>
            <span>MIR</span>
          </v-toolbar-title>
          <v-spacer></v-spacer>
      
      <v-toolbar-items class = "hidden-xs-only">
        <v-btn  v-for="item in menuItems" :key="item.title" @click="navigate(item.route)" class ="grey--text" >
        <!-- <v-btn  v-for="item in menuItems" :key="item.title" :to= "item.route" class ="grey--text" > -->
          <v-icon left >
          </v-icon>
          {{item.title}}
        </v-btn>
      
      </v-toolbar-items>
      
      <v-spacer></v-spacer>
      </v-toolbar>
    </nav>

    <router-view :key="$route.fullPath"></router-view>
  </v-app>
</template>

<script>

import moduleA from './modules/moduleA/module'
import Blog from './modules/blog/module'
import router from './services/router'


export default {
  name: 'App',

  components: {

  },

  methods:{

    loadBlogModule(){
      this.$store.dispatch('/system/initializeModule', Blog)
    },

		loadModuleA () {
				this.$store.dispatch('system/initializeModule', moduleA)
		},




    loadPortfolioModule(){
      console.log("loading portfolio")
    },

    navigate(route){
      if(route != this.$route.path){
        
        if(route == '/blog'){
          this.loadModuleA()
        }

        if(route=='/portfolio'){
          this.loadModuleA()
        }

        router.push(route)
      }
          
    }
  },

  data(){
    return {
        drawer: false,
        menuItems:[
          {title:'Landing', route:'/' }, 
          {title: 'Blog', route: '/blog'},
          {title:'Portfolio', route:'/portfolio/' },

        ],

        color: 'primary',
        colors: [
          'primary',
          'blue',
          'success',
          'red',
          'teal',
        ],
        right: false,
        permanent: false,
        miniVariant: false,
        expandOnHover: false,
        background: false,
      }
    },
};
</script>
