<template>
  <v-container fluid="">
    <v-layout row wrap>
      <v-card flat>
       <v-card-title>
           Dakobed Products Store
       </v-card-title>
       <v-layout row>
        
        <template>

          <v-row>
          <v-col
            v-for="n in 9"
            :key="n"
            class="d-flex child-flex"
            cols="4"
          >
            <v-img
              :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
              :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
              aspect-ratio="1"
              class="grey lighten-2"
            >
              <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-col>
        </v-row>

        </template>


        
        
        <v-flex xs3 md3 offset-sm1 v-for="item in getProducts" v-bind:key=item.id>
            <ProductCard v-bind:productID="item.id" v-bind:productName="item.productName" 
            v-bind:imageURL="item.imageURL" v-bind:productPrice="item.price"/>
              <!-- <v-card >
                  <v-img :src="item.imageURL" height="200px" width="100"></v-img>
                  
              </v-card> -->
              
          </v-flex>

       </v-layout>

       <!-- <v-card-text>
           {{getProducts}}

       </v-card-text> -->
      </v-card>
        
          <!-- <v-flex md6 offset-1>

          </v-flex>
          <v-flex md3 offset-1>

            <v-card  tile flat >
    
              <v-btn icon>
                <router-link to="/cart">
                <v-icon  >mdi-cart</v-icon>
                </router-link>
              </v-btn>
        
            </v-card>
          </v-flex> -->


      </v-layout>
  </v-container>
</template>


<script>




import { mapGetters, mapActions } from "vuex";
import ProductCard from './ProductCard'

export default {
    components:{
        ProductCard
    },

    methods:{
        ...mapActions(["fetchProducts"]),
    },
    computed: {
        ...mapGetters(["getProducts"]),
    },
    created(){
        console.log("DFDFDF")
      this.fetchProducts();
    },
}
</script>