<template>
  <v-container>
    <h2> {{article_title}} </h2>

    <p v-html="content"></p>

  </v-container>

</template>

<script>
export default {
    created(){

        this.article_id = this.$route.params.article_id
        this.article_title = "Apache Cassandra Data Modeling"
        console.log("the content is " + this.content)
    },
    
    props:{
        content: String
    },


    data(){
        return {
            html_string: `<h1> THIS IS RENDERED <h1>`

        }
    }
}
</script>