<template>
<div>
  <b-navbar class="sticky-top" toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">Snackstore</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item :to="'store'">Store</b-nav-item>
        <b-nav-item :to="'staff'">Staff</b-nav-item>
        <!--<b-nav-item :to="manage">Manage</b-nav-item>-->
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template slot="button-content"><em>User</em></template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <router-view></router-view>
</div>

</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Snackstore?'
    }
  }
}
</script>

<style>
body {
  font-family: 'Lato', sans-serif !important;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}

a {
  color: #42b983;
}
</style>
