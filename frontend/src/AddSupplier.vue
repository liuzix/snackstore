<template>

    <div>
        <form class="review-form" @submit.prevent="checkForm">
        
          <p v-if="errors.length">
            <b>Please correct the following error(s):</b>
            <ul>
              <li v-for="error in errors">{{ error }}</li>
            </ul>
          </p>
          <p>
            <label for="name">Name:</label>
            <input id="name" v-model="name" placeholder="name">
          </p>
          
          <p>
            <label for="address">Address:</label>
            <input id="address" v-model="address" placeholder="address">
          </p>
          
          <p>
            <label for="phone_number">Phone Number:</label>
            <input id="phone_number" v-model="phone_number" placeholder="phone_number">
          </p>
              
          <p>
            <input type="submit" value="Submit">  
          </p>    
        
        </form>
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
                .then(_ => window.location.reload() )
                .catch(error => console.log(error))
            
                

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
              
              this.send_form(this.name, this.address, this.phone_number);
        },
        
        validPhoneNumber: function (phone_number) {
          var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return re.test(phone_number);
          
        }
    }
}
</script>
