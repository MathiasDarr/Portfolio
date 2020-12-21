<template>
  <v-container>
      <h2> {{article_title}} </h2>

      <Paragraph v-bind:title = "paragraph_title" v-bind:text = paragraph />

      <Paragraph v-bind:title = "paragraph2_title" v-bind:text = paragraph2 />
  </v-container>
</template>

<script>

import Paragraph from '../../../../components/Paragraph'

export default {
    components:{
      Paragraph
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
          paragraph2: `The pruimary concern in relation data modeling are the relationships between entities`

        }
    }


}
</script>