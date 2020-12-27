<template>
  <div>

        <v-card flat>          
          <div class = "editor">

            <v-card > 
            <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
                <div class="menubar">
                  <v-icon name="mdi-account-multiple-outline" />
                  <button class="menubar__button" :class="{ 'is-active': isActive.bold() }" @click="commands.bold">
                      Bold
                  </button>

                </div>
            </editor-menu-bar>
            </v-card>
            <editor-content class="editor__content" :editor="editor"/>
    
          </div>
        </v-card>

  </div>
</template>


<script>
/* eslint-disable */
import {Editor, EditorContent, EditorMenuBar, EditorMenuBubble } from "tiptap"

import {Blockquote, CodeBlock, HardBreak, Heading, HorizontalRule, OrderedList, BulletList, ListItem, Code, Italic, Bold, Link, Strike, Image, Underline}from "tiptap-extensions"

import axios from 'axios';
import router from '../../../../services/router'
import { mapGetters, mapActions } from "vuex";
export default {
    components:{
        EditorContent, 
        EditorMenuBar, 
        EditorMenuBubble, 
    },
    methods:{
        async PostArticle(name, category){
            var url = 'https://kiyaefg4z8.execute-api.us-west-2.amazonaws.com/Prod/portfolio'
            console.log("THE IMAGE URL IS "  + this.getImageUrl)            
            // console.log("CATEGORY " + category)
            // // console.log("DATA OBJECT" + data_object.article_cateogry)
            // const res = await axios.put(url, { article_name: name, article_category:category,content:this.editor.getHTML() });
            // // console.log(this.ediotr)
            // router.push({name:'portfolio'})
        },


        async await_post(data_object){
          // console.log("I get called with" + data_object.article_name )            // this.PostArticle()
          // console.log("I GET CALLED WITH  " + data_object.article_category)
          await this.PostArticle(data_object.article_name, data_object.article_category)

        },


        getEditorContentHtml(){
            return this.editor.getHTML()
        },
        post_content(content_object){
          this.await_post(content_object)
        }

    },

    created(){
      this.$parent.$on('post_article', this.post_content )
    },

    mounted() {
        // this.bus.$on('submit', this.getEditorContentHtml)
    },  
    computed:{
      ...mapGetters(["getImageUrl"])
    },

    data(){
        return {
            editor: new Editor({
            extensions:[
                new Blockquote(),
                new BulletList(),
                new CodeBlock(),
                new Bold(),
                new HorizontalRule(),
                new HardBreak(),
                new Heading(),
                new OrderedList(),
                new Code(),
                new ListItem(),
                new Strike(),
                new Underline(),
                new BulletList(),
                new Image()
            ],
            content: `

            <h2> Project Description </h2>


            In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield of data science known as MIR (Music Information Retrieval). As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could get a transcription of what they are playing?
            

            <h3>
              Raw Audio Signal
            </h3>

  
            
            `  
            })
        }
    },
    beforeDestroy() {
      this.editor.destroy()
    },
    
}
</script>