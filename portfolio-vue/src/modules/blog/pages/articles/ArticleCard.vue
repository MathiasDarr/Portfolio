<template>
  <v-container>
    <v-card height="200" width="800">
      <v-card-title>
        {{ title }} 

      </v-card-title>
      <v-card-subtitle>
        {{ article_date }}
      </v-card-subtitle>
    </v-card>
  </v-container>    
</template>

<script>
export default {
    props:{
      title: String,
      article_date:String
    }
}
</script>
