<template>
    <div class="w-75 mx-auto position-relative">
        <div v-if="loading" 
            class="spinner-border position-absolute" 
            role="status"
            style="left:50%;"
        >
            <span class="sr-only">Loading...</span>
        </div>
        <b-pagination
            v-model="cur_page"
            :total-rows="total"
            :per-page="per_page"
            class="mt-4"
        ></b-pagination>

        <div class="row">
            <div class = "col-8">
                <b-list-group id="snacks-list">
                    <b-list-group-item v-for="snack in snacks" :key="snack.sid">
                        <div class="position-relative">
                            <div>
                                {{ snack.name }}
                                <div class="float-right">
                                    <b-badge v-if="snack.inventory> 0">In stock</b-badge>
                                    <b-badge v-else>Out of stock</b-badge>
                                </div>
                            </div>
                            <hr>
                            <div>Description: {{ snack.description}}</div>
                            <div>Price: {{ snack.cost }}</div>
                            <div>Inventory {{ snack.inventory }}</div>
                            <b-button variant="outline-primary"
                                class="position-absolute"
                                style="right:0; bottom:0;"
                                @click="(evt) => handle_buy({sid: snack.sid, name: snack.name, price: snack.cost})"
                            >Buy</b-button>
                        </div>
                    </b-list-group-item>
                </b-list-group>
                <b-pagination
                    v-model="cur_page"
                    :total-rows="total"
                    :per-page="per_page"
                    class="mt-4"
                ></b-pagination>
            </div>
            <div class="col-4"><cart /></div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import cart from "./Cart.vue"
import { mapMutations, mapGetters, mapActions } from 'vuex';

export default {
    name: "store",
    data() {
        return {
            snacks: null,
            loading: true,
            err_msg: null,
            total: 0,
            per_page: 5,
            cur_page: 1,
        }
    },

    computed: {
        ...mapGetters(['logged_in'])
    },

    watch: {
        cur_page: function(val) {
            this.update_view()
        }
    },

    mounted() {
        this.update_view()
    },

    methods: {
        ...mapActions(['add_to_cart_update']),
        update_view() {
            this.loading = true
            axios.get('/api/countsnacks')
                .then(response => {
                    this.total = response.data
                })
                .catch(error => console.log(error))

            axios.get("/api/getsnacks/" + (this.cur_page - 1) * this.per_page + "/" + this.per_page)
                .then(response => {
                    this.snacks = response.data
                    this.loading = false
                })
                .catch(error => console.log(error))
        },

        handle_buy(item) {
            if (this.logged_in) {
                this.add_to_cart_update(item)
            } else {
                alert("please log in first")
            }
        }
    }
}
</script>

