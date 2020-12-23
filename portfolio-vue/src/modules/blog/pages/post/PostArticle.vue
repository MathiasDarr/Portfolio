<template>
  <v-container>
    <v-layout>
  
      <v-flex md12>
      <v-container>
      
        <v-row>
          <v-col cols="12" sm="8">
      
          <h1> Post Article </h1>
          </v-col>
          <v-col cols="12" sm="4"
            >
              <v-btn color="primary" @click="LoadArticle('post_article')">Load Article </v-btn>
            </v-col>

          </v-row>


        </v-container>


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

    <v-container>
      
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

    </v-container>

    </v-flex>
    </v-layout>



  </v-container>
</template>

<script>
/* eslint-disable */

import {Editor, EditorContent, EditorMenuBar, EditorMenuBubble } from "tiptap"

import {Blockquote, CodeBlock, HardBreak, Heading, HorizontalRule, OrderedList, BulletList, ListItem, Code, Italic, Bold, Link, Strike, Image, Underline}from "tiptap-extensions"

import axios from 'axios';
import router from '../../../../services/router'



export default {
    name: "PostArticle",
    components:{
        EditorContent, EditorMenuBar, EditorMenuBubble
    },
    methods:{
        async PostArticle(){
            var url = 'https://2qlgw486nb.execute-api.us-west-2.amazonaws.com/Prod/articles'
            console.log("CATEGORY " + this.category)
            const res = await axios.put(url, { title: this.title, category:this.category, article_date:'12-22-2020', content:this.editor.getHTML() });
            // console.log(this.ediotr)
            router.push({name:'blog'})
        },
        async await_post(){
            this.PostArticle()
        },

        async add_image(image_url, height, width){
            // this.editor.setContent(this.editor.getHTML() + '<h1>FUCK</h1> <img src="' + this.image_url+ '" width=""500" height ="=2000" />'   )
            this.editor.setContent(this.editor.getHTML() + '<h1>FUCK</h1> <img src="' + this.image_url2+ '" width=""500" height ="=2000" />'   )

        },

        async select_image(){
            this.$prompt("Select Image").then((text) => {
                console.log(text)
                this.add_image(text)
            });
        },

        LoadArticle(){
            
        }
    },

    data(){
        return {



            introduction:` In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
                the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
                task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
                is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
                AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates. `,

            introduction_title: 'Project Desrption',
            motviation_title: 'Motivation',
            motivation:`Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
              in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me. `,
            methods_title: 'Methods',
            analysis: ` To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
              a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
              Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)`,
            analysis_title: 'Analysis',

            archticture_title: 'Query Service Archtiecture',
            archtiecture : `
              I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
              swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
              as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
              a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    

            `,
            snotel_project:`
              In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
              the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
              task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
              is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
              AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates.

              Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
              in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me.

              To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
              a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
              Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)

              I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
              swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
              as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
              a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    

            `,



            categories: ['Spark', 'Machine Learning', 'Serverless Application Model', 'Vue JS', 'Integration Testing', 'Spring Data'],
            category:'',
            image_url:'https://dakobed.s3-us-west-1.amazonaws.com/bonanza.jpg',
            image_url2:'https://dakobed.s3-us-west-1.amazonaws.com/chiwawa.jpg',
            content: `
            <p>Dear Hiring Manager</p><p>I am writing to you about my interest in the engineering position that I saw advertised on your website.&nbsp;</p><p>I am a software/data/cloud engineer located in the Seattle area looking for new oppertunities.&nbsp;</p><p>My most recent position was a QA engineer for QualityLogic contracted through Ultimate Software to&nbsp; write pytests and java tests to test API endpoints for a human resources software product.&nbsp; The tests that I wrote ran in a CI/CD environment.</p><p>I spent a year as a&nbsp; software developer at EigenVector Research developing a MatLab data analysis toolbox used by chemical engineers to analyze spectra.&nbsp; While at EigenVector, I developed a tool using angular to plot and monitor time series data that was being received from an instrument measuring chemical spectra. &nbsp; I also developed several file importers for different types of spectral data formats, wrote documentation, and provided customer support.</p><p>Since last being employed I have focused on my portfolio and developing my skills.&nbsp; I now have an AWS certification, and my github contributions grid is a patchwork quilt of dark green squares (though somewhat less so since I moved my less polished work to a different github account).&nbsp; Since having been declined for a role I had really wanted (for what in my mind was lack of scripting experience), I have made it a point to improve my bash skills, as well as awk, sed and regular expressions.&nbsp;</p><p>The technologies that I feel most confident in are Python, Java, Linux, Spring Boot, DynamoDB, AWS, CloudFormation, Boto3, Docker &amp; Vue JS.&nbsp; The technologies that I have experience with but am interested in getting more experience with in a professional environment are Spark, Kafka &amp; Airflow.</p><p>With a solid understanding of computer science fundamentals, modern machine learning techniques, knowledge of cloud application development, a strong passion for learning and the ability to write clean well tested and documented code, I am a strong candidate for this position.&nbsp;&nbsp;&nbsp;&nbsp;</p>
            
            
            `,

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

            <p>

            In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
                the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
                task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
                is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
                AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates.
            </p>

            <p>
            Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
            in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me.

            </p>
            <p>
              To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
              a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
              Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)
            </p>

            <p>
              I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
              swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
              as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
              a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    
            </p>
    

            <img src="https://dakobed.s3-us-west-1.amazonaws.com/bonanza.jpg" />
            `  
            })
        }
    },
    beforeDestroy() {
      this.editor.destroy()
    },
    
}
</script>