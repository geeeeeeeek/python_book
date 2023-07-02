<template>
  <div class="search">
    <Header />
    <div class="search-content">
      <SearchContentView />
    </div>
    <Footer />
  </div>
</template>
<script>
import Header from '@/views/index/components/header'
import Footer from '@/views/index/components/footer'
import SearchContentView from '@/views/index/components/search-content-view'

export default {
  components: {
    Footer,
    Header,
    SearchContentView
  },
  data () {
    return {
    }
  }

}
</script>
<style scoped lang="less">

.search-content {
  width: 1100px;
  margin: 4px auto;
}
</style>
