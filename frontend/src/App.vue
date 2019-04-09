<template>
  <div>
    <b-navbar class="sticky-top" toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Snackstore</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="'store'">Store</b-nav-item>
          <b-nav-item :to="'staff'" v-if="user.type=='staff'">Staff</b-nav-item>


          <!--<b-nav-item :to="manage">Manage</b-nav-item>-->
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if="!logged_in" v-b-modal.modal-login>Login</b-nav-item>
          <b-nav-item-dropdown v-else right>
            <template slot="button-content">
              <em>{{user.name}}</em>
            </template>
            <b-dropdown-item v-on:click="sign_out">Sign out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

                  

    <b-modal
      id="modal-login"
      title="Signup or Login"
      @ok="(evt) => $refs.login_ref.handle_submit(evt)"
    >
      <login ref="login_ref"/>
    </b-modal>
   <router-view></router-view>
  </div>
</template>

<script>
import login from "./Login.vue";
import axios from "axios";
import { data_store } from "./data_store.js";
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "app",
  computed: {
    ...mapState(["user"]),
    ...mapGetters(['logged_in'])
  },

  methods: {
    ...mapActions(["fetch_data"]),
    sign_out() {
      axios.get("/api/user_signout").then(_ => window.location.reload());
    }
  },

  mounted() {
    this.fetch_data();
  }
};
</script>

<style>
body {
  font-family: "Lato", sans-serif !important;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1,
h2 {
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
