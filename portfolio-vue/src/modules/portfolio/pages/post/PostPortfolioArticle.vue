<template>
  <v-container>
    <v-layout>
  
      <v-flex md12>
        <v-container>
  
          <v-row>
            <v-col cols="12" sm="12">
              <h1> Post Article </h1>
            </v-col>
          
          </v-row>
        </v-container>
        <v-card>
            <v-form>
              <v-container fluid>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-text-field label="Article Title" value="" v-model="title"></v-text-field>
                    </v-col>
                  <v-col class="d-flex" cols="12" offset="2" sm="3">
                    <v-select :items="categories" label="Article Category" v-model="category"></v-select>
                  </v-col>
                </v-row>
              </v-container>  
          </v-form>
        </v-card>


        
        <v-layout>
          <v-flex md9>
            <EditorComponent />
          </v-flex>
          <v-flex md3>
            <PostSidebar @addImage="onAddimage" @postEvent="onClickButton"/>
              <!-- <EditorComponent /> -->
          </v-flex>
        </v-layout>


    <!-- <v-container>
      
      <v-row>
        <v-col cols="12" sm="2">
            <v-btn color="primary" @click="add_image()">Add Image </v-btn>
        </v-col>

        <v-col cols="12" sm="2">
            <v-btn color="primary" @click="await_post()">Post Article </v-btn>
        </v-col>
      
        <v-col cols="12" sm="2">
            <v-btn color="primary" @click="select_image()">Select Image </v-btn>
        </v-col>
      
      </v-row>

    </v-container> -->

    </v-flex>
    </v-layout>



  </v-container>
</template>

<script>
/* eslint-disable */

import {Editor, EditorContent, EditorMenuBar, EditorMenuBubble } from "tiptap"

import {Blockquote, CodeBlock, HardBreak, Heading, HorizontalRule, OrderedList, BulletList, ListItem, Code, Italic, Bold, Link, Strike, Image, Underline}from "tiptap-extensions"

import EditorComponent from './EditorComponent'


import router from '../../../../services/router'
import { mapGetters, mapActions } from "vuex";

import PostSidebar from '../post/PostSidebar'


export default {
    name: "PostArticle",
    components:{
        EditorContent, 
        EditorMenuBar, 
        EditorMenuBubble, 

        EditorComponent,
        PostSidebar
    },
    computed:{
      ...mapGetters(["getIdToken"]),
    },
    methods:{

        async chooseMainImage(){},
        async uploadImage(){

        },
        async PostArticle(){
            var url = 'https://wnhvjytp6c.execute-api.us-west-2.amazonaws.com/Prod/articles'
            console.log("CATEGORY " + this.category)
            const res = await axios.put(url, { title: this.title, category:this.category, article_date:'12-22-2020', content:this.editor.getHTML() });
            // console.log(this.ediotr)
            router.push({name:'blog'})
        },
        async await_post(){
            this.PostArticle()
        },

        LoadArticle(){
            
        },

        submit(){
          
          this.upload_file()
        },

        onFileChange(){
          this.file = this.$refs.file.files[0]          
        },

        getClickEvent(data_object){
            console.log("I AM GETTING EMITTED FROM CHILD " + data_object)
            // this.$broadcast('await_post', data_object);
            // this.$refsgetEditorContentHtml
        },

        onClickButton(value){
          console.log(value)
          console.log(this.category)
          this.$emit('post_article',{'article_category': this.category, 'article_name':this.title})
        },

        onAddimage(data){
          console.log("THE DATA IS " + data)
          this.$emit('add_image', data)
        }





    },

    data(){
        return {

            file: '',
            data_object:Object,
            image_url:'https://dakobed.s3-us-west-1.amazonaws.com/bonanza.jpg',
            image_url2:'https://dakobed.s3-us-west-1.amazonaws.com/chiwawa.jpg',

            categories: ['Spark', 'Machine Learning', 'Serverless Application Model', 'Vue JS', 'Integration Testing', 'Spring Data', 'Data Pipelines'],
            category:'',
            title: 'First Article',

        }
    },
    // beforeDestroy() {
    //   this.editor.destroy()
    // },
    
}
</script>


