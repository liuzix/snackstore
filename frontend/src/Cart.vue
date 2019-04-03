<template>
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
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: 'cart',
    computed: {
        ...mapState(['cart'])
    },
    
    methods: {
        ...mapActions(['remove_from_cart_update'])
    }
}
</script>
