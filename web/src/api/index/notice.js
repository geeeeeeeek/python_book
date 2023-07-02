/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/index/notice/list_api',
}

/**
 * 列表
 */
export const listApi = function (data) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: data
  })
}
