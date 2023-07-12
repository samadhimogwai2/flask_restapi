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
  <p>{{ getResponse }}</p>

  <template v-if="showFlag">
    <div :class="classObj" role="alert">
      {{ putStatus }}
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
      username: "",
      getResponse: "",
      putStatus: "",
      showFlag: false,
    }
  },
  computed: {
    classObj(){
        return {
          alert: true,
          "alert-primary": this.putStatus === "SUCCESS",
          "alert-danger": this.putStatus != "SUCCESS",
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
          let putResponse = JSON.parse(response.data)
          this.putStatus = putResponse["status"]
        })
        .catch(error => {
          console.log(error);
          this.putStatus = "FAIL"
        })
        .finally(() => {
          this.showFlag = true
        })
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:5000/user/'+this.id)
      .then(response => {
        this.getResponse = JSON.parse(response.data)
      })
  }
}
</script>
