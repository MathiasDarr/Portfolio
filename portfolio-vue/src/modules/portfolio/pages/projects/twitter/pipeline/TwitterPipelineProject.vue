<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <ProjectList />
      </v-flex>
      <v-flex md7>
        <h1> This is the Twitter Pipeline Project </h1>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>

import ProjectList from '../../../ProjectList'

export default {
    components:{
        ProjectList
    }
}
</script>