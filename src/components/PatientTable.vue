<template>
  <div id="patient-table">
    <table>
      <!-- ...thead... -->
      <tbody>
        <th>
          <td>Name</td>
          <td>Gender</td>
          <td>Phone</td>
          <td>Age</td>
          <td>Prediction</td>
        </th>
        <tr v-for="patient in patients" :key="patient.id">
          <td>{{ patient.name }}</td>
          <td>{{ patient.gender }}</td>
          <td>{{ patient.phone }}</td>
          <td>{{ patient.age }}</td>
          <td>{{ patient.prediction }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    name: 'patient-table',
    props: {
      patients_new: Array,
    },
    data(){
      return {
        patients: () => {this.patients_new+[]}
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        let {data} = await axios.get('http://127.0.0.1:5000/patient_data')
        this.patients = data
      }
    }
  }
</script>

<style scoped></style>