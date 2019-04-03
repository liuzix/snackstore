import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import store_comp from './Store.vue'
import login from './Login.vue'
import cart from './Cart.vue'
import axios from 'axios'
import store from './data_store.js'

Vue.use(BootstrapVue)
Vue.use(VueRouter)


Vue.component('store', store_comp)
Vue.component('login', login)
Vue.component('cart', cart)


const routes = [
    {path: '/store', component: store_comp},
    {
        path: '/',
        redirect: '/store'
    },
]

const router = new VueRouter({
    routes
})

var app = new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App,)
})
