import router from './router'
import store from './store'
import storage from 'store'
import { ADMIN_TOKEN, TOKEN } from '@/store/constants'

// 路由权限白名单
const allowList = ['admin-login', 'login', 'register', 'portal', 'search', 'detail', '403', '404']
// 前台登录地址
const loginRoutePath = '/index/login'
// 后台登录地址
const adminLoginRoutePath = '/admin-login'

router.beforeEach((to, from, next) => {
  console.log(to, from)
  /* has token */

  /** 后台路由 **/
  if (to.path.startsWith('/admin')) {
    if (storage.get(ADMIN_TOKEN)) {
      if (to.path === adminLoginRoutePath) {
        next({ path: '/' })
      } else {
        next()
      }
    } else {
      if (allowList.includes(to.name)) {
        // 在免登录名单，直接进入
        next()
      } else {
        next({ path: adminLoginRoutePath, query: { redirect: to.fullPath } })
      }
    }
  }

  /** 前台路由 **/
  if (to.path.startsWith('/index')) {
    if (storage.get(TOKEN)) {
      if (to.path === loginRoutePath) {
        next({ path: '/' })
      } else {
        next()
      }
    } else {
      if (allowList.includes(to.name)) {
        // 在免登录名单，直接进入
        next()
      } else {
        next({ path: loginRoutePath, query: { redirect: to.fullPath } })
      }
    }
  }
})
//
// router.afterEach(() => {
//   NProgress.done() // finish progress bar
// })
