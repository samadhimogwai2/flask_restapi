<template>
  <h1 class="mt-5">Task一覧</h1>

  <table class="table">
    <thead>
      <tr class="table-primary">
        <th class="col-5"> ID </th>
        <th class="col-2"> Image Name </th>
        <th class="col-2"> Result </th>
        <th class="col-1">  </th>
      </tr>
    </thead>
    <tbody>
      <template v-for="item in response">
        <tr class="align-middle">
          <td>{{item.id}}</td>
          <td>{{item.image_name}}</td>
          <td>{{item.result}}</td>
          <td>
            <button @click="deleteUser(item.id)" class="btn btn-close"></button>
          </td>
        </tr>
      </template>  
    </tbody>
  </table>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      response: {}
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:5000')
      .then(response => {
         let json_response = JSON.parse(response.data)
         this.response = json_response["task_list"]
      })
      .catch(error => {
        console.log(error);
      })
  },
  methods: {
    deleteUser(id){
      axios
        .delete('http://127.0.0.1:5000/' + id)
        .then(response => {
          this.response = JSON.parse(response)
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => {
          this.$router.go({path: '/', force: true})
        })
    },
    editUser(id){
      this.$router.push({name: 'user', params: {"id": id}})
    },
  }
}
</script>
