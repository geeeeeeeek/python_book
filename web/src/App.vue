<template>
  <a-config-provider :locale="zh">
    <div id="app">
      <router-view/>
    </div>
  </a-config-provider>
</template>

<script>
import zh from 'ant-design-vue/lib/locale-provider/zh_CN' // 中文

export default {
  name: 'App',
  data () {
    return {
      zh
    }
  },
  mounted () {
    document.title = '图书系统演示'
  }
}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  height: 100vh;
  overflow: scroll;
}
</style>
