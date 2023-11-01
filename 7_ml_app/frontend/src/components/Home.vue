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
      <template v-for="item in task_list">
        <tr class="align-middle">
          <td>{{item.id}}</td>
          <td>{{item.image_name}}</td>
          <td>{{item.result}}</td>
          <td>
            <button @click="deleteTask(item.id)" class="btn btn-close"></button>
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
      task_list: []
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:5000')
      .then(response => {
        let getResponse = JSON.parse(response.data)
        this.task_list = getResponse["task_list"]
      })
      .catch(error => {
        console.log(error)
      })
  },
  methods: {
    deleteTask(id){
      axios
        .delete('http://127.0.0.1:5000/' + id)
        .then(response => {
          let deleteResponse = JSON.parse(response)
          console.log(deleteResponse)
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => {
          this.$router.go({path: '/', force: true})
        })
    },
  }
}
</script>
