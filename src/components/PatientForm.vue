<template>
  <div id="patient-form">
    <form @submit.prevent="handleSubmit">
      <div class="flex-row">
        <div class="flex-small two-thirds">
          <label>Patient Name</label>
          <input v-model="patient.name" type="text" />
        </div>
        <div class="flex-small one-third">
          <label for="choose">Select Gender</label>
          <select id="choose" v-model="patient.gender">
            <option disabled selected>Please select</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>
      </div>
      <div class="flex-row">
        <div class="flex-small two-thirds">
          <label>Phone No.</label>
          <input v-model="patient.phone" type="number" />
        </div>
        <div class="flex-small one-third">
          <label>Age</label>
          <input v-model="patient.age" type="number" />
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
    name: 'patient-form',
    data() {
      return {
        patient: {
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
            
            datax.append('file', this.selectedFile); 


          
            datax.append('name', this.patient.name);
            datax.append('gender', this.patient.gender);
            datax.append('age', this.patient.age);
            datax.append('phone', this.patient.phone);

            let {data} = await axios.post('http://127.0.0.1:5000/',datax)

            this.patient.prediction = data.prediction

            this.$emit('add:patient', this.patient)
        },
        
    }
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>