<template>
  <div>
     
      <v-layout>
      <ImageUpload />

      </v-layout>
        <v-layout>
    <v-container>
      <v-list>
          <v-list-item>
            <v-btn color="primary" @click="add_image()">Add Image </v-btn>
          </v-list-item>
          <!-- <v-list-item>
              <v-btn color="primary" @click="$emit('clickEvent', 'dfd')">Select Image </v-btn>
          </v-list-item> -->
          <v-list-item>
            <v-btn color="primary" @click="onClickPostArticle()">Post Article </v-btn>    
          </v-list-item>
      </v-list>

    </v-container>
        </v-layout>

  </div>
</template>

<script>
/* eslint-disable */


import ImageUpload from '../../../../components/shared/ImageUpload'
import { mapGetters, mapActions } from "vuex";

export default {
    components:{
        ImageUpload
    },
    methods:{
      ...mapActions(["setImageUploadUrl"]),
        async add_image(image_url){
            this.setImageUploadUrl(image_url)
            // this.editor.setContent(this.editor.getHTML() + '<h1>FUCK</h1> <img src="' + this.image_url+ '" width=""500" height ="=2000" />'   )
            // this.editor.setContent(this.editor.getHTML() + '<h1>FUCK</h1> <img src="' + this.image_url2+ '" width=""500" height ="=2000" />'   )
            // this.#emit('addImage', )
        },

        async select_image(){
            this.$prompt("Select Image").then((text) => {
                console.log(text)
                this.add_image(text)
            });
        },

        onClickPostArticle(event){
          this.$emit('postEvent', {first:'data'})
          // this.$broadcast('responsePaginated', response.data);
        }


    },
    
}
</script>