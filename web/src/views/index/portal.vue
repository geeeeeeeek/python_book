<template>
  <div class="portal">
    <Header />
    <Content />
    <Footer />
  </div>
</template>
<script>
import Header from '@/views/index/components/header'
import Footer from '@/views/index/components/footer'
import Content from '@/views/index/components/content'

export default {
  components: {
    Footer,
    Header,
    Content
  },
  data () {
    return {
    }
  }
}
</script>
<style scoped lang="less">

</style>
