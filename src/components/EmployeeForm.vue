<template>
  <div id="employee-form">
    <form @submit.prevent="handleSubmit">
      <div class="flex-row">
        <div class="flex-small two-thirds">
          <label>Patient Name</label>
          <input v-model="employee.name" type="text" />
        </div>
        <div class="flex-small one-third">
          <label for="choose">Select Gender</label>
          <select id="choose" v-model="employee.gender">
            <option disabled selected>Please select</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>
      </div>
      <div class="flex-row">
        <div class="flex-small two-thirds">
          <label>Phone No.</label>
          <input v-model="employee.phone" type="number" />
        </div>
        <div class="flex-small one-third">
          <label>Age</label>
          <input v-model="employee.age" type="number" />
        </div>
      </div>
      <div class="flex-row">
        <div class="flex-small half">
          <label>Upload Chest-XRay</label>
          <input type="file" @change="onFileSelected"/>
        </div>
        <div class="flex-small half">
          <label>Get Result</label>
          <button>Predict</button>
        </div>
      </div>
      
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'employee-form',
    data() {
      return {
        employee: {
          name: '',
          gender: '',
          phone: '',
          age: '',
          prediction: '',
        },
      }
    },
    methods: {
      onFileSelected(e){
            this.selectedFile = e.target.files[0]
        },
        async handleSubmit() {
            let datax = new FormData();
            datax.append('name', 'my-picture');
            datax.append('file', this.selectedFile); 

            let {data} = await axios.post('http://127.0.0.1:5000/',datax)

            this.employee.prediction = data.prediction

            this.$emit('add:employee', this.employee)
        },
        
    }
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>