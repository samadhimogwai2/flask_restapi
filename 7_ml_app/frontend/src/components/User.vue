<template>
  <h1 class="mt-5">User</h1>

  <form>
    <div class="row form-row align-items-end justify-content-center">
      <div class="col-auto">
        <label class="sr-only" for="inlineFormInput">ID</label>
        <input type="text" class="form-control mb-2" id="inlineFormInput" :placeholder="id" disabled>
      </div>
      <div class="col-auto">
        <label class="sr-only" for="inlineFormInputGroup">Username</label>
        <div class="input-group mb-2">
          <input v-model="username" type="text" class="form-control" id="inlineFormInputGroup" placeholder="Username">
        </div>
      </div>
      <div class="col-auto">
        <button @click="change" type="button" class="btn btn-primary mb-2">Change</button>
      </div>
    </div>
  </form>
  {{ getResponse }}

  <template v-if="showFlag">
    <div :class="classObj" role="alert">
      {{ putResponse }}
    </div>
  </template>
</template>

<script>
import axios from 'axios'

export default {
  name: 'User',
  props: {
    id: String
  },
  data() {
    return {
      getResponse: "",
      putResponse: "",
      username: "",
      showFlag: false,
      resultFlag: false,
    }
  },
  computed: {
    classObj(){
        return {
          alert: true,
          "alert-primary": this.putResponse === "SUCCESS",
          "alert-danger": this.putResponse != "SUCCESS",
        }
    }
  },
  methods: {
    change(){
      const putData = {
        "id": String(this.id),
        "username": String(this.username)
      }

      axios
      .put('http://127.0.0.1:5000/user/'+this.id, putData)
      .then(response => {
        const json_response = JSON.parse(response.data).status
        this.putResponse = json_response

        this.showFlag = true
      })
      .catch(function (error) {
        console.log(error);
        this.putResponse = "FAIL"
      })
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:5000/user/'+this.id)
      .then(response => {
        let json_response = JSON.parse(response.data)
        console.log(json_response)
        this.response = json_response
      })
  }
}
</script>
