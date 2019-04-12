<template>

    <div>
        <b-card class="mt-3" header="Add supplier">
            <b-form  class="review-form" @submit.prevent="send_form(name, address, phone_number)">
                <b-form-group label="Supplier Name">
                  <b-form-input id="name" v-model="name" />
                </b-form-group>
                <b-form-group label="Address">
                  <b-form-input id="address" v-model="address" />
                </b-form-group>
                <b-form-group label="Phone Number">
                  <b-form-input id="phone_number" v-model="phone_number" />
                </b-form-group>
                <b-button type="submit" variant="primary">submit</b-button>
            
            </b-form >
        </b-card>
    </div>

</template>

<script>

import axios from 'axios'


export default {
    name: 'addSupplier',
    data() {
        return {
            name: null, 
            address: null,
            phone_number: null
        }
    },

    methods: {
        send_form(name, address, phone_number) {
            this.loading = true


            axios.post("/staff_api/addsuppliers", {'name': name, 'address': address, 'phone_number': phone_number})
                .then(response => {
                    this.loading = false
                })
                .then(_ => this.$emit('update') )
                .catch(error => console.log(error))
            
                

        }
    }

}
</script>
