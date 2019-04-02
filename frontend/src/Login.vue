<template>
    <div>
        <b-form-group label="Login name:" label-for="input-1">
            <b-form-input v-model="login_name" id="input-1" />
        </b-form-group>
        <b-form-group label="Real name:" label-for="input-2">
            <b-form-input v-model="name" id="input-2" />
        </b-form-group>
        <b-form-group label="Password:" label-for="input-3">
            <b-form-input type="password" v-model="password" id="input-3" />
        </b-form-group>
        <b-form-group label="Repeat password:" label-for="input-4">
            <b-form-input type="password" v-model="repeat_password" id="input-4" />
        </b-form-group>
        <b-form-group label="Address:" label-for="input-5">
            <b-form-input v-model="address" id="input-5" />
        </b-form-group>
        <p class="text-danger">{{ msg }}</p>
    </div>
</template>

<script>
import axios from "axios"
const MD5 = require("crypto-js/md5")

export default {
    name: "login",
    data() {
        return {
            login_name: "",
            password: "",
            repeat_password: "",
            name: "",
            address: "",
            msg: "",
            mode: "signup"
        }
    },

    methods: {
        handle_submit(evt) {
            this.msg = ""
            evt.preventDefault()
            if (this.mode == "signup") {
                if (this.password != this.repeat_password)
                    this.msg = "Passwords do not match."
                
                var postdata = {
                    login: this.login_name,
                    name: this.name,
                    password: MD5(this.password).toString(),
                    address: this.address
                }

                axios.post('/api/signup_customer', postdata)
                    .then(_ => {
                        window.location.reload()
                    })
                    .catch(error => {
                        this.msg = error.response.data.msg
                        console.log(error.response.data)
                    })

            } else if (this.mode == "login") {

            }
        }
    }
}
</script>