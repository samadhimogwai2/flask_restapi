<template>
  <h1 class="mt-5">User</h1>

  <form>
    <div class="row form-row align-items-end justify-content-center">
      <div class="col-auto">
        <label class="sr-only" for="inlineFormInput">ID</label>
        <input v-model="id" type="text" class="form-control mb-2" id="inlineFormInput" placeholder="ID">
      </div>
      <div class="col-auto">
        <button @click="get" type="button" class="btn btn-primary mb-2">Get</button>
      </div>
    </div>
  </form>
  {{ getResponse }}
</template>

<script>
import axios from 'axios'

export default {
  name: 'Get',
  data() {
    return {
      id: "",
      getResponse: ""
    }
  },
  methods: {
    get(){
      axios
        .get('http://127.0.0.1:5000/user/'+this.id)
        .then(response => {
          this.getResponse = JSON.parse(response.data)
        })
        .catch(error => {
          console.log(error);
          
        })
        .finally(() => {
          this.id = ""
        })
      }
  }
}
</script>
