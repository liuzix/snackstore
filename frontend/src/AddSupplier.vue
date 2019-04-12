<template>

    <div>

        <b-card class="mt-3" header="Add supplier">
            <b-form  class="review-form" @submit.prevent="checkForm">
            
            
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
              <p v-if="errors.length">
                <b>Please correct the following error(s):</b>
                <ul>
                  <li v-for="error in errors">{{ error }}</li>
                </ul>
              </p>
        </b-card>

    </div>

</template>

<script>

import axios from 'axios'


export default {
    name: 'addSupplier',
    data() {
        return {
            errors: [],
            name: null, 
            address: null,
            phone_number: null
        }
    },

    methods: {
        send_form(name, address, phone_number) {
            this.loading = true;


            axios.post("/staff_api/addsuppliers", {'name': name, 'address': address, 'phone_number': phone_number})
                .then(response => {
                    this.loading = false
                })
                .then(_ => this.$emit('update') )
                .catch(error => console.log(error))
            
            this.clearData();
            
            
        },
        checkForm: function (e) {
              this.errors = [];
        
              if (!this.name) {
                this.errors.push("Name required.");
              }
              if (!this.phone_number) {
                this.errors.push('Phone number required.');
              } else if (!this.validPhoneNumber(this.phone_number)) {
                this.errors.push('Valid phone number required.');
              }
        
              if (!this.errors.length) {
                return true;
              }
        
              e.preventDefault();
              
              if (this.error.length == 0) {
                this.send_form(this.name, this.address, this.phone_number);
              }         
        },
        
        validPhoneNumber: function (phone_number) {
          var re = /\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*/;
          return re.test(phone_number);
          
        },
        
        clearData: function() {
            this.name = null;
            this.phone_number = null;
            this.address = null;
        }
    }
}
</script>
