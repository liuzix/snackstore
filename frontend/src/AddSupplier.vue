<template>

    <div>
        <form class="review-form" @submit.prevent="send_form(name, address, phone_number)">
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
                .then(_ => window.location.reload() )
                .catch(error => console.log(error))
            
                

        }
    }

}
</script>
