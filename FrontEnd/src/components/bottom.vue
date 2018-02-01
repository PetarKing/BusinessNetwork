<template>
  <div id="bot">
    <footer id="myFooter">
        <div class="container-fluid">
            <div class="row">
                <div class="col-2"/>
                 <div class="col-8">
                 <a href="http://30hills.com/"><img id="image" class="img-responsive center-block" src="https://image-store.slidesharecdn.com/550eb66e-97dc-43e6-ae35-ecb4c9caf236-original.jpeg" alt=""/></a>
                 </div>
                 <div class="col-2"/>
            </div>
        </div>
        <div class="footer-copyright">
            <p>Copyright © 2018 , Petar Nedeljković</p>
        </div>
    </footer>
  </div>

</template>

<script>
export default {
  name: 'bot',
  components:{},
  data: function () {
    return {
  }
  },
  methods:
{

}
}
</script>

<style scoped>

#col1{
   align-content: center;
}
#col2{
   margin-top: 20px;
}
#myFooter {
    margin-top: 2.5%;
    background-color: rgb(0, 90, 71);
    color: white;
    padding-top: 1em;
}

#myFooter .footer-copyright {
    background-color: rgb(4, 65, 51);
    padding-top: 3px;
    padding-bottom: 3px;
    text-align: center;
}

#myFooter .row {
    margin-bottom: 30px;
}


#myFooter .footer-copyright p {
    margin: 10px;
    color: #ccc;
}

#myFooter h5 {
    font-size: 15px;
    color: white;
    font-weight: bold;
}

#list{
  
  list-style-type: none;
  font-size: 15px;
  color: white;
  font-weight: bold;
}

@media screen and (max-width: 767px) {
    #myFooter {
        text-align: center;
    }
}


/* CSS used for positioning the footers at the bottom of the page. */
/* You can remove this. */

#myFooter{
   flex: 0 0 auto;
   -webkit-flex: 0 0 auto;
}

#creditText{
    font-size: 0.8em;
}
</style>
