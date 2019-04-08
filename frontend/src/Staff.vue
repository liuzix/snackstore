<template>
    <div class="w-75 mx-auto position-relative">
        <div v-if="loading" 
            class="spinner-border position-absolute" 
            role="status"
            style="right:0"
        >
            <span class="sr-only">Loading...</span>
        </div>
        <b-pagination
            v-model="cur_page"
            :total-rows="total"
            :per-page="per_page"
            class="mt-4"
        ></b-pagination>
        <b-list-group id="snacks-list">
            <b-list-group-item v-for="snack in snacks" :key="snack.sid">
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

                <div><b-form-input v-on:blur= "edit_snack(snack.sid, snack.inventory)" v-model="snack.inventory"
                 v-autowidth="{maxWidth: '960px', minWidth: '20px', comfortZone: 0}" 
                placeholder="new inventory"></b-form-input></div>
                </hr>
            </b-list-group-item>
        </b-list-group>
        <b-pagination
            v-model="cur_page"
            :total-rows="total"
            :per-page="per_page"
            class="mt-4"
        ></b-pagination>
    </div>
</template>

<script>
import axios from "axios"
export default {
    name: "staff",
    data() {
        return {
            snacks: null,
            loading: true,
            err_msg: null,
            total: 0,
            per_page: 5,
            cur_page: 1
        }
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
        update_view: function() {
            this.loading = true
            axios.get('/staff_api/countsnacks')
                .then(response => {
                    this.total = response.data
                })
                .catch(error => console.log(error))
                


            axios.get("/staff_api/getsnacks/" + this.cur_page + "/" + this.per_page)
                .then(response => {
                    this.snacks = response.data
                    this.loading = false
                })
                .catch(error => console.log(error))
        },
        
        edit_snack: function(sid, qty) {
        
            axios.post('/staff_api/editsnacks', {'sid': sid, 'qty': qty})

                .catch(error => console.log(error))
        
        }
    }
}
</script>

