<template>
  <div id="app">
    <hh/>
    <router-view></router-view>
    <bot/>
  </div>

</template>

<script>
  import hh from './components/header';
  import bot from './components/bottom';
  
  export default {
  name: 'app',
  components:{
  'hh':hh,
  'bot': bot
  }
  }
</script>

<style>
    @import url("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css");
    @import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700|Raleway:400,800,900");

  /*
  Future Imperfect by HTML5 UP
  html5up.net | @ajlkn
  Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
  */

  /* Basic */

  @-ms-viewport {
  width: device-width;
  }

  body {
  -ms-overflow-style: scrollbar;
  }

  @media screen and (max-width: 480px) {

  html, body {
  min-width: 320px;
  }

  }

  body {
  background: #f4f4f4;
  }

  body.is-loading *, body.is-loading *:before, body.is-loading *:after {
  -moz-animation: none !important;
  -webkit-animation: none !important;
  -ms-animation: none !important;
  animation: none !important;
  -moz-transition: none !important;
  -webkit-transition: none !important;
  -ms-transition: none !important;
  transition: none !important;
  }


  /* Header */

  body {
  padding-top: 3.5em;
  }

  #header {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  -moz-justify-content: space-between;
  -webkit-justify-content: space-between;
  -ms-justify-content: space-between;
  justify-content: space-between;
  background-color: #ffffff;
  border-bottom: solid 1px rgba(160, 160, 160, 0.3);
  height: 3.5em;
  left: 0;
  line-height: 3.5em;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 10000;
  }

  #header a {
  color: inherit;
  text-decoration: none;
  }

  #header ul {
  list-style: none;
  margin: 0;
  padding-left: 0;
  }

  #header ul li {
  display: inline-block;
  padding-left: 0;
  }

  #header h1 {
  height: inherit;
  line-height: inherit;
  white-space: nowrap;
  }

  #header h1 a {
  font-size: 0.7em;
  }

  #header .links {
  -moz-flex: 1;
  -webkit-flex: 1;
  -ms-flex: 1;
  flex: 1;
  border-left: solid 1px rgba(160, 160, 160, 0.3);
  height: inherit;
  line-height: inherit;
  margin-left: 1.5em;
  overflow: hidden;
  padding-left: 1.5em;
  }

  #header .links ul li {
  border-left: solid 1px rgba(160, 160, 160, 0.3);
  line-height: 1;
  margin-left: 1em;
  padding-left: 1em;
  }

  #header .links ul li:first-child {
  border-left: 0;
  margin-left: 0;
  padding-left: 0;
  }

  #header .links ul li a {
  border-bottom: 0;
  font-family: "Raleway", Helvetica, sans-serif;
  font-size: 0.7em;
  font-weight: 400;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  }

  #header .links ul li:hover a {
  color:#1E90FF;
  }

  #header .main {
    margin-right: 1%;
    margin-top: 1%;
  height: inherit;
  line-height: inherit;
  text-align: right;
  }

  #header .main ul li > a:before {
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  font-family: FontAwesome;
  font-style: normal;
  font-weight: normal;
  text-transform: none !important;
  }

  #header .main ul li > a:before {
  display: block;
  height: inherit;
  left: 0;
  line-height: inherit;
  position: absolute;
  text-align: center;
  text-indent: 0;
  top: 0;
  width: inherit;
  }

@media screen and (max-width: 1300px) {
  #posts, #vesti, #takmicenja, #seminari{
    margin-left:2%;
   margin-right:2%;
}

  }

  @media screen and (max-width: 1100px) {

  #header .links {
  display: none;
  }
  #placeholder1{
    display: none;
  }

  }

  @media screen and (min-width: 1101px) {

  #header .main{
    display: none;
  }
  #posts, #vesti, #takmicenja, #seminari{
  margin-left:auto;
   margin-right:auto;
  }
  }

  @media screen and (max-width: 736px) {

  #header {
  height: 2.75em;
  line-height: 2.75em;
  }

  #header h1 {
  padding: 0 0 0 1em;
  }
  }
</style>
