<template>
  <v-container>
      <h2> {{article_title}} </h2>

      <Paragraph v-bind:title = "paragraph_title" v-bind:text = paragraph />

      <Paragraph v-bind:title = "paragraph2_title" v-bind:text = paragraph2 />

      <vue-gist-embed :gistId="gistId"></vue-gist-embed>

  </v-container>
</template>

<script>

import Paragraph from '../../../../components/Paragraph'
import VueGistEmbed from 'vue-gist-embed';
export default {
    components:{
      Paragraph,
      VueGistEmbed
    },
    created(){
        console.log("HERLDF")
        this.article_id = this.$route.params.article_id
        this.article_title = "Apache Cassandra Data Modeling"
    },
    
    computed: {
      // ...mapGetters(["getArticles"]),
    },
    data(){
        return {
          article_detail: [],
          paragraph_title: "Apache Cassandra Data Modeling",
          paragraph: `Data modeling in Cassandra is very differant than data modeling relationally.`,
    
          paragraph2_title: "Relational Data Modeling",
          paragraph2: `The pruimary concern in relation data modeling are the relationships between entities.  Consider the case where we have an employee entity which has a foregin key relationship to a second entity, 'department`,

          paragraph3_title : "Spring JPA",
          paragraph3: `Spring Data JPA can be used to interface with a postgres table in the following manner.  In this tutorial we will set up a controller, a service, an entity class and a repository for querying the database.`,

          paragraph_4_title: "Spring Kafka Binder",
          gistId:'d271c02e6fbef12386d260e6f46fcbe4'

        }
    }

}
</script>