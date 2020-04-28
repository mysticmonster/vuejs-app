<template>
  <div id="patient-table">
    <table>
      <!-- ...thead... -->
      <tbody>
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
  export default {
    name: 'patient-table',
    props: {
      patients: Array,
    },
  }
</script>

<style scoped></style>