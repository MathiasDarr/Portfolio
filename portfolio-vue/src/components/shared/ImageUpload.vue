<template>
    <v-container>
        <v-card>
        <div class="container">
            <div class="large-12 medium-12 small-12 cell">
            
                <input type="file" id="file" ref="file" v-on:change="onFileChange()"/>
              <v-btn small color="primary" v-on:click="submit()">Upload Thumbnail</v-btn>
            </div>
        </div>
        <div class ="container">
            <div v-if="uploaded_file_url != ''">
                
                <v-img :src="uploaded_file_url"> </v-img>
                fuck
            </div>
            <div v-else>
                fdf 
            </div>

        </div>

        </v-card>


    </v-container>


</template>


<script>
/* eslint-disable */
import { mapGetters, mapActions } from "vuex";
import axios from 'axios';

export default {
    // https://dakobed-sqs-transform-bucket.s3-us-west-2.amazonaws.com/dakobedbard/snotel.png
    
    computed:{
      ...mapGetters(["getIdToken"]),
    },
    
    
    methods:{
        ...mapActions(["setImageUploadUrl"]),


        async fetch_presigned_url(file){
            try{
                var name = this.file.name
                var presignedurl ='https:/bpvjzngdjb.execute-api.us-west-2.amazonaws.com/Prod/signedURL' 
                var upload_verification_url ='https:/bpvjzngdjb.execute-api.us-west-2.amazonaws.com/Prod/upload/' 
                
                var body = {userID:'dakobedbard@gmail.com', filename:name}
                const response = await axios.post(presignedurl, body)

                var data = response.data.presigned 
                var key = data.fields.key
                console.log(data)
                console.log(data.url+key)
                let form = new FormData()
                Object.keys(data.fields).forEach(key=>form.append(key, data.fields[key]))
                form.append('file', this.file)
                let post_response = await fetch(data.url, {method:'POST', body: form})
                if (post_response.ok) { // if HTTP-status is 200-299
                    const verificaiton_response = await axios.post(upload_verification_url, {key:key})
                    this.uploaded_file_url = data.url + key
                    
                    
                    this.setImageUploadUrl(this.uploaded_file_url)
                } else {
                    alert("HTTP-Error: " + response.status);
                }
            }catch(err){
                console.log(err)
            }
        },

        async upload_file(){
            await this.fetch_presigned_url(file)
        },
        submit(){
          
          this.upload_file()
        },

        onFileChange(){
          this.file = this.$refs.file.files[0]          
        }

    },

    data(){
        return {
            file: '',
            uploaded_file_url: ''
        }
    }
}
</script>