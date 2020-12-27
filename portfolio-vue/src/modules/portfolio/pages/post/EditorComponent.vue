<template>
  <div>

        <v-card flat>
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
        getEditorContentHtml(){
            return this.editor.getHTML()
        }
    },

    mounted() {
        // this.bus.$on('submit', this.getEditorContentHtml)
    },  

    data(){
        return {
            categories: ['Spark', 'Machine Learning', 'Serverless Application Model', 'Vue JS', 'Integration Testing', 'Spring Data', 'Data Pipelines'],
            category:'',
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
                new BulletList(),
                new Image()
            ],
            content: `

            <h2> Project Description </h2>


            In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield of data science known as MIR (Music Information Retrieval). As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could get a transcription of what they are playing?
            

            <h3>
              Raw Audio Signal
            </h3>



            <h3>
              Spectogram showing energy located in frequency bins over time intervals 
            </h3>
            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/screenshot.png" width="740" height="350">
            
            
            <h2> Methods </h2>
            
            I attempt to reproduce the neural network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.
            
            <h3>
              Network Architecture
            </h3>
            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/cnn.png" width="560" height="320">
            
            <h3>
              Data Preprocessing

            </h3>

            <p>
            In order to normalize the data, the mean value (for each frequency bin of the spectogram) taken over all of the training data must be calculated.
            Since the data is too large to fit into memory, I implemented an algorithm known as Welford's algorithm, an iterative algorithm which calculates the running mean of a dataset such that not all of the data must be loaded into memory at once.

            </p>
            
            <h3>
              Training the neural network
            </h3>
            
            <p>
            The transforms and processed annotation numpy arrays are saved to S3 from where they are downloaded to an EC2 GPU instance.  The data is fed into a Keras generator (fit generator API) for training the neural network.  

   
            </p>

            <h3>
              Results
            </h3>
            <p>
            As of right now, the neural network was unable to make proper predictions..  I'm not entirely sure where I've gone wrong.
            </p>

            
            `  
            })
        }
    },
    beforeDestroy() {
      this.editor.destroy()
    },
    
}
</script>