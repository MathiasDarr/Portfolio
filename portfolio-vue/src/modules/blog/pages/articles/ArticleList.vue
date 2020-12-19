<template>
 <v-container>


    <v-list shaped>
      <v-subheader>Articles</v-subheader>
      <v-list-item-group
        color="primary"
      >
        <v-list-item
          v-for="item in articles"
          @click="navigate(item.article_id)"
          :key="item.article_id"
        >

        <ArticleCard :title="item.title"/>
        {{item.article_id}}
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>


 </v-container>
</template>

<script>
/* eslint-disable */

import ArticleCard from './ArticleCard'
import axios from 'axios';
import { mapGetters, mapActions } from "vuex";
import router from '../../../../services/router'

export default {
    created(){
      this.await_articles()
    },
    components:{
        ArticleCard
    },
    methods:{
      ...mapActions(["setArticles"]),

      navigate(article_id){
        console.log(article_id)
        router.push({name:'article', params:{article_id:article_id}})
      },

      async fetch_articles(){
            try{
                //var url = window.__runtime_configuration.apiEndpoint + '/categories'
                var url ='https://2qlgw486nb.execute-api.us-west-2.amazonaws.com/Prod/articles'
                const response = await axios.get(url)            
                var response_articles = JSON.parse(response.data.body)
                // this.setArticles(response_articles.articles)
                console.log(response_articles.articles)
                this.articles = response_articles.articles
            }catch(err){
                console.log(err)
            }
        },

        async await_articles(){
            await this.fetch_articles()
            // this.articles = this.getArticles
        },


    
    },
    computed: {
      // ...mapGetters(["getArticles"]),
    },
    data(){
        return {
          articles: []
          // articles: [{ title: 'Spark ML Pipelines'},
          //                {title: 'Spring Integration Tests'},
          //                {title: 'S3 Presigned Post URLs'},
          //                ]
        }
    }


}
</script>