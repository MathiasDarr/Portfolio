<template>
  <div>
     
      <v-layout>
      <ImageUpload />

      </v-layout>
        <v-layout>
    <v-container>
      <v-list>
          <!-- <v-list-item>
            <v-btn color="primary" @click="add_image()">Add Image </v-btn>
          </v-list-item> -->
          <v-list-item>
              <v-btn color="primary" @click="$emit('clickEvent', 'dfd')">Select Image </v-btn>
          </v-list-item>
          <v-list-item>
            <v-btn color="primary" @click="await_post()">Post Article </v-btn>    
          </v-list-item>
      </v-list>

    </v-container>
        </v-layout>

  </div>
</template>

<script>
/* eslint-disable */


import ImageUpload from './ImageUpload'
export default {
    components:{
        ImageUpload
    },
    methods:{
        // async add_image(image_url, height, width){
        //     // this.editor.setContent(this.editor.getHTML() + '<h1>FUCK</h1> <img src="' + this.image_url+ '" width=""500" height ="=2000" />'   )
        //     this.editor.setContent(this.editor.getHTML() + '<h1>FUCK</h1> <img src="' + this.image_url2+ '" width=""500" height ="=2000" />'   )

        // },

        async select_image(){
            this.$prompt("Select Image").then((text) => {
                console.log(text)
                this.add_image(text)
            });
        },

    },
    
}
</script>