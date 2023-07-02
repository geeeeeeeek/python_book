/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  registerApi: '/myapp/index/user/register',
  loginApi: '/myapp/index/user/login',
  infoApi: '/myapp/index/user/info',
  updateApi: '/myapp/index/user/update',
  updatePwdApi: '/myapp/index/user/updatePwd',
}

export const registerApi = function (data) {
  return axios({
    url: api.registerApi,
    method: 'post',
    data: data
  })
}

export const loginApi = function (data) {
  return axios({
    url: api.loginApi,
    method: 'post',
    data: data
  })
}

export const infoApi = function (params) {
  return axios({
    url: api.infoApi,
    method: 'get',
    params: params
  })
}

export const updateApi = function (params, data) {
  return axios({
    url: api.updateApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    params: params,
    data: data
  })
}

export const updatePwdApi = function (params, data) {
  return axios({
    url: api.updatePwdApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    params: params,
    data: data
  })
}
