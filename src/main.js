// entry point

import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
}).$mount('#app')
