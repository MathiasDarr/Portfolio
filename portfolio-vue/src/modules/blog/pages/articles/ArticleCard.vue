<template>
  <v-container>
    <v-card height="300" width="1300">
      
      <v-layout>
        <v-flex md9>
          <v-card-title>
            {{ title }} 

          </v-card-title>
        </v-flex>
        <v-flex md3>
          <v-card-subtitle>
            <b> {{ article_date }} </b>
          </v-card-subtitle>
        </v-flex>
        
      </v-layout>


      <v-divider></v-divider>
      <v-layout>
        <v-flex md9>
          <v-card-text>
            <p v-html="article_preview"></p>
          </v-card-text>  
        </v-flex>
        <v-flex md3>
          <v-card-subtitle>
            <v-img lazy-src="https://picsum.photos/id/11/10/6" src="https://picsum.photos/id/11/500/300"> </v-img>
          </v-card-subtitle>
        </v-flex>
      </v-layout>
<!-- 
      <v-card-text>
         <p v-html="article_preview"></p>
      </v-card-text>       -->

    </v-card>
  </v-container>    
</template>

<script>
export default {
  created(){

  },

    props:{
      title: String,
      article_date:String,
      article_preview:String,
      category:String
    }
}
</script>
