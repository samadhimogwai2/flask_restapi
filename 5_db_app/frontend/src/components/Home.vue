<template>
  <h1 class="mt-5">User一覧</h1>

  <table class="table">
    <thead>
      <tr class="table-primary">
        <th class="col-5"> ID </th>
        <th class="col-5"> Username </th>
        <th class="col-1">  </th>
        <th class="col-1">  </th>
      </tr>
    </thead>
    <tbody>
      <template v-for="item in response">
        <tr class="align-middle">
          <td>{{item.id}}</td>
          <td>{{item.username}}</td>
          <td>
            <button @click="editUser(item.id)" class="btn btn-outline-primary">Edit</button>
          </td>
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
  props: {
    msg: String
  },
  data() {
    return {
      response: {}
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:5000')
      .then(response => {
        let json_response = JSON.parse(response.data).users
        this.response = json_response
      })
      .catch(function (error) {
        console.log(error);
      })
  },
  methods: {
    deleteUser(id){
      axios
      .delete('http://127.0.0.1:5000/user/' + id)
      .then(response => {
        let json_response = response
        this.response = json_response
      })
      .catch(function (error) {
        console.log(error);
      })

      this.$router.go({path: '/', force: true})
    },
    editUser(id){
      this.$router.push({name: 'user', params: {"id": id}})
    },
  }
}
</script>
