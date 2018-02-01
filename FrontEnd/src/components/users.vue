<template>
  <div id="users" class="grid">

   <div id="main">
     <div class="row"  v-show="!seleced">
       <div class="col-2"/>
     <div class="col-8"><input id="inp" v-model="query"/>
     </div>
        <div class="col-2"/>
    </div>

    <div class="row" v-show="seleced">
    <div class="col-5"/>
    <div class="col-2">
      <div>
        <h3>{{user_details.firstName}}'s connections:</h3>
      </div>
      <div class="funkyradio">
       
        <div class="funkyradio-primary">
            <input @click="change_level(1)" type="radio" name="radio" id="first" checked/>
            <label for="first">1-st</label>
        </div>
        <div class="funkyradio-success">
            <input @click="change_level(2)" type="radio" name="radio" id="second" />
            <label for="second">2-nd</label>
        </div>
        <div class="funkyradio-danger">
            <input @click="change_level(3)" type="radio" name="radio" id="suggested" />
            <label for="suggested">Suggested</label>
        </div>
   </div> 
  </div>
  <div class="col-5"/>

    </div>
  
        <div class="row">
        <div class="col-2"/>
      <div class="card-group  col-8">
  
  <div class="card" v-for="user in user_data" v-bind:key="user.id"  @click="user_selected(user.id)">
    <!--Card image-->
      <img  class="card-img-top" v-show="user.gender=='male'" src="../assets/male.png" alt="">
      <img  class="card-img-top" v-show="user.gender=='female'" src="../assets/female.png" alt="">

    <!--Card content-->
    <div class="card-block">
        <!--Title-->
        <h4 class="card-title">{{user.firstName}} {{user.surname}}</h4>
        <!--Text-->
        <p class="card-text"><i>{{user.gender}}   /  {{user.age}}</i></p>
    </div>

</div>
      </div>
<div class="col-2"/>
      </div>

   </div>
  </div>

</template>

<script>
  import {HTTP} from '../http-instance';
  
  export default {
  name: 'users',
  data: function () {
  return {
  errors:[],
  user_array:[
      {

      }
    ],
  seleced: false,
  query: "",
  current_id: 1,
  user_details: {firstName: ""},
  }
  },
  computed:{
   user_data: function () {
  return this.user_array;
  },
  user_current: function () {
  return this.user_details;

  }
  },
  created(){
  HTTP.get('search')
  .then(response => {
  this.user_array = response.data;
  console.log(this.user_array);
  })
  .catch(e => {
  console.log(e);
  this.errors.push(e);
  });
  },
  watch:{
    query: function(value){
      this.search(value);
    }
  },
  methods: {
    search: function(query){
    HTTP.get("search?query="+query)
  .then(response => {
  this.user_array = response.data;
  })
  .catch(e => {
  console.log("Network Error!");
  console.log(e);
  });
    },

    user_selected: function(id){
      HTTP.get("user?id="+id)
  .then(response => {
  this.seleced = true;
  this.current_id = id;
  this.user_details = response.data;
  document.getElementById("first").checked = true;
  document.getElementById("second").checked = false;
  document.getElementById("suggested").checked = false;
  this.change_level(1);
  })
  .catch(e => {
  console.log("Network Error!");
  console.log(e);
  });

    },

  change_level: function(level){
    if(level != "3"){
      console.log(this.current_id);
    HTTP.get("friends?level="+level+"&id="+this.current_id)
  .then(response => {
  this.user_array = response.data;
  })
  .catch(e => {
  console.log("Network Error!");
  console.log(e);
  });
  }
  else{
    HTTP.get("suggest?id="+this.current_id)
  .then(response => {
  this.user_array = response.data;
  })
  .catch(e => {
  console.log("Network Error!");
  console.log(e);
  });
  }
  }
  }

}
</script>

<style scoped>
#main{
  margin-top: 50px; 
  width: 100vw;
  margin-bottom: 20px;
}

#inp{
  width: 60%;
  margin-left: 15%;
  margin-bottom: 2%; 
  border: 2px solid rgb(27, 219, 178);
}

h3{
  color: rgb(4, 156, 123);
}
.card{
  max-width: 256px;
  margin: auto; 
}

.card:hover img {
	opacity: 1;
	-webkit-animation: flash 2.5s;
	animation: flash 2.5s;
}
@-webkit-keyframes flash {
	0% {
		opacity: .4;
	}
	100% {
		opacity: 1;
	}
}
@keyframes flash {
	0% {
		opacity: .4;
	}
	100% {
		opacity: 1;
	}
}

.card{
  margin-bottom: 10px;
}
.funkyradio div {
  margin-bottom: 20px;
  clear: both;
  overflow: hidden;
}

.funkyradio label {
  width: 100%;
  border-radius: 3px;
  border: 1px solid #D1D3D4;
  font-weight: normal;
}

.funkyradio input[type="radio"]:empty,
.funkyradio input[type="checkbox"]:empty {
  display: none;
}

.funkyradio input[type="radio"]:empty ~ label,
.funkyradio input[type="checkbox"]:empty ~ label {
  position: relative;
  line-height: 2.5em;
  text-indent: 3.25em;
  margin-top: 2em;
  cursor: pointer;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

.funkyradio input[type="radio"]:empty ~ label:before,
.funkyradio input[type="checkbox"]:empty ~ label:before {
  position: absolute;
  display: block;
  top: 0;
  bottom: 0;
  left: 0;
  content: '';
  width: 2.5em;
  background: #D1D3D4;
  border-radius: 3px 0 0 3px;
}

.funkyradio input[type="radio"]:hover:not(:checked) ~ label,
.funkyradio input[type="checkbox"]:hover:not(:checked) ~ label {
  color: #888;
}

.funkyradio input[type="radio"]:hover:not(:checked) ~ label:before,
.funkyradio input[type="checkbox"]:hover:not(:checked) ~ label:before {
  content: '\2714';
  text-indent: .9em;
  color: #C2C2C2;
}

.funkyradio input[type="radio"]:checked ~ label,
.funkyradio input[type="checkbox"]:checked ~ label {
  color: #777;
}

.funkyradio input[type="radio"]:checked ~ label:before,
.funkyradio input[type="checkbox"]:checked ~ label:before {
  content: '\2714';
  text-indent: .9em;
  color: #333;
  background-color: #ccc;
}

.funkyradio input[type="radio"]:focus ~ label:before,
.funkyradio input[type="checkbox"]:focus ~ label:before {
  box-shadow: 0 0 0 3px #999;
}

.funkyradio-default input[type="radio"]:checked ~ label:before,
.funkyradio-default input[type="checkbox"]:checked ~ label:before {
  color: #333;
  background-color: #ccc;
}

.funkyradio-primary input[type="radio"]:checked ~ label:before,
.funkyradio-primary input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #337ab7;
}

.funkyradio-success input[type="radio"]:checked ~ label:before,
.funkyradio-success input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #5cb85c;
}

.funkyradio-danger input[type="radio"]:checked ~ label:before,
.funkyradio-danger input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #d9534f;
}

.funkyradio-warning input[type="radio"]:checked ~ label:before,
.funkyradio-warning input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #f0ad4e;
}

.funkyradio-info input[type="radio"]:checked ~ label:before,
.funkyradio-info input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #5bc0de;
}
</style>
