<template>
  <div class="content-list">
    <div class="list-title">我的借阅</div>
    <a-tabs default-active-key="1" @change="onTabChange">
      <a-tab-pane key="1" tab="全部">
      </a-tab-pane>
      <a-tab-pane key="2" tab="在借">
      </a-tab-pane>
      <a-tab-pane key="3" tab="已还">
      </a-tab-pane>
    </a-tabs>
    <a-spin :spinning="loading" style="min-height: 200px;">
      <div class="list-content">
      <div class="order-item-view" v-for="(item, index) in borrowData" :key="index">
        <div class="header flex-view">
          <div class="left">
            <span class="text">借阅ID</span>
            <span class="num mg-4">#</span>
            <span class="num">{{item.id}}</span>
          </div>
          <div class="right">
            <a-popconfirm
              v-if="item.status==='1'"
              title="确定还书？"
              ok-text="是"
              cancel-text="否"
              @confirm="handleReturn(item)"
            >
              <a-button type="primary" size="small" style="margin-right: 24px;">还书</a-button>
            </a-popconfirm>
            <span class="text">状态</span>
            <span class="state">{{item.status==='1'? '在借':'已还'}}</span>
          </div>
        </div>
        <div class="content flex-view">
          <div class="left-list">
            <div class="list-item flex-view">
              <img :src="item.cover" class="book-img">
              <div class="detail flex-between flex-view">
                <div class="flex-between flex-top flex-view">
                  <h2 class="name">{{item.title}}</h2>
                  <span class="count">1本</span>
                </div>
                <div class="flex-between flex-center flex-view">
                  <span class="type">纸质书</span>
                  <span class="price"></span>
                </div>
              </div>
            </div>
          </div>
          <div class="right-info">
            <p class="title">借入时间</p>
            <p class="name">{{item.borrow_time}}</p>
            <p class="title">到期时间</p>
            <p class="text">{{item.expect_time}}
            </p>
            <p class="text"></p>
          </div>
        </div>
        <div class="bottom flex-view">
          <div class="left">
            <span class="text">共1本</span>
            <span class="open" @click="handleDetail(item.book)">图书详情</span>
          </div>
        </div>
      </div>
    </div>
    </a-spin>
  </div>
</template>

<script>
import {listApi} from '@/api/index/borrow'
import {returnBookApi} from '@/api/index/borrow'

export default {
  name: 'BorrowView',
  data () {
    return {
      loading: false,
      borrowData: [],
      borrowStatus: ''
    }
  },
  mounted () {
    this.getBorrowList()
  },
  methods: {
    onTabChange (key) {
      console.log(key)
      if (key === '1') {
        this.borrowStatus = ''
      }
      if (key === '2') {
        this.borrowStatus = '1'
      }
      if (key === '3') {
        this.borrowStatus = '2'
      }
      this.getBorrowList()
    },
    getBorrowList () {
      this.loading = true
      let userId = this.$store.state.user.userId
      listApi({userId: userId, borrowStatus: this.borrowStatus}).then(res => {
        res.data.forEach((item, index) => {
          if (item.cover) {
            item.cover = this.$BASE_URL + item.cover
          }
        })
        this.borrowData = res.data
        this.loading = false
      }).catch(err => {
        console.log(err)
        this.loading = false
      })
    },
    handleReturn (item) {
      returnBookApi({id: item.id}, {book: item.book}).then(res => {
        this.getBorrowList()
        this.$message.success('还书成功')
      }).catch(err => {
        console.log(err)
      })
    },
    handleDetail (bookId) {
      // 跳转新页面
      let text = this.$router.resolve({name: 'detail', query: {id: bookId}})
      window.open(text.href, '_blank')
    },
  }
}
</script>
<style scoped lang="less">
.flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.content-list {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;

  .list-title {
    color: #152844;
    font-weight: 600;
    font-size: 18px;
    line-height: 24px;
    height: 24px;
    margin-bottom: 4px;
  }
}

.order-item-view {
  background: #f7f9fb;
  border-radius: 4px;
  padding: 16px;
  margin-top: 12px;

  .header {
    border-bottom: 1px solid #cedce4;
    padding-bottom: 12px;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    font-size: 14px;

    .text {
      color: #6f6f6f;
    }

    .mg-4 {
      margin-left: 4px;
    }

    .num {
      font-weight: 500;
      color: #152844;
    }

    .num {
      font-weight: 500;
      color: #152844;
    }

    .time {
      margin-left: 16px;
      color: #a1adc5;
    }

    .state {
      color: #ff7b31;
      font-weight: 600;
      margin-left: 10px;
    }
  }

  .content {
    padding: 12px 0;
    overflow: hidden;

    .left-list {
      overflow: hidden;
      height: 132px;
      -webkit-box-flex: 2;
      -ms-flex: 2;
      flex: 2;
      padding-right: 16px;

      .list-item {
        height: 60px;
        margin-bottom: 12px;
        overflow: hidden;
        cursor: pointer;
      }

      .book-img {
        width: 48px;
        height: 100%;
        margin-right: 12px;
      }

      .detail {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
        -ms-flex-direction: column;
        flex-direction: column;
      }

      .flex-between {
        -webkit-box-pack: justify;
        -ms-flex-pack: justify;
        justify-content: space-between;
      }

      .flex-between {
        -webkit-box-pack: justify;
        -ms-flex-pack: justify;
        justify-content: space-between;
      }

      .flex-top {
        -webkit-box-align: start;
        -ms-flex-align: start;
        align-items: flex-start;
      }

      .name {
        color: #152844;
        font-weight: 600;
        font-size: 14px;
        line-height: 18px;
      }

      .count {
        color: #484848;
        font-size: 12px;
      }

      .flex-between {
        -webkit-box-pack: justify;
        -ms-flex-pack: justify;
        justify-content: space-between;
      }

      .flex-center {
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
      }

      .type {
        color: #6f6f6f;
        font-size: 12px;
      }

      .price {
        color: #ff7b31;
        font-weight: 600;
        font-size: 14px;
      }
    }

    .right-info {
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      border-left: 1px solid #cedce4;
      padding-left: 12px;
      line-height: 22px;
      font-size: 14px;

      .title {
        color: #6f6f6f;
      }

      .name {
        color: #152844;
      }

      .text {
        color: #484848;
      }

      .mg {
        margin-bottom: 4px;
      }
    }
  }

  .bottom {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    border-top: 1px solid #cedce4;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    font-size: 14px;
    padding-top: 14px;

    .text {
      color: #6f6f6f;
    }

    .open {
      color: #4684e2;
      margin-left: 8px;
      cursor: pointer;
    }

    .right {
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
    }

    .text {
      color: #6f6f6f;
    }

    .num {
      color: #152844;
      margin: 0 40px 0 8px;
    }

    .money {
      font-weight: 600;
      font-size: 18px;
      color: #ff7b31;
      margin-left: 8px;
    }
  }

}

.order-item-view:first-child {
  margin-top: 16px;
}

</style>
