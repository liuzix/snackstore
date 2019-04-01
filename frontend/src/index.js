import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'
import store from './Store.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueRouter)
Vue.component(store)


const routes = [
    {path: '/store', component: store},
]

const router = new VueRouter({
    routes
})


new Vue({
    el: '#app',
    router,
    render: h => h(App)
})