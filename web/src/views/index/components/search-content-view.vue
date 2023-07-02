<template>
  <div class="content-margin">
    <h1 class="search-name-box">{{keyword}}</h1>
    <div class="search-tab-nav clearfix">
      <div class="tab-text">
        <span>与</span>
        <span class="strong">{{keyword}}</span>
        <span>相关的内容</span>
      </div>
    </div>
    <div class="content-list">
      <div class="book-list">

        <a-spin :spinning="loading" style="min-height: 200px;">
        <div class="books flex-view">
            <div class="book-item item-column-4" v-for="item in pageData" @click="handleDetail(item)">
              <div class="img-view">
                <img :src="item.cover" lazy="loaded">
              </div>
              <div class="info-view">
                <h3 class="book-name">{{item.title}}</h3>
                <p class="authors" v-if="item.author">{{item.author}}（作者）</p>
                <p class="translators" v-if="item.translator">{{item.translator}}（译者）</p>
              </div>
            </div>
        </div>
        </a-spin>
        <div class="page-view" style="">
          <a-pagination v-model="page" size="small" @change="changePage" :hideOnSinglePage="true" :defaultPageSize="pageSize" :total="total"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {listApi as listBookList} from '@/api/index/book'

export default {
  name: 'SearchContentView',
  data () {
    return {
      loading: false,
      keyword: '',
      bookData: [],
      pageData: [],

      page: 1,
      total: 0,
      pageSize: 20,
    }
  },
  watch: {
    // 监听路由
    $route (to, from) {
      this.search()
    }
  },

  mounted () {
    this.search()
  },
  methods: {
    search () {
      this.keyword = this.$route.query.keyword.trim()
      this.getBookList({'keyword': this.keyword})
    },
    // 分页事件
    changePage (page) {
      this.page = page
      let start = (this.page - 1) * this.pageSize
      this.pageData = this.bookData.slice(start, start + this.pageSize)
      console.log('第' + this.page + '页')
    },
    handleDetail (item) {
      // 跳转新页面
      let text = this.$router.resolve({name: 'detail', query: {id: item.id}})
      window.open(text.href, '_blank')
    },
    getBookList (data) {
      this.loading = true
      listBookList(data).then(res => {
        res.data.forEach((item, index) => {
          if (item.cover) {
            item.cover = this.$BASE_URL + item.cover
          }
        })
        this.bookData = res.data
        this.total = this.bookData.length
        this.changePage(1)
        this.loading = false
      }).catch(err => {
        console.log(err)
        this.loading = false
      })
    }
  }
}
</script>
<style scoped lang="less">
.content-margin {
  margin: 156px 0 100px;
}

.page-view {
  width: 100%;
  text-align: center;
  margin-top: 48px;
}

.search-name-box {
  background: #f5f9fb;
  height: 100px;
  line-height: 100px;
  font-size: 20px;
  color: #152844;
  text-align: center;
  position: fixed;
  top: 56px;
  left: 0;
  z-index: 1;
  width: calc(100% - 8px);
}

.search-tab-nav {
  position: relative;
  padding: 24px 0 16px;
  text-align: center;

  .tab-text {
    float: left;
    color: #5f77a6;
    font-size: 14px;
  }

  .strong {
    color: #152844;
    font-weight: 600;
    margin: 0 4px;
  }
}

.books {
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
}

.flex-view {
  display: flex;
}

.book-item {
  position: relative;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  margin-right: 20px;
  min-width: 255px;
  max-width: 255px;
  height: fit-content;
  border-radius: 4px;
  overflow: hidden;
  margin-top: 16px;
  cursor: pointer;

  .img-view {
    background: #eaf1f5;
    font-size: 0;
    text-align: center;
    height: 156px;
    padding: 8px 0;

    img {
      max-width: 100%;
      height: 100%;
      display: block;
      margin: 0 auto;
      border-radius: 4px;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
    }
  }

  .info-view {
    background: #f6f9fb;
    text-align: center;
    height: 108px;
    overflow: hidden;
    padding: 0 16px;

    h3 {
      color: #1c355a;
      font-weight: 500;
      font-size: 16px;
      line-height: 20px;
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      margin: 12px 0 8px;
    }

    .authors, .translators {
      color: #6f6f6f;
      font-size: 12px;
      line-height: 14px;
      margin-top: 4px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
  }

}
</style>
