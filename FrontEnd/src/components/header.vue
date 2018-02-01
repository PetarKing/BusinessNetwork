<template>
  <div id="hh">
	<header id="header">
		<div class="col-sm-2 col-xs-1" id="placeholder1"></div>
		<div class="col-sm-4 col-xs-6 center-block">
			<router-link to="/">
			<h3>BUSINESS NETWORK</h3>
			</router-link>
			</div>
						<div class="col-sm-2 col-xs-1"></div>
						<div class="col-sm-4 col-xs-5">
						<nav class="links">
							<ul>
								<li><router-link to="/"><strong>POSTS</strong></router-link></li>
								<li><router-link to="/users"><strong>USERS</strong></router-link></li>
							</ul>
						</nav>
						</div>
						<nav class="main">
							<dr text="" type="info" class="pull-right">
								<li><router-link to="/"><strong>POSTS</strong></router-link></li>
								<li><router-link to="/users"><strong>USERS</strong></router-link></li>
								</dr>
						</nav>
					</header>

  </div>

</template>

<script>
import Dropdown from 'vue-strap/src/Dropdown'

export default {
  name: 'hh',
  components:{
		alert: alert,
		'dr': Dropdown
	},
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
  h1{
  margin-top: 0;
  }

  li:hover strong{
  color: rgb(16, 180, 139);
  border-bottom: 2px solid rgb(2, 160, 107);
  }

  .main li{
  width: 100%;
  align-self: center;
  }

	#logo-img
	{
		margin-top:0.1em;
		max-height: 4em;
	}

	#header{
	 min-height: 4.2em;
	}

	h3{
		color: rgb(4, 156, 123);
		font-family:  Georgia, Serif;
		font-weight: bold; 
	}
</style>
