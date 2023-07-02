import Vue from 'vue'
import {BASE_URL} from '@/store/constants'
switch (process.env.NODE_ENV) {
  case 'development':
    Vue.prototype.$BASE_URL = BASE_URL
    break
  case 'production':
    Vue.prototype.$BASE_URL = BASE_URL
    break
  default:
    Vue.prototype.$BASE_URL = BASE_URL
    break
}
