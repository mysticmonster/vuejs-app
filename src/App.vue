<template>
  <div id="app" class="small-container">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>Patient Details</h1>

    <employee-form @add:employee="addEmployee" />
    <employee-table v-bind:employees="employees" />
  </div>
</template>

<script>
  import EmployeeTable from '@/components/EmployeeTable.vue'
  import EmployeeForm from '@/components/EmployeeForm.vue'
  // import ImageUpload from '@/components/ImageUpload.vue'
  

  export default {
    name: 'app',
    components: {
      EmployeeTable,
      EmployeeForm,
      // ImageUpload,
    },
    data() {
      return {
        employees: [
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
    addEmployee(employee) {
      const lastId =
        this.employees.length > 0
          ? this.employees[this.employees.length - 1].id
          : 0;
      const id = lastId + 1;
      const newEmployee = { ...employee, id };
      this.employees = [...this.employees, newEmployee]
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