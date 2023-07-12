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
      {{ postStatus }}
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
      postStatus: "",
      showFlag: false,
    }
  },
  computed: {
    classObj(){
        return {
          alert: true,
          "alert-primary": this.postStatus === "SUCCESS",
          "alert-danger": this.postStatus != "SUCCESS",
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
          let postResponse = JSON.parse(response.data)
          this.postStatus = postResponse["status"]
        })
        .catch(error => {
          console.log(error);
          this.postStatus = "FAIL"
        })
        .finally(() => {
          this.id = ""
          this.username = ""
          this.showFlag = true
        })
      }
  }
}
</script>
