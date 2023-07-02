<template>
  <div class="content">
    <div class="content-left">
      <div class="left-search-item">
        <h4>图书分类</h4>
        <a-tree :tree-data="cData" :selected-keys="selectedKeys" @select="onSelect" style="min-height: 220px;">
        </a-tree>
      </div>
      <!--      <div class="left-search-item"><h4>书籍状态</h4>-->
      <!--        <div class="check-item flex-view"><input type="checkbox" name="state"-->
      <!--                                                 id="state0" value=""><label-->
      <!--          for="state0">上架</label>-->
      <!--        </div>-->
      <!--        <div class="check-item flex-view"><input type="checkbox" name="state"-->
      <!--                                                 id="state1" value=""><label-->
      <!--          for="state1">下架</label>-->
      <!--        </div>-->
      <!--        <div class="check-item flex-view"><input type="checkbox" name="state"-->
      <!--                                                 id="state2" value=""><label-->
      <!--          for="state2">预售</label>-->
      <!--        </div>-->
      <!--      </div>-->
      <div class="left-search-item"><h4>热门标签</h4>
        <div class="tag-view tag-flex-view">
            <span class="tag" :class="{'tag-select': selectTagId===item.id}" v-for="item in tagData" :key="item.id"
                  @click="clickTag(item.id)">{{ item.title }}</span>
        </div>
      </div>
    </div>
    <div class="content-right">
      <div class="top-select-view flex-view">
        <div class="order-view">
          <span class="title"></span>
          <span class="tab"
                :class="selectTabIndex===index? 'tab-select':''"
                v-for="(item,index) in tabData"
                :key="index"
                @click="selectTab(index)">
            {{ item }}
          </span>
          <span :style="{left: tabUnderLeft + 'px'}" class="tab-underline"></span>
        </div>
      </div>
      <a-spin :spinning="loading" style="min-height: 200px;">
        <div class="pc-book-list flex-view">
          <div v-for="item in pageData" :key="item.id" @click="handleDetail(item)" class="book-item item-column-3"><!---->
            <div class="img-view">
              <img :src="item.cover"></div>
            <div class="info-view"><h3 class="book-name">{{ item.title }}</h3>
              <p class="authors">{{ item.author }}</p>
              <p class="translators" v-if="item.translator">{{ item.translator }}（译者）</p></div>
          </div>
          <div v-if="pageData.length <= 0 && !loading" class="no-data" style="">暂无数据</div>
        </div>
      </a-spin>
      <div class="page-view" style="">
        <a-pagination v-model="page" size="small" @change="changePage" :hideOnSinglePage="true"
                      :defaultPageSize="pageSize" :total="total"/>
      </div>

    </div>

  </div>
</template>

<script>
import {listApi as listClassificationList} from '@/api/index/classification'
import {listApi as listTagList} from '@/api/index/tag'
import {listApi as listBookList} from '@/api/index/book'

export default {
  name: 'Content',
  data () {
    return {
      selectX: 0,
      selectTagId: -1,
      cData: [],
      selectedKeys: [],
      tagData: [],
      loading: false,

      tabData: ['最新', '最热', '推荐'],
      selectTabIndex: 0,
      tabUnderLeft: 12,

      bookData: [],
      pageData: [],

      page: 1,
      total: 0,
      pageSize: 12,
    }
  },
  mounted () {
    this.initSider()
    this.getBookList({})
  },
  methods: {
    initSider () {
      listClassificationList().then(res => {
        this.cData = res.data
      })
      listTagList().then(res => {
        this.tagData = res.data
      })
    },
    getSelectedKey () {
      if (this.selectedKeys.length > 0) {
        return this.selectedKeys[0]
      } else {
        return -1
      }
    },
    onSelect (selectedKeys) {
      this.selectedKeys = selectedKeys
      console.log(this.selectedKeys[0])
      if (this.selectedKeys.length > 0) {
        this.getBookList({c: this.getSelectedKey()})
      }
      this.selectTagId = -1
    },
    clickTag (index) {
      this.selectedKeys = []
      this.selectTagId = index
      this.getBookList({tag: this.selectTagId})
    },
    search () {
      const keyword = this.$refs.keyword.value
      console.log(keyword)
      this.getBookList({'keyword': keyword})
    },
    // clearSearch () {
    //   this.$refs.keyword.value = ''
    //   this.search()
    // },
    // 最新|最热|推荐
    selectTab (index) {
      this.selectTabIndex = index
      this.tabUnderLeft = 12 + 53 * index
      console.log(this.selectTabIndex)
      let sort = (index === 0 ? 'recent' : index === 1 ? 'hot' : 'recommend')
      const data = {sort: sort}
      if (this.selectTagId !== -1) {
        data['tag'] = this.selectTagId
      } else {
        data['c'] = this.getSelectedKey()
      }
      this.getBookList(data)
    },
    handleDetail (item) {
      // 跳转新页面
      let text = this.$router.resolve({name: 'detail', query: {id: item.id}})
      window.open(text.href, '_blank')
    },
    // 分页事件
    changePage (page) {
      this.page = page
      let start = (this.page - 1) * this.pageSize
      this.pageData = this.bookData.slice(start, start + this.pageSize)
      console.log('第' + this.page + '页')
    },
    getBookList (data) {
      this.loading = true
      listBookList(data).then(res => {
        this.loading = false
        res.data.forEach((item, index) => {
          if (item.cover) {
            item.cover = this.$BASE_URL + item.cover
          }
        })
        console.log(res)
        this.bookData = res.data
        this.total = this.bookData.length
        this.changePage(1)
      }).catch(err => {
        console.log(err)
        this.loading = false
      })
    }
  }
}

</script>

<style scoped lang="less">
.content {
  display: flex;
  flex-direction: row;
  width: 1100px;
  margin: 80px auto;
}

.content-left {
  width: 220px;
  margin-right: 32px;
}

.left-search-item {
  overflow: hidden;
  border-bottom: 1px solid #cedce4;
  margin-top: 24px;
  padding-bottom: 24px;
}

h4 {
  color: #4d4d4d;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  height: 24px;
}

.category-item {
  cursor: pointer;
  color: #333;
  margin: 12px 0 0;
  padding-left: 16px;
}

ul {
  margin: 0;
  padding: 0;
}

ul {
  list-style-type: none;
}

li {
  margin: 4px 0 0;
  display: list-item;
  text-align: -webkit-match-parent;
}

.child {
  color: #333;
  padding-left: 16px;
}

.child:hover {
  color: #4684e2;
}

.select {
  color: #4684e2;
}

.flex-view {
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  //justify-content: space-between;
  display: flex;
}

.name {
  font-size: 14px;
}

.name:hover {
  color: #4684e2;
}

.count {
  font-size: 14px;
  color: #999;
}

.check-item {
  font-size: 0;
  height: 18px;
  line-height: 12px;
  margin: 12px 0 0;
  color: #333;
  cursor: pointer;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.check-item input {
  cursor: pointer;
}

.check-item label {
  font-size: 14px;
  margin-left: 12px;
  cursor: pointer;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
}

.tag-view {
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin-top: 4px;
}

.tag-flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.tag {
  background: #fff;
  border: 1px solid #a1adc6;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  border-radius: 16px;
  height: 20px;
  line-height: 18px;
  padding: 0 8px;
  margin: 8px 8px 0 0;
  cursor: pointer;
  font-size: 12px;
  color: #152833;
}

.tag:hover {
  background: #4684e3;
  color: #fff;
  border: 1px solid #4684e3;
}

.tag-select {
  background: #4684e3;
  color: #fff;
  border: 1px solid #4684e3;
}

.content-right {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  padding-top: 12px;

  .pc-search-view {
    margin: 0 0 24px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;

    .search-icon {
      width: 20px;
      height: 20px;
      -webkit-box-flex: 0;
      -ms-flex: 0 0 20px;
      flex: 0 0 20px;
      margin-right: 16px;
    }

    input {
      outline: none;
      border: 0px;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      border-bottom: 1px solid #cedce4;
      color: #152844;
      font-size: 14px;
      height: 22px;
      line-height: 22px;
      -ms-flex-item-align: end;
      align-self: flex-end;
      padding-bottom: 8px;
    }

    .clear-search-icon {
      position: relative;
      left: -20px;
      cursor: pointer;
    }

    button {
      outline: none;
      border: none;
      font-size: 14px;
      color: #fff;
      background: #288dda;
      border-radius: 32px;
      width: 88px;
      height: 32px;
      line-height: 32px;
      margin-left: 2px;
      cursor: pointer;
    }

    .float-count {
      color: #999;
      margin-left: 24px;
    }
  }

  .flex-view {
    display: flex;
  }

  .top-select-view {
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    height: 40px;
    line-height: 40px;

    .type-view {
      position: relative;
      font-weight: 400;
      font-size: 18px;
      color: #5f77a6;

      .type-tab {
        margin-right: 32px;
        cursor: pointer;
      }

      .type-tab-select {
        color: #152844;
        font-weight: 600;
        font-size: 20px;
      }

      .tab-underline {
        position: absolute;
        bottom: 0;
        //left: 22px;
        width: 16px;
        height: 4px;
        background: #4684e2;
        -webkit-transition: left .3s;
        transition: left .3s;
      }
    }

    .order-view {
      position: relative;
      color: #6c6c6c;
      font-size: 14px;

      .title {
        margin-right: 8px;
      }

      .tab {
        color: #999;
        margin-right: 20px;
        cursor: pointer;
      }

      .tab-select {
        color: #152844;
      }

      .tab-underline {
        position: absolute;
        bottom: 0;
        left: 84px;
        width: 16px;
        height: 4px;
        background: #4684e2;
        -webkit-transition: left .3s;
        transition: left .3s;
      }
    }

  }

  .pc-book-list {
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;

    .book-item {
      min-width: 255px;
      max-width: 255px;
      position: relative;
      flex: 1;
      margin-right: 20px;
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

        .authors {
          color: #6f6f6f;
          font-size: 12px;
          line-height: 14px;
          margin-top: 4px;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .translators {
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

    .no-data {
      height: 200px;
      line-height: 200px;
      text-align: center;
      width: 100%;
      font-size: 16px;
      color: #152844;
    }
  }

  .page-view {
    width: 100%;
    text-align: center;
    margin-top: 48px;
  }
}

</style>
