<template>
  <h1 class="mt-5">User一覧</h1>

  <table class="table">
    <thead>
      <tr class="table-primary">
        <th class="col-3"> ID </th>
        <th class="col-7"> Username </th>
        <th class="col-1">  </th>
        <th class="col-1">  </th>
      </tr>
    </thead>
    <tbody>
      <template v-for="item in users">
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
  data() {
    return {
      users: [],
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:5000')
      .then(response => {
        let getResponse = JSON.parse(response.data)
        this.users = getResponse["users"]
      })
      .catch(error => {
        console.log(error);
      })
  },
  methods: {
    deleteUser(id){
      axios
      .delete('http://127.0.0.1:5000/user/' + id)
      .then(response => {
        let deleteResponse = JSON.parse(response.data)
        console.log(deleteResponse)
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
