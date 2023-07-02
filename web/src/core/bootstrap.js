import store from '@/store'
import storage from 'store'
import {
  ADMIN_TOKEN, ADMIN_USERNAME, TOKEN, USERID, USERNAME
} from '@/store/constants'

export default function Initializer () {
  // storage.remove('Show-header')
  store.commit('SET_ADMIN_TOKEN', storage.get(ADMIN_TOKEN))
  store.commit('SET_ADMIN_USERNAME', storage.get(ADMIN_USERNAME))

  store.commit('SET_TOKEN', storage.get(TOKEN))
  store.commit('SET_USERNAME', storage.get(USERNAME))
  store.commit('SET_USERID', storage.get(USERID))

  // store.dispatch('setLang', storage.get(APP_LANGUAGE, 'zh-CN'))
}
