<template>
  <v-container>
    <v-layout>
      <v-flex md4>
        <PostArticleMenu />
      </v-flex>
      <v-flex md8>
        

      <v-container>
      
        <v-row>
          <v-col cols="12" sm="8">
        
          <h1> Post Article  dfdf </h1>

          </v-col>


          <v-col cols="12" sm="4"
            >
              <v-btn color="primary" @click="LoadArticle()">Load Article </v-btn>
            </v-col>

          </v-row>


        </v-container>


        <v-card>
          <div>
            
            <v-form>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="12"
                    >
                <v-text-field
                 label="Article Title"
                 value=""
                 v-model="title"
                 ></v-text-field>
              </v-col>
            </v-row>


          </v-container>
  


  
        </v-form>
                
                
                            
                <!-- <editor-menu-bar :editor="editor" v-slot="{commands, isActive}"> 
                    <div class ="menubar">
                        <button 
                        class="menubar__button"
                        :class="{ 'is-active': isActive.bold()}" @click="commands.bold"> Bold</button>
                        <button 
                            class="menubar__button" 
                            :class="{ 'is-active': isActive.underline() }"
                        > Underline </button>
                    </div>

                </editor-menu-bar> -->
                <editor-content class="editor__content" :editor="editor"/>
            </div>
        </v-card>

    <v-container>
      
      <v-row>
        <v-col
          cols="12"
          sm="3"
        >
        
            <v-btn color="primary" @click="SaveArticle()">Save Article </v-btn>

        </v-col>


        <v-col
          cols="12"
          sm="6"
        >
            <v-btn color="primary" @click="PostArticle()">Post Article </v-btn>
        </v-col>

      </v-row>


    </v-container>

    </v-flex>
    </v-layout>



  </v-container>
</template>

<script>
/* eslint-disable */

import {Editor, EditorContent, EditorMenuBar, EditorMenuBubble } from "tiptap"

import {Blockquote, CodeBlock, HardBreak, Heading, HorizontalRule, OrderedList, BulletList, ListItem, Code, Italic, Bold, Link, Strike, Underline} from "tiptap-extensions"

import PostArticleMenu from './PostArticleMenu'

export default {
    name: "PostArticle",
    components:{
        EditorContent, EditorMenuBar, EditorMenuBubble, PostArticleMenu
    },
    methods:{
        PostArticle(){
            console.log(this.title)
            // console.log(this.ediotr)
            console.log(this.editor.getHTML())
        },
        LoadArticle(){
            
        }
    },


    data(){
        return {
            title: '',
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
                new BulletList()

            ],
            content: `





            This is where you type your article.
            `  
            })
        }
    }
    
}
</script>