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


export default {
    components:{
        EditorContent, 
        EditorMenuBar, 
        EditorMenuBubble, 
    },
    methods:{
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


        getEditorContentHtml(){
            return this.editor.getHTML()
        },
        add_image_to_html(data){
          console.log("DOWNSTREAM " + this.getImageUrl)
          // console.log("THE IMAGE URL IS " + JSON.stringify(data))
          this.editor.setContent(this.editor.getHTML() + '<img src="' + this.getImageUrl +  '"/>'   )
        }
        
        
    },

    created(){
      this.$parent.$on('post_article', this.post_content )
      this.$parent.$on('add_image', this.add_image_to_html)
    },

    mounted() {

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


            In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing and instrumentand 
            

            
            `  
            })
        }
    },
    beforeDestroy() {
      this.editor.destroy()
    },
    
}
</script>