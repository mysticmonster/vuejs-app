<template>
  <div id="employee-table">
    <table>
      <!-- ...thead... -->
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td>{{ employee.name }}</td>
          <td>{{ employee.gender }}</td>
          <td>{{ employee.phone }}</td>
          <td>{{ employee.age }}</td>
          <td>{{ employee.prediction }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'employee-table',
    props: {
      employees: Array,
    },
  }
</script>

<style scoped></style>