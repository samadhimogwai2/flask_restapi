<template>
  <h1 class="mt-5">Create</h1>
  
  <form>
    <div class="row form-row align-items-end justify-content-center">
      <div class="col-auto">
        <label class="sr-only" for="inlineFormInput">ID</label>
        <input v-model="id" type="text" class="form-control mb-2" id="inlineFormInput" placeholder="ID">
      </div>
      <div class="col-auto">
        <label class="sr-only" for="inlineFormInputGroup">Username</label>
        <div class="input-group mb-2">
          <input v-model="username" type="text" class="form-control" id="inlineFormInputGroup" placeholder="Username">
        </div>
      </div>
      <div class="col-auto">
        <button @click="post" type="button" class="btn btn-primary mb-2">Create</button>
      </div>
    </div>
  </form>

  <template v-if="showFlag">
    <div :class="classObj" role="alert">
      {{ response }}
    </div>
  </template>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'Create',
  data() {
    return {
      id: "",
      username: "",
      showFlag: false,
      response: ""
    }
  },
  computed: {
    classObj(){
        return {
          alert: true,
          "alert-primary": this.response === "SUCCESS",
          "alert-danger": this.response != "SUCCESS",
        }
    }
  },
  methods: {
    post(){
      const postData = {
        "id": String(this.id),
        "username": String(this.username)
      }
      
      axios
        .post('http://127.0.0.1:5000', postData)
        .then(response => {
          let json_response = JSON.parse(response.data)
          this.response = json_response["status"]
        })
        .catch(function (error) {
          console.log(error);
          this.response = "FAIL"
        })

      this.showFlag = true
      this.id = ""
      this.username = ""
      }
  }
}
</script>
