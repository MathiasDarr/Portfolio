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
            <PostSidebar  @addImage="onAddimage" @postEvent="onClickButton"/>
              <!-- <EditorComponent />  @postEvent="await_post"-->
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

import axios from 'axios';
import router from '../../../../services/router'
import { mapGetters, mapActions } from "vuex";

import PostSidebar from '../post/PostSidebar'


export default {

    categories: ['Spark', 'Machine Learning', 'Serverless Application Model', 'Vue JS', 'Integration Testing', 'Spring Data', 'Data Pipelines'],
    category:'',
    title: '',

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
            categories: ['Spark', 'Machine Learning', 'Serverless Application Model', 'Vue JS', 'Integration Testing', 'Spring Data', 'Data Pipelines'],
            category:'',
            title: 'First Blog Post Article',
            image_url:'https://dakobed.s3-us-west-1.amazonaws.com/bonanza.jpg',
            image_url2:'https://dakobed.s3-us-west-1.amazonaws.com/chiwawa.jpg',
            content: `
            <p>Dear Hiring Manager</p><p>I am writing to you about my interest in the engineering position that I saw advertised on your website.&nbsp;</p><p>I am a software/data/cloud engineer located in the Seattle area looking for new oppertunities.&nbsp;</p><p>My most recent position was a QA engineer for QualityLogic contracted through Ultimate Software to&nbsp; write pytests and java tests to test API endpoints for a human resources software product.&nbsp; The tests that I wrote ran in a CI/CD environment.</p><p>I spent a year as a&nbsp; software developer at EigenVector Research developing a MatLab data analysis toolbox used by chemical engineers to analyze spectra.&nbsp; While at EigenVector, I developed a tool using angular to plot and monitor time series data that was being received from an instrument measuring chemical spectra. &nbsp; I also developed several file importers for different types of spectral data formats, wrote documentation, and provided customer support.</p><p>Since last being employed I have focused on my portfolio and developing my skills.&nbsp; I now have an AWS certification, and my github contributions grid is a patchwork quilt of dark green squares (though somewhat less so since I moved my less polished work to a different github account).&nbsp; Since having been declined for a role I had really wanted (for what in my mind was lack of scripting experience), I have made it a point to improve my bash skills, as well as awk, sed and regular expressions.&nbsp;</p><p>The technologies that I feel most confident in are Python, Java, Linux, Spring Boot, DynamoDB, AWS, CloudFormation, Boto3, Docker &amp; Vue JS.&nbsp; The technologies that I have experience with but am interested in getting more experience with in a professional environment are Spark, Kafka &amp; Airflow.</p><p>With a solid understanding of computer science fundamentals, modern machine learning techniques, knowledge of cloud application development, a strong passion for learning and the ability to write clean well tested and documented code, I am a strong candidate for this position.&nbsp;&nbsp;&nbsp;&nbsp;</p>
            
            `,

            title: '',

        }
    },

    
}
</script>


