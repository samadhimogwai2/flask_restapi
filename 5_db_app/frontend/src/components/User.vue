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
        this.putResponse = JSON.parse(response.data).status

        this.showFlag = true
      })
      .catch(function (error) {
        console.log(error);
        this.putResponse = "FAIL"
      })

      this.showFlag = true
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
