import Vue from 'vue'
import Router from 'vue-router'

// 重复点击bug
const originalPush = Router.prototype.push

Router.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(Router)

const constantRouterMap = [
  // ************* 前台路由 **************
  {
    path: '/',
    redirect: '/index'
  },
  {
    path: '/index',
    name: 'index',
    redirect: '/index/portal',
    component: () => import('@/views/index'),
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('@/views/index/login')
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('@/views/index/register')
      },
      {
        path: 'portal',
        name: 'portal',
        component: () => import('@/views/index/portal')
      },
      {
        path: 'detail',
        name: 'detail',
        component: () => import('@/views/index/detail')
      },
      {
        path: 'search',
        name: 'search',
        component: () => import('@/views/index/search')
      },
      {
        path: 'user',
        name: 'user',
        redirect: 'user/addressView',
        component: () => import('@/views/index/user'),
        children: [
          {
            path: 'addressView',
            name: 'addressView',
            component: () => import('@/views/index/user/address-view')
          },
          {
            path: 'wishBookView',
            name: 'wishBookView',
            component: () => import('@/views/index/user/wish-book-view')
          },
          {
            path: 'collectBookView',
            name: 'collectBookView',
            component: () => import('@/views/index/user/collect-book-view')
          },
          {
            path: 'orderView',
            name: 'orderView',
            component: () => import('@/views/index/user/order-view')
          },
          {
            path: 'borrowView',
            name: 'borrowView',
            component: () => import('@/views/index/user/borrow-view')
          },
          {
            path: 'userInfoEditView',
            name: 'userInfoEditView',
            component: () => import('@/views/index/user/userinfo-edit-view')
          },
          {
            path: 'followView',
            name: 'followView',
            component: () => import('@/views/index/user/follow-view')
          },
          {
            path: 'fansView',
            name: 'fansView',
            component: () => import('@/views/index/user/fans-view')
          },
          {
            path: 'scoreView',
            name: 'scoreView',
            component: () => import('@/views/index/user/score-view')
          },
          {
            path: 'commentView',
            name: 'commentView',
            component: () => import('@/views/index/user/comment-view')
          },
          {
            path: 'securityView',
            name: 'securityView',
            component: () => import('@/views/index/user/security-view')
          },
          {
            path: 'pushView',
            name: 'pushView',
            component: () => import('@/views/index/user/push-view')
          },
          {
            path: 'messageView',
            name: 'messageView',
            component: () => import('@/views/index/user/message-view')
          },
        ]
      }
    ]
  },
  // ************* 后台路由 **************
  {
    path: '/admin',
    name: 'admin',
    redirect: '/admin/overview',
    component: () => import('@/views/admin/layout/adminLayout'),
    children: [
      {
        path: 'overview',
        name: 'overview',
        component: () => import('@/views/admin/overview')
      },
      {
        path: 'book',
        name: 'book',
        component: () => import('@/views/admin/book')
      },
      {
        path: 'classification',
        name: 'classification',
        component: () => import('@/views/admin/classification')
      },
      {
        path: 'tag',
        name: 'tag',
        component: () => import('@/views/admin/tag')
      },
      {
        path: 'loginLog',
        name: 'loginLog',
        component: () => import('@/views/admin/login-log')
      },
      {
        path: 'opLog',
        name: 'opLog',
        component: () => import('@/views/admin/op-log')
      },
      {
        path: 'errorLog',
        name: 'errorLog',
        component: () => import('@/views/admin/error-log')
      },
      {
        path: 'banner',
        name: 'banner',
        component: () => import('@/views/admin/banner')
      },
      {
        path: 'ad',
        name: 'ad',
        component: () => import('@/views/admin/ad')
      },
      {
        path: 'notice',
        name: 'notice',
        component: () => import('@/views/admin/notice')
      },
      {
        path: 'comment',
        name: 'comment',
        component: () => import('@/views/admin/comment')
      },
      {
        path: 'borrow',
        name: 'borrow',
        component: () => import('@/views/admin/borrow')
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('@/views/admin/user')
      },
      {
        path: 'sysInfo',
        name: 'sysInfo',
        component: () => import('@/views/admin/sys-info')
      }
    ]
  },
  {
    path: '/admin-login',
    name: 'admin-login',
    component: () => import('@/views/admin/admin-login')
  }
]

export default new Router({
  routes: constantRouterMap
})
