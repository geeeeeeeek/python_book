/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/index/book/list',
  detailApi: '/myapp/index/book/detail',
  addWishUserApi: '/myapp/index/book/addWishUser',
  removeWishUserApi: '/myapp/index/book/removeWishUser',
  getWishBookListApi: '/myapp/index/book/getWishBookList',
  addCollectUserApi: '/myapp/index/book/addCollectUser',
  removeCollectUserApi: '/myapp/index/book/removeCollectUser',
  getCollectBookListApi: '/myapp/index/book/getCollectBookList',
  // increaseRecommendCountApi: '/myapp/index/book/increaseRecommendCount',
}

/**
 * list
 */
export const listApi = function (data) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: data
  })
}
/**
 * detail
 */
export const detailApi = function (data) {
  return axios({
    url: api.detailApi,
    method: 'get',
    params: data
  })
}

export const addWishUserApi = function (data) {
  return axios({
    url: api.addWishUserApi,
    method: 'post',
    params: data
  })
}

export const removeWishUserApi = function (data) {
  return axios({
    url: api.removeWishUserApi,
    method: 'post',
    params: data
  })
}

export const getWishBookListApi = function (params) {
  return axios({
    url: api.getWishBookListApi,
    method: 'get',
    params: params
  })
}

export const addCollectUserApi = function (data) {
  return axios({
    url: api.addCollectUserApi,
    method: 'post',
    params: data
  })
}

export const removeCollectUserApi = function (data) {
  return axios({
    url: api.removeCollectUserApi,
    method: 'post',
    params: data
  })
}

export const getCollectBookListApi = function (params) {
  return axios({
    url: api.getCollectBookListApi,
    method: 'get',
    params: params
  })
}

// export const increaseRecommendCountApi = function (data) {
//   return axios({
//     url: api.increaseRecommendCountApi,
//     method: 'post',
//     params: data
//   })
// }
