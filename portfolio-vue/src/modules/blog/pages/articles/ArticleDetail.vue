<template>
  <v-container>
      <!-- <h1> {{ article_title }} </h1> -->
      
    <v-container>
      
      <v-row>
        <v-col cols="12" sm="10">
            <h1> {{ article_title }} </h1>
        </v-col>

        <v-col cols="12" sm="2">
            <v-btn color="primary" @click="delete_article()">Delete Article </v-btn>
        </v-col>
      </v-row>

    </v-container>
      
      
      <p v-html="content"></p>


    <!-- <h2> {{article_title}} </h2> -->
    <!-- <p :v-html="article_content"></p>
    <div v-if="content != ''">
        <ArticleContents :content="content" />
         <p :v-html="html_string"></p>

    </div> -->

  </v-container>

</template>

<script>
/* eslint-disable */

import axios from 'axios';


export default {

    components:{
    },

    created(){

        this.article_id = this.$route.params.article_id

        this.fetch_article_detail()
    },


    methods:{

      async fetch_article_detail(){
            try{
                //var url = window.__runtime_configuration.apiEndpoint + '/categories'
                var url ='https://2qlgw486nb.execute-api.us-west-2.amazonaws.com/Prod/articles/detail/'+ this.article_id + '/' + this.article_date
                const response = await axios.get(url)            
                var response_article_detail = JSON.parse(response.data.body)
                // this.setArticles(response_articles.articles)
                this.content = response_article_detail.article.content
                this.article_title = response_article_detail.article.title
  

                // this.article = response_articles.article
            }catch(err){
                console.log(err)
            }
        },
        
        async await_article_detail(){
            await this.fetch_article_detail()
            // this.articles = this.getArticles
        },


      async delete_article(){
            try{
                //var url = window.__runtime_configuration.apiEndpoint + '/categories'
                var url ='https://2qlgw486nb.execute-api.us-west-2.amazonaws.com/Prod/articles/detail/'+ this.article_id + '/' + this.article_date
                const response = await axios.delete(url)            
                var response_articles = JSON.parse(response.data.body)
                // this.setArticles(response_articles.articles)
                console.log(response_articles.articles)
            }catch(err){
                console.log(err)
            }
        },

        async await_delete_article(){
            await this.delete_article()
        },


    },


    
    props:{
        article_date:String,

    },


    data(){
        return {
            title: 'Welcome to <br/> Arrow GTP',
            html_string: `<h1> THIS IS RENDERED <h1>`,
            article_title:'',
            content: '',
            article_content:'<h1> Spark ML Pipelines THIS IS GETTING RENDERED</h1>'
        }
    }
}
</script>