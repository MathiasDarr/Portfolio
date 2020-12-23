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
        <v-btn  v-for="item in menuItems" :key="item.title" @click="navigate(item.route, item.name, item.module_)" class ="grey--text" >
        <!-- <v-btn  v-for="item in menuItems" :key="item.title" :to= "item.route" class ="grey--text" > -->
          <v-icon left >
          </v-icon>
          {{item.title}}
        </v-btn>
      
      </v-toolbar-items>
      
      <v-toolbar-items class = "hidden-xs-only">
        <v-btn  v-for="item in authItems" :key="item.title" @click="navigate_to_name_route(item.name)" class ="grey--text" >
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
/* eslint-disable */

import portfolio from './modules/portfolio/module'
import blog from './modules/blog/module'
import router from './services/router'
import module from './modules/portfolio/module';


export default {
  name: 'App',

  components: {

  },

  methods:{

    loadBlogModule(){
      this.$store.dispatch('system/initializeModule', blog)
    },

		loadPortfolioModule () {
				this.$store.dispatch('system/initializeModule', portfolio)
		},

    check_module(children, module_name, module_){
        if(module_name == 'landing'){
          return
        }
        
        if(children[module_name] == null){
            this.$store.dispatch('system/initializeModule', module_)
          }else{
            console.log("YES")
        }
    },
    navigate(route, name, module_){
      if(route != this.$route.path){
                
        var children = this.$store._modules.root._children
        this.check_module(children, name, module_)

        router.push(route)
      }
    },
    navigate_to_name_route(route){
      router.push({name:route})
    }
  },

  data(){
    return {
        drawer: false,
        menuItems:[
          {title:'Landing', route:'/', name:'landing', module_: null }, 
          {title: 'Blog', route: '/blog', name:'blog', module_:blog},
          {title:'Portfolio', route:'/portfolio', name:'portfolio', module_: portfolio },
        ],
        authItems:[
          {title:'Register', route:'/register', name:'register'}, 
          {title:'Login', route:'/login', name:'login'}, 
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
