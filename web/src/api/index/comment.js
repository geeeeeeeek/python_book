/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/index/comment/list',
  listMyCommentsApi: '/myapp/index/comment/listMyComments',
  createApi: '/myapp/index/comment/create',
  deleteApi: '/myapp/index/comment/delete',
  likeApi: '/myapp/index/comment/like',
}

/**
 * 列表
 */
export const listApi = function (params) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: params
  })
}

/**
 * 新建
 */
export const createApi = function (data) {
  return axios({
    url: api.createApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    data: data
  })
}

/**
 * 删除
 */
export const deleteApi = function (params) {
  return axios({
    url: api.deleteApi,
    method: 'post',
    params: params
  })
}

/**
 * like
 */
export const likeApi = function (params) {
  return axios({
    url: api.likeApi,
    method: 'post',
    params: params
  })
}

/**
 * listMyCommentsApi
 */
export const listMyCommentsApi = function (params) {
  return axios({
    url: api.listMyCommentsApi,
    method: 'get',
    params: params
  })
}
