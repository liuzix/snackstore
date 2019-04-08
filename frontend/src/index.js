import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'

import App from './App.vue'
import staff from './Staff.vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import store_comp from './Store.vue'
import login from './Login.vue'
import cart from './Cart.vue'
import axios from 'axios'
import store from './data_store.js'
import VueInputAutowidth from 'vue-input-autowidth'



Vue.use(VueInputAutowidth)
Vue.use(BootstrapVue)
Vue.use(VueRouter)
Vue.component(store)
Vue.component("staff", staff)

Vue.component('store', store_comp)
Vue.component('login', login)
Vue.component('cart', cart)


const routes = [
    {path: '/store', component: store_comp},
    {
        path: '/',
        redirect: '/store'
    },
    {path: '/staff', component: staff}

]

const router = new VueRouter({
    routes
})

var app = new Vue({
    el: '#app',
    staff,
    store,
    router,
    render: h => h(App,)
})
