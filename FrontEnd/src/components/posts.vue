<template>
  <div id="posts">
  
    <div class="row" id="large">
  <div class="col-sm-8">
    <popover trigger="hover" effect="fade" placement="left" title="Likes" v-bind:content="post_data1.articles[0].likes">
    <a :href="post_data1.articles[0].url">
    <div class="image">

      <img class="img-top img-responsive" :src="post_data1.articles[0].urlToImage" alt="" />
      <div class="text">
      <h2 class="card-title"><span class="highlight">{{post_data1.articles[0].title}}</span></h2>
      <p class="card-text"><span class="highlight">{{post_data1.articles[0].description.slice(0, 100)}}...</span></p>
      </div>
</div>
</a>
    </popover>
  </div>

  <div class="col-sm-4">
    <div class="row">
      <popover trigger="hover" effect="fade" placement="right" title="Likes" v-bind:content="post_data2.articles[0].likes">
      <a :href="post_data2.articles[0].url">
    <div class="image">

      <img class="img-top-small img-responsive" :src="post_data2.articles[0].urlToImage" alt="" />
      <div class="text">
      <h4 class="card-title"><span class="highlight">{{post_data2.articles[0].title}}</span></h4>
      <p class="card-text"><span class="highlight">{{post_data2.articles[0].description.slice(0, 100)}}...</span></p>
      </div>
    </div>
    </a>
  </popover>

<popover trigger="hover" effect="fade" placement="right" title="Likes" v-bind:content="post_data3.articles[0].likes">
    <a :href="post_data3.articles[0].url">
     <div class="image">
      <img class="img-top-small img-responsive" :src="post_data3.articles[0].urlToImage" alt="" />
      <div class="text">
      <h4 class="card-title"><span class="highlight">{{post_data3.articles[0].title}}</span></h4>
      <p class="card-text"><span class="highlight">{{post_data3.articles[0].description.slice(0, 100)}} ...</span></p>
      </div>
    </div>

  </a>
</popover>
    </div>
    </div>
    </div>

    <div class="row" id="mini">
    <div class="col-xs-12 col-md-4" >
      <h1 class="ttl">Business Insider</h1>
      <div id="c1">
      <!-- Mini Post -->
      <div class="card" v-for="post in post_data1.articles" :key="post.url">
       <popover trigger="hover" effect="fade" placement="left" title="Likes" v-bind:content="post.likes">
        <a :href="post.url"><div class="image"><img class="card-img-top img-responsive" :src="post.urlToImage" alt=""/></div></a>
        <div class="card-block">
           <h4 class="card-title">{{post.title}}</h4>
          <p class="about">
            <span class="date">{{post.pub_date}}</span>
          </p>
           <p class="card-text">{{post.description.slice(0, 100)}}...</p> 
        </div>
        </popover>
    </div>
      </div>
   </div>  


    <div class="col-xs-12 col-md-4" >
      <h1 class="ttl">Bloomberg</h1>
      <div id="c2">
      <!-- Mini Post -->
      <div class="card" v-for="post in post_data2.articles" :key="post.url">
        <popover trigger="hover" effect="fade" placement="right" title="Likes" v-bind:content="post.likes">
        <a :href="post.url"><div class="image"><img class="card-img-top img-responsive" :src="post.urlToImage" alt=""/></div></a>
        <div class="card-block">
           <h4 class="card-title">{{post.title}}</h4>
          <p class="about">
            <span class="date">{{post.pub_date}}</span>
          </p>
           <p class="card-text">{{post.description.slice(0, 100)}}...</p>
        </div>
        </popover>
    </div>
      </div>
   </div>  


    <div class="col-xs-12 col-md-4" >
      <h1 class="ttl">CNBC</h1>
      <div id="c3">
      <!-- Mini Post -->
      <div class="card" v-for="post in post_data3.articles" :key="post.url">
        <popover trigger="hover" effect="fade" placement="right" title="Likes" v-bind:content="post.likes">
        <a :href="post.url"><div class="image"><img class="card-img-top-mini img-responsive" :src="post.urlToImage" alt=""/></div></a>
        <div class="card-block">
           <h4 class="card-title">{{post.title}}</h4>
          <p class="about">
            <span class="date">{{post.pub_date}}</span>
          </p>
           <p class="card-text">{{post.description.slice(0, 100)}}...</p>
        </div>
        </popover>
    </div>
      </div>
   </div>  
   
</div>
  <div class="row">
    <div class="col-4"/>
    <div class="col-4"><h5>Feed powered by <a href="https://newsapi.org">NewsAPI.org</a></h5></div>
    <div class="col-4"/>
  </div>

  </div>

</template>

<script>
  import {HTTP} from '../http-instance';
  import axios from 'axios';
  import Popover from 'vue-strap/src/Popover';
  
  export default {
  name: 'posts',
  components:{'popover': Popover},
  data: function () {
  return {
    likes_temp: "",
  errors:[],
  post:[],
  post_arrays1:{articles:[
      {pub_date: "",
      title: "",
      description: "",
      pub_date: "",
      url: ""}
    ]},
  post_arrays2:{articles:[
      {pub_date: "",
      title: "",
      description: "",
      pub_date: "",
      url: "test"}
    ]},
  post_arrays3:{articles:[
      {pub_date: "",
      title: "",
      description: "",
      pub_date: "",
      url: ""}
    ]},
  }
  },
  computed:{
   post_data1: function () {
  return this.post_arrays1;
  },
   post_data2: function () {
  return this.post_arrays2;
  },
   post_data3: function () {
  return this.post_arrays3;
  }
  },
  created(){
    var vue_instance = this;
  
  axios.get('https://newsapi.org/v2/top-headlines?' +
          'sources=business-insider&' +
          'apiKey=8ef9c5f35b1242b58fc8091992986eac')
  .then(response => {
  this.post_arrays1 = response.data;

   this.post_arrays1.articles.forEach(function(entry) {
    entry = vue_instance.getLikes(entry);
    });
    console.log(this.post_arrays1.articles[0]);
  })
  .catch(e => {
  console.log(e);
  this.errors.push(e);
  });

  axios.get('https://newsapi.org/v2/top-headlines?' +
          'sources=bloomberg&' +
          'apiKey=8ef9c5f35b1242b58fc8091992986eac')
  .then(response => {
  this.post_arrays2 = response.data;

  var vue_instance = this;
  this.post_arrays2.articles.forEach(function(entry) {
    entry = vue_instance.getLikes(entry);
    });
  })
  .catch(e => {
  console.log(e);
  this.errors.push(e);
  });

  axios.get('https://newsapi.org/v2/top-headlines?' +
          'sources=cnbc&' +
          'apiKey=8ef9c5f35b1242b58fc8091992986eac')
  .then(response => {
  this.post_arrays3 = response.data;

   this.post_arrays3.articles.forEach(function(entry) {
    entry = vue_instance.getLikes(entry);
    });
  })
  .catch(e => {
  console.log(e);
  this.errors.push(e);
  });
  },

  methods: {
    getLikes: function(entry){
    var likes_temp = "No one has like this post yet!";

    HTTP.get("likes?url="+entry.url)
    .then(response => {
    entry.likes = response.data;
    entry.title = entry.title+" ";
    return entry;
  })
  .catch(e => {
  console.log("Network Error!");
  entry.likes = "No likes yet!";
  return entry;
  });
    }
  }

}
</script>

<style scoped>
.center-block{
  margin-bottom: 2%;
}
#mini{
  margin-top: 5%;
}
#large{
  margin-top: 2%;
}
#posts{
  max-width: 1300px;
   display:block;
}
.card {
    margin-top: 5%;
    margin-bottom: 5%;
    font-size: 1em;
    overflow: visible;
    padding:  1px;
    border: none;
    border-radius: .28571429rem;
    box-shadow:   1px 3px   #d4d4d5,       1px #d4d4d5;
    max-width: 500px;
    
    
    margin-left:auto;
   margin-right:auto;
   display:block;
}

.card-block {
    font-size: 1em;
    position: relative;
    margin: -1px;
    padding: 1em;
    border: none;
    border-top: 1px solid rgba(34, 36, 38, .1);
    box-shadow: none;
    background: #fff;
}

h1{
  text-align: left;
}

.card-img-top{
      height: 300px;
      margin-left:auto;
   margin-right:auto;
   display:block;
}

#c1{
  border: 1px solid rgba(34, 36, 38, .1);
  border-left: none;
  padding-right: 5%;
}
#c2{
  border: 1px solid rgba(34, 36, 38, .1);
  padding-right: 5%;
  padding-left: 5%;
}
#c3{
  border: 1px solid rgba(34, 36, 38, .1);
  border-right: none;
  padding-left: 5%;
}

img{
  -webkit-transition: all  .5s linear;
          transition: all  .5s linear;
  -webkit-transform: scale3d(1, 1, 1);
          transform: scale3d(1, 1, 1);
}
.card:hover img{
  -webkit-transform: scale3d(1.2, 1.2, 1);
          transform: scale3d(1.2, 1.2, 1);
}

.image { 
   position: relative; 
   width: 100%; /* for IE 6 */
   overflow: hidden;
   border: 1px solid rgba(34, 36, 38, .1);
}

.image .text { 
   position: absolute;
  padding-right: 10%;
   bottom: 1%; 
   left:  5%; 
   width: 100%; 
}

.highlight { 
   background: rgba(2 , 2 , 2 , .5);
   color: white;
}

.img-top{
   height: 400px;
      margin-left:auto;
   margin-right:auto;
   display:block;
}
.img-top-small{
  height: 200px;
      margin-left:auto;
   margin-right:auto;
   display:block;
}

.image:hover img{
  -webkit-transform: scale3d(1.2, 1.2, 1);
          transform: scale3d(1.2, 1.2, 1);
}

h5{
  color: rgb(4, 110, 70);
}

  @media screen and (max-width: 991px) {

  #mini h1 {
  text-align: center;
  }
  }

  .date{
    color: #1E9 FF;
    font-weight: bold;
  }

  .about{
    color: gray;
  }

  .ttl{
    color:turquoise;
    font-weight: bold;
    font-style: italic;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

.btnText
 {
   color: white;
  }
</style>
