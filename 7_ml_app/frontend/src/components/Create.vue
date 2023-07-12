<template>
  <h1 class="mt-5">Image Recognition</h1>

  <template v-if="showFlag">
    <div :class="classObj" role="alert">
      {{ postStatus }}
    </div>
  </template>

  <form>
    <div class="row form-row align-items-end justify-content-center mt-3">
      <div class="col-auto">
        <input class="form-control" type="file" ref="preview" id="formFile" @change="upload">
      </div>
      <div class="col-auto">
        <button @click="post" type="button" class="btn btn-primary">POST</button>
      </div>
    </div>
  </form>

  <template v-if="previewURL">
    <img :src="previewURL" class="img-fluid mt-5" alt="">
  </template>

</template>

<script>
import axios from 'axios'

export default {
  name: 'Create',
  data() {
    return {
      postStatus: "",
      previewURL: "",
      image_b64: ",",
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
    upload(e){
      const file = e.target.files[0]
      this.previewURL = URL.createObjectURL(file)
      this.image_name = file.name

      if(file){
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => {
          this.image_b64 = reader.result.split(',')[1]
        }
      }
    },
    post(){
      const postData = {
        "image_name": String(this.image_name),
        "image_b64": String(this.image_b64)
      }
      axios
        .post('http://127.0.0.1:5000/image', postData)
        .then(response => {
          let postResponse = JSON.parse(response.data)
          this.postStatus = postResponse["status"]
        })
        .catch(error => {
          console.log(error)
          this.postStatus = "FAIL"
        })
        .finally(() => {
          this.showFlag = true
        })
    }
  }
}
</script>
