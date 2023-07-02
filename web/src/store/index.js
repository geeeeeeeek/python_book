import Vue from 'vue'
import Vuex from 'vuex'
// import {listApi} from '@/api/admin'

import user from './modules/user'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {}, // 存放数据
  getters: {}, // 计算属性
  mutations: {}, // 修改state中数据的一些方法
  actions: {}, // 异步方法
  modules: {
    user
  }
})
