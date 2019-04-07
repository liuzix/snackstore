import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        cart: [],
        user: {}
    },

    getters: {
        logged_in(state) {
            return typeof state.user.login !== "undefined"
        }
    },

    mutations: {
        add_to_cart(state, {sid, price, name}) {
            const found = state.cart.findIndex(x => x.sid == sid)
            if (found == -1)
                state.cart.push({sid: sid, name: name, quantity: 1, price: price})
            else {
                Object.assign(state.cart[found], {quantity: state.cart[found].quantity + 1})
            }
        },

        remove_from_cart(state, sid) {
            const found = state.cart.findIndex(x => x.sid == sid)
            if (found >= 0) {
                state.cart.splice(found, 1)
            }
        },

        set_cart(state, cart) {
            state.cart = cart
        },

        set_user(state, user) {
            state.user = user
        }
    },

    actions: {
        fetch_data (context) {
            axios.get("/api/user_info")
                .then(res => {
                    if (!res.data.logged_in) return
                    console.log(res.data.data)
                    context.commit('set_cart', res.data.data.cart)
                    res.data.data.cart = undefined
                    context.commit('set_user', res.data.data)
                })
                .catch(err => {
                    console.log(err)
                })
        },

        update_cart (context) {
            axios.post("/api/upload_cart", context.state.cart)
                .catch(err => console.log(err))
        },

        add_to_cart_update(context, item) {
            context.commit('add_to_cart', item)
            context.dispatch('update_cart')
        },

        remove_from_cart_update(context, sid) {
            context.commit('remove_from_cart', sid)
            context.dispatch('update_cart')
        }
    }
})