<template>
  <v-container>
    <v-card height="200">
      <v-card-title>
        {{ title }} 

      </v-card-title>
    </v-card>
  </v-container>    
</template>

<script>
export default {
    props:{
      title: String
    }
}
</script>
