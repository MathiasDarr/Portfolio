<template>
  <v-container>
      Article Detail
      {{article_id}}
  </v-container>
</template>

<script>


export default {

    created(){
        console.log("HERLDF")
        this.article_id = this.$route.params.article_id
    },
    
    computed: {
      // ...mapGetters(["getArticles"]),
    },
    data(){
        return {
          article_detail: []
    
        }
    }


}
</script>