<template>
  <div>
    <p :v-html="content"></p>
  </div>    
</template>

<script>

export default {
    created(){
        this.content = content
    },
    props:{
        content: String
    }

}
</script>