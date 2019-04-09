<template>

    <div>
        <b-list-group id="cart">
            <h4>Shopping cart</h4>
            <div class = "alert alert-primary" v-if="cart.length == 0">Your cart is empty now</div>
            <b-list-group-item v-for="item in cart" :key="item.sid">
                <div>{{ item.name }}</div>
                <div>Quantity: {{ item.quantity }}</div>
                <div>Price: {{ item.price }}</div>
                <div><b-button-close @click="remove_from_cart_update(item.sid)" /></div>
            </b-list-group-item>
        </b-list-group>
        <b-button 
            class="float-right mt-2"
            v-if="cart.length > 0"
            variant="outline-primary"
            @click="handle_checkout"
        >Checkout</b-button>
    </div>

</template>

<script>
import { mapState, mapActions } from 'vuex'

import axios from 'axios'


export default {
    name: 'cart',
    computed: {
        ...mapState(['cart'])
    },
    
    methods: {

        ...mapActions(['remove_from_cart_update', 'fetch_data']),

        handle_checkout() {
            axios.post("/api/checkout")
                .then (_ => this.fetch_data())
                .catch(err => console.log(err.data))
        }

    }
}
</script>
