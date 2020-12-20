<template>
  <v-container>




    
    <v-layout row>
      <v-flex md2>

      </v-flex> 
      <v-flex md10>
        <div class="title font-weight-medium">
          <v-layout row>
            <v-flex md8>
              <v-card  tile flat>
                <v-card-text>
                  <v-card-title>
                    Mathias Darr
                  </v-card-title>
                  <v-card-subtitle>
                      {{ title }}
                  </v-card-subtitle>
                  <v-divider></v-divider>
                  <Paragraph v-bind:title = "''" v-bind:text = porfolio_introduction />


                </v-card-text>
              </v-card>
            </v-flex>

            <v-flex md4>
              <v-card  tile flat >
                <v-img :src="'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg'" height="700px" width="560"></v-img>
              </v-card>
            </v-flex>
          </v-layout>
        
        </div>
      </v-flex>
    </v-layout> 
  </v-container>
</template>

<script>

import { mapGetters } from "vuex";
// import Paragraph from '../../../components/shared/Paragraph'

// import axios from 'axios';
// import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
// import { CognitoAuth } from 'amazon-cognito-auth-js'

import Paragraph from '../../../components/Paragraph'

export default {
  
  components:{
    Paragraph
  },

  methods:{
  },
  created(){
    var name = "mddarr@gmail.com"
    var split = name.split("@")
    console.log("Welcome " + split[0])
    console.log("welcome..")

  },
  data(){
    return {
      title: 'Software, Data & Cloud Engineer.',

      porfolio_introduction:`I am a talented engineer in  Seattle looking for junior/mid-level opportunities in the Seattle area or remote.  I have a 
      strong passion for learning, ability to learn new technologies quickly, and a willingess to embrace challenges.   
      `,

      introduction_title: 'Bio',
      technologies: [
        "Vuejs, Vuetify, Vuex, Axios, D3js",
        "Sring Boot",
        "Keras Deep Learning Library",
        "Librosa Audio Processing Library",
        "Kafka & Spark Streaming ",
        "PySpark, AWS EMR, Airflow",

        "AWS Serverless Application Model, API Gateway, Lambda, Simple Queue Service, Cognito",
        "AWS EC2, DynamoDB, S3",
        "AWS Elastic Container Service, Elastic Container Repository",
        "ElasticSearch",
        "Docker"
      ],
      link:'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-vue',
      link_title: 'Vue Application',
    }
  },
  computed: {
    ...mapGetters(["getLoggedIn","getJwtAccessToken", "getIdToken"]),

  },
}
</script>

<style>
code {
  font-family: Consolas,"courier new";
  color: crimson;
  background-color: #f1f1f1;
  padding: 2px;
  font-size: 105%;
}
</style>