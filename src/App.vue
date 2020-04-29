<template>
  <div id="app" class="small-container">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>Patient Details</h1>

    <navbar />
    <patient-form @add:patient="addPatient" />
    <patient-table v-bind:patients="patients" />

  </div>
</template>

<script>
  import PatientTable from '@/components/PatientTable.vue'
  import PatientForm from '@/components/PatientForm.vue'
  // import ImageUpload from '@/components/ImageUpload.vue'
  // import Navbar from '@/components/Navbar.vue'
  

  export default {
    name: 'app',
    components: {
      PatientTable,
      PatientForm,
    },
    data() {
      return {
        patients: [
          {
            id: 1,
            name: 'Patient Name',
            phone: 'Phone No.',
            age: 'Age',
            gender: 'Gender',
            prediction: 'Prediction'
          },
        ],
      }
    },
    methods: {
    addPatient(patient) {
      const lastId =
        this.patients.length > 0
          ? this.patients[this.patients.length - 1].id
          : 0;
      const id = lastId + 1;
      const newPatient = { ...patient, id };
      this.patients = [...this.patients, newPatient]
    }
  }
}
</script>

<style>
  button {
    background: #009435;
    border: 1px solid #009435;
  }

  .small-container {
    max-width: 680px;
  }

  #app img {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>