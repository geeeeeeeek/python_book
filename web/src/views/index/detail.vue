<template>
  <div class="detail">
    <Header/>
  </div>
</template>
<script>
import Header from '@/views/index/components/header'
import Footer from '@/views/index/components/footer'
import {
  detailApi,
  addWishUserApi,
  listApi as listBookList,
  addCollectUserApi
} from '@/api/index/book'
import {listApi as listCommentListApi, createApi as createCommentApi, likeApi} from '@/api/index/comment'
import {createApi} from '@/api/index/borrow'

export default {
  components: {
    Footer,
    Header
  },
  data () {
    return {
      bookId: '',
      detailData: undefined,
      tabUnderLeft: 6,
      tabData: ['简介', '评论'],
      selectTabIndex: 0,
      commentData: [],
      recommendData: [],
      sortIndex: 0,
      order: 'recent', // 默认排序最新
    }
  },
  mounted () {
    this.bookId = this.$route.query.id.trim()
    this.getBookDetail()
    this.getRecommendBook()
    this.getCommentList()
  },
  methods: {
    selectTab (index) {
      this.selectTabIndex = index
      console.log(this.selectTabIndex)
      this.tabUnderLeft = 6 + 58 * index
    },
    getBookDetail () {
      detailApi({id: this.bookId}).then(res => {
        this.detailData = res.data
        this.detailData.cover = this.$BASE_URL + this.detailData.cover
      }).catch(err => {
        this.$message.error('获取详情失败')
      })
    },
    addToWish () {
      let username = this.$store.state.user.username
      if (username) {
        addWishUserApi({bookId: this.bookId, username: username}).then(res => {
          this.detailData = res.data
          this.detailData.cover = this.$BASE_URL + this.detailData.cover
          this.$message.success('加入成功')
        }).catch(err => {
          console.log('操作失败')
        })
      } else {
        this.$message.warn('请先登录')
      }
    },
    collect () {
      let username = this.$store.state.user.username
      if (username) {
        addCollectUserApi({bookId: this.bookId, username: username}).then(res => {
          this.$message.success('收藏成功')
          this.detailData = res.data
          this.detailData.cover = this.$BASE_URL + this.detailData.cover
        }).catch(err => {
          console.log('收藏失败')
        })
      } else {
        this.$message.warn('请先登录')
      }
    },
    share () {
      let content = '分享一个非常好玩的网站 ' + window.location.href
      let shareHref = 'http://service.weibo.com/share/share.php?title=' + content
      window.open(shareHref)
    },
    handleBorrow (detailData) {
      console.log(detailData)
      const userId = this.$store.state.user.userId
      if (userId) {
        createApi({
          book: detailData.id,
          user: userId
        }).then(res => {
          this.$message.success('借阅成功')
          this.getBookDetail()
        }).catch(err => {
          this.$message.error(err.msg || '失败')
        })
      } else {
        this.$message.warn('请先登录')
      }
    },
    getRecommendBook () {
      listBookList({sort: 'recommend'}).then(res => {
        res.data.forEach((item, index) => {
          if (item.cover) {
            item.cover = this.$BASE_URL + item.cover
          }
        })
        console.log(res)
        this.recommendData = res.data.slice(0, 6)
      }).catch(err => {
        console.log(err)
      })
    },
    handleDetail (item) {
      // 跳转新页面
      let text = this.$router.resolve({name: 'detail', query: {id: item.id}})
      window.open(text.href, '_blank')
    },
    sendComment () {
      let text = this.$refs.comment.value.trim()
      console.log(text)
      if (text.length <= 0) {
        return
      }
      this.$refs.comment.value = ''
      let userId = this.$store.state.user.userId
      if (userId) {
        createCommentApi({content: text, book: this.bookId, user: userId}).then(res => {
          this.getCommentList()
        }).catch(err => {
          console.log(err)
        })
      } else {
        this.$message.warn('请先登录！')
        this.$router.push({name: 'login'})
      }
    },
    like (commentId) {
      likeApi({commentId: commentId}).then(res => {
        this.getCommentList()
      }).catch(err => {
        console.log(err)
      })
    },
    getCommentList () {
      listCommentListApi({bookId: this.bookId, order: this.order}).then(res => {
        this.commentData = res.data
      }).catch(err => {
        console.log(err)
      })
    },
    sortCommentList (sortType) {
      if (sortType === 'recent') {
        this.sortIndex = 0
      } else {
        this.sortIndex = 1
      }
      this.order = sortType
      this.getCommentList()
    }
  }
}
</script>
<style scoped lang="less">

.hide {
  display: none;
}

.detail-content {
  display: flex;
  flex-direction: column;
  width: 1100px;
  margin: 4px auto;
}

.flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.hidden-lg {
  display: none !important;
}

.book-infos-view {
  display: flex;
  margin: 89px 0 40px;
  overflow: hidden;

  .book-infos {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    display: flex;
  }

  .mobile-share-box {
    height: 38px;
    background: transparent;
    padding: 0 16px;
    margin: 12px 0;
    font-size: 0;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;

    .state {
      width: 64px;
      height: 24px;
      line-height: 24px;
      background: rgba(70, 132, 226, .1);
      border-radius: 2px;
      font-weight: 500;
      font-size: 12px;
      color: #4684e2;
      text-align: center;
    }

    .share-img {
      background: #fff;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      text-align: center;

      img {
        position: relative;
        top: 4px;
        width: 24px;
      }
    }
  }

  .book-img-box {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 235px;
    flex: 0 0 235px;
    margin: 0 40px 0 0;

    img {
      width: 235px;
      height: 339px;
      display: block;
      margin: 0 auto;
      border: 1px solid #eee;
      border-radius: 4px;
    }
  }

  .book-info-box {
    text-align: left;
    padding: 0;
    margin: 0;
  }

  .book-state {
    height: 26px;
    line-height: 26px;

    .state {
      font-weight: 500;
      color: #4684e2;
      background: rgba(70, 132, 226, .1);
      border-radius: 2px;
      padding: 5px 8px;
      margin-right: 16px;
    }

    span {
      font-size: 14px;
      color: #152844;
    }
  }

  .book-name {
    font-size: 24px;
    line-height: 32px;
    margin: 16px 0;
  }

  .translators, .authors {
    line-height: 18px;
    font-size: 14px;
    margin: 8px 0;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    -webkit-box-pack: start;
    -ms-flex-pack: start;
    justify-content: flex-start;

    .name {
      color: #315c9e;
      white-space: normal;
    }
  }

  .tags {
    position: absolute;
    bottom: 20px;
    margin-top: 16px;

    .category-box {
      color: #152844;
      font-size: 14px;

      .title {
        color: #787878;
      }
    }
  }

  .book-counts {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 235px;
    flex: 0 0 235px;
    margin-left: 20px;
  }

  .pointer {
    cursor: pointer;
  }

  .count-item {
    height: 64px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    cursor: pointer;
  }

  .count-img {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 32px;
    flex: 0 0 32px;
    margin-right: 24px;
    font-size: 0;

    img {
      width: 100%;
      display: block;
    }
  }

  .count-box {
    position: relative;
    border-bottom: 1px solid #cedce4;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    height: 100%;
  }

  .count-text-box {
    font-size: 0;

    .count-title {
      color: #152844;
      font-weight: 600;
      font-size: 16px;
      line-height: 18px;
      display: block;
      height: 18px;
    }
  }

  .count-num-box {
    font-weight: 600;
    font-size: 20px;
    line-height: 24px;
    color: #152844;
  }
}

.buy-way {
  overflow: hidden;

  .title {
    font-weight: 600;
    font-size: 18px;
    height: 26px;
    line-height: 26px;
    color: #152844;
    margin-bottom: 12px;
  }

  .buy-way-item {
    background: #fbfeff;
    border: 1px solid #cedce4;
    border-radius: 4px;
    -webkit-box-flex: 0;
    margin-right: 20px;
    -ms-flex: 0 0 255px;
    flex: 0 0 255px;
    padding: 10px;

    .name {
      font-weight: 500;
      font-size: 16px;
      line-height: 24px;
      color: #152844;
      height: 24px;
      margin-bottom: 12px;
    }

    .price {
      position: relative;
      line-height: 24px;
    }

    .price-text {
      color: #ff7b31;
      font-size: 18px;
      font-weight: 700;
    }

    .buy-btn {
      cursor: pointer;
      display: block;
      background: #4684e2;
      border-radius: 4px;
      text-align: center;
      color: #fff;
      font-size: 14px;
      height: 32px;
      line-height: 32px;
      width: 76px;
      outline: none;
      border: none;
      margin-top: 12px;
    }

    .buy-btn img {
      width: 12px;
      margin-right: 2px;
      vertical-align: middle;
    }

    .buy-btn span {
      vertical-align: middle;
    }
  }
}

.book-content-view {
  margin-top: 40px;
  padding-bottom: 50px;
}

.main-content {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;

  .text {
    color: #484848;
    font-size: 16px;
    line-height: 26px;
    padding-left: 12px;
    margin: 11px 0;
    white-space: pre-wrap;
  }
}

.main-tab {
  border-bottom: 1px solid #cedce4;
}

.order-view {
  position: relative;
  color: #6c6c6c;
  font-size: 14px;
  line-height: 40px;

  .title {
    margin-right: 8px;
  }

  .tab {
    margin-right: 20px;
    cursor: pointer;
    color: #5f77a6;
    font-size: 16px;
    cursor: pointer;
  }

  .tab-select {
    color: #152844;
    font-weight: 600;
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

.recommend {
  -webkit-box-flex: 0;
  -ms-flex: 0 0 235px;
  flex: 0 0 235px;
  margin-left: 20px;

  .title {
    font-weight: 600;
    font-size: 18px;
    line-height: 26px;
    color: #152844;
    margin-bottom: 12px;
  }

  .books {
    border-top: 1px solid #cedce4;

    .book-item {
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      min-width: 255px;
      max-width: 255px;
      margin: 16px 0;
      height: fit-content;
      border-radius: 4px;
      overflow: hidden;
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
  }
}

.flex-view {
  display: flex;
}

.book-comment {
  .title {
    font-weight: 600;
    font-size: 14px;
    line-height: 22px;
    height: 22px;
    color: #152844;
    margin: 24px 0 12px;
  }

  .publish {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;

    .mine-img {
      -webkit-box-flex: 0;
      -ms-flex: 0 0 40px;
      flex: 0 0 40px;
      margin-right: 12px;
      border-radius: 50%;
      width: 40px;
      height: 40px;
    }

    .content-input {
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      background: #f6f9fb;
      border-radius: 4px;
      height: 32px;
      line-height: 32px;
      color: #484848;
      padding: 5px 12px;
      white-space: nowrap;
      outline: none;
      border: 0px;
    }

    .send-btn {
      margin-left: 10px;
      background: #4684e2;
      border-radius: 4px;
      -webkit-box-flex: 0;
      -ms-flex: 0 0 80px;
      flex: 0 0 80px;
      color: #fff;
      font-size: 14px;
      text-align: center;
      height: 32px;
      line-height: 32px;
      outline: none;
      border: 0px;
      cursor: pointer;
    }
  }

  .tab-view {
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    font-size: 14px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    margin: 24px 0;

    .count-text {
      color: #484848;
      float: left;
    }

    .tab-box {
      color: #5f77a6;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;

      .tab-select {
        color: #152844;
      }

      span {
        cursor: pointer;
      }
    }

    .line {
      width: 1px;
      height: 12px;
      margin: 0 12px;
      background: #cedce4;
    }
  }
}

.comments-list {
  .comment-item {
    .flex-item {
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      padding-top: 16px;

      .avator {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 40px;
        flex: 0 0 40px;
        width: 40px;
        height: 40px;
        margin-right: 12px;
        border-radius: 50%;
        cursor: pointer;
      }

      .person {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
      }

      .name {
        color: #152844;
        font-weight: 600;
        font-size: 14px;
        line-height: 22px;
        height: 22px;
        cursor: pointer;
      }

      .time {
        color: #5f77a6;
        font-size: 12px;
        line-height: 16px;
        height: 16px;
        margin-top: 2px;
      }

      .float-right {
        color: #4684e2;
        font-size: 14px;
        float: right;

        span {
          margin-left: 19px;
          cursor: pointer;
        }

        .num {
          color: #152844;
          margin-left: 6px;
          cursor: auto;
        }
      }
    }
  }
}

.comment-content {
  margin-top: 8px;
  color: #484848;
  font-size: 14px;
  line-height: 22px;
  padding-bottom: 16px;
  border-bottom: 1px dashed #cedce4;
  margin-left: 52px;
  overflow: hidden;
  word-break: break-word;
}

.infinite-loading-container {
  clear: both;
  text-align: center;
}
</style>
