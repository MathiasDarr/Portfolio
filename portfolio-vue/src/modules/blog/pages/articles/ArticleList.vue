<template>
 <v-container>

    <v-list shaped>
      <v-subheader>Articles</v-subheader>
      <v-list-item-group
        color="primary"
      >
        <v-list-item
          v-for="item in articles"
          @click="navigate(item.article_id, item.content, item.article_date)"
          :key="item.article_id"
        >

        <ArticleCard :title="item.title" :article_date="item.article_date" :article_preview="item.preview" :category="item.category" />
        
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

import ArticleDetail from './ArticleDetail'
import ArticleCard from './ArticleCard'
import axios from 'axios';
import { mapGetters, mapActions } from "vuex";
import router from '../../../../services/router'

export default {
    created(){
      this.await_articles()
    },
    components:{
        ArticleCard,
        ArticleDetail
    },
    methods:{
      ...mapActions(["setArticles"]),

      navigate(article_id, article_content, article_date){
        console.log(article_id)
        router.push({name:'article', params:{article_id:article_id, content: article_content, article_date: article_date}})
      },

      async fetch_articles(){
            try{
                //var url = window.__runtime_configuration.apiEndpoint + '/categories'
                var url ='https://wnhvjytp6c.execute-api.us-west-2.amazonaws.com/Prod/articles'
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