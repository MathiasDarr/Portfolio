<template>
  <v-container>
    <v-layout>
      <v-flex md4>
        <PostArticleMenu />
      </v-flex>
      <v-flex md8>
        <h1> Post Article  dfdf </h1>


        <v-card>
            <div>
                <editor-menu-bar :editor="editor" v-slot="{commands, isActive}"> 
                    <div class ="menubar">
                        <button 
                        class="menubar__button"
                        :class="{ 'is-active': isActive.bold()}" @click="commands.bold"> Bold</button>
                        <button 
                            class="menubar__button" 
                            :class="{ 'is-active': isActive.underline() }"
                        > Underline </button>
                    </div>

                </editor-menu-bar>
                <editor-content class="editor__content" :editor="editor"/>
            </div>
        </v-card>

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
                new BulletList()

            ],
            content: `
            <h2> 
                Hi there,
            </h2>`  
            })
        }
    }
    
}
</script>