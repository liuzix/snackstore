<template>

    <div>
        <b-card no-body>
            <b-tabs card>
                  <b-tab title="Customer Orders" active>
                    <div class = "col-8">
                        <b-list-group id="orders-list">
                        
                            <b-list-group-item v-for="order in orders" :key="order.oid">
                                <div>
                                    {{ order.name }}
                                    <div class="float-right">
                                        <b-badge v-if="order.status == 'complete'">Complete</b-badge>
                                        <b-badge v-else> Incomplete </b-badge>
                                    </div>
                                </div>
                                <hr>
                                <div>Date: {{ order.date}}</div>
                                <div>Address: {{ order.address }}</div>    
                                
                                <div id="delete">
                                  <b-button variant="warning" v-on:click="delete_order(order.oid)">Delete this Order</b-button>
                                </div>     
                                                                                      
                                </hr>
                            </b-list-group-item>
                        </b-list-group>
                        <b-pagination
                            v-model="cur_page_orders"
                            :total-rows="total_orders"
                            :per-page="per_page_orders"
                            class="mt-4"
                        ></b-pagination>
                    </div>                    
                  </b-tab>
                  
                  <b-tab title="Inventory">

                    <div class = "col-8">
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
                                      
                  </b-tab>
                  <b-tab title="Supplier" active>
                  <div class="row">
                    <div class = "col-8">
                        <b-list-group id="suppliers-list">
                        
                            <b-list-group-item v-for="supplier in suppliers" :key="supplier.spid">
                                <div>
                                    {{ supplier.name }}
                                    <div class="float-right">
                                        <b-badge v-if="supplier.status == 'active'">Active</b-badge>
                                        <b-badge v-else> Inactive </b-badge>
                                    </div>
                                </div>
                                <hr>
                                <div>Address: {{ supplier.address}}</div>
                                <div>Phone Number: {{ supplier.phone_number}}</div>
                                <div>maintainer: {{ supplier.sname }}</div>                               
                                </hr>
                            </b-list-group-item>
                        </b-list-group>
                        <b-pagination
                            v-model="cur_page_suppliers"
                            :total-rows="total_suppliers"
                            :per-page="per_page_suppliers"
                            class="mt-4"
                        ></b-pagination>
                    </div>  
                <div class="col-4"><addSupplier /></div>   
                </div>               
                  </b-tab>
                  
              </b-tabs>
        </b-card>           
    </div>
</template>

<script>
import axios from "axios"
import addSupplier from "./AddSupplier.vue"
import { mapMutations, mapGetters, mapActions } from 'vuex';

export default {
    name: "staff",
    data() {
        return {
            orders: null, 
            snacks: null,
            suppliers: null, 
            loading: true,
            err_msg: null,
            total: 0,
            total_orders:0,
            total_suppliers: 0,
            per_page: 5,
            per_page_orders: 5,
            per_page_suppliers: 5,
            cur_page: 1,
            cur_page_orders: 1,
            cur_page_suppliers: 1 
        }
    },
    
    

    computed: {
        ...mapGetters(['logged_in'])
    },

    watch: {
        cur_page: function(val) {
            this.update_view()
            
        },
        cur_page_orders: function(val) {
            this.update_orders()
            
        },
        cur_page_suppliers: function(val) {
            this.update_suppliers()
            
        }
    },

    mounted() {
        this.update_view()
        this.update_orders()
        this.update_suppliers()
    },

    methods: {
        ...mapActions(),
        update_view() {
            this.loading = true
            axios.get('/staff_api/countsnacks')
                .then(response => {
                    this.total = response.data
                })
                .catch(error => console.log(error))

            axios.get("/staff_api/getsnacks/" + (this.cur_page - 1) * this.per_page + "/" + this.per_page)
                .then(response => {
                    this.snacks = response.data
                    this.loading = false
                })
                .catch(error => console.log(error))
                

        },
        
        edit_snack: function(sid, qty) {
        
            axios.post('/staff_api/editsnacks', {'sid': sid, 'qty': qty})

                .catch(error => console.log(error))
        
        },
        
        delete_order: function(oid) {
        
        
        
            axios.post('/staff_api/deleteorder', {'oid': oid})
                .then (_ => window.location.reload())
                .catch(error => console.log(error))
            
        },
        
        update_orders() {
            this.loading = true
            axios.get('/staff_api/countorders')
                .then(response => {
                    this.total_orders = response.data
                })
                .catch(error => console.log(error))

            axios.get("/staff_api/getorders/" + (this.cur_page_orders - 1) * this.per_page_orders + "/" + this.per_page_orders)
                .then(response => {
                    this.orders = response.data
                    this.loading = false
                })
                .catch(error => console.log(error))
                

        },
        
        update_suppliers() {
            this.loading = true
            axios.get('/staff_api/countsuppliers')
                .then(response => {
                    this.total_suppliers = response.data
                })
                .catch(error => console.log(error))

            axios.get("/staff_api/getsuppliers/" + (this.cur_page_suppliers - 1) * this.per_page_suppliers + "/" + this.per_page_suppliers)
                .then(response => {
                    this.suppliers = response.data
                    this.loading = false
                })
                .catch(error => console.log(error))
                

        },
        


    }
}
</script>

