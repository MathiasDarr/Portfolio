<template>
 <v-container>


    <v-list shaped>
      <v-subheader>Articles</v-subheader>
      <v-list-item-group
        color="primary"
      >
        <v-list-item
          v-for="(item, i) in articles"
          :key="i"
        >

        <Article :title="item.title" />
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

import Article from './Article'


export default {
    components:{
        Article
    },

    data(){
        return {
          articles: [{ title: 'Spark ML Pipelines'},
                         {title: 'Spring Integration Tests'},
                         {title: 'S3 Presigned Post URLs'},
                        
                         ]


        }
    }


}
</script>