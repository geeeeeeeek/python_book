<template>
  <div class="content-list">
    <div class="list-title">我的评论</div>
    <div class="list-content">
      <div class="comment-view">
        <a-spin :spinning="loading" style="min-height: 200px;">
          <div class="comment-list">
            <div class="comment-item flex-view" v-for="item in commentData">
              <img src="@/assets/images/avatar.jpg" class="avatar">
              <div class="infos">
                <div class="name flex-view">
                  <h3></h3>
                  <h3 @click="handleClickTitle(item)">《{{item.title}}》</h3>
                </div>
                <div class="time">{{item.comment_time}}</div>
                <div class="content">{{item.content}}</div>
              </div>
            </div>
          </div>
        </a-spin>
      </div>
    </div>
  </div>
</template>

<script>
import {listMyCommentsApi} from '@/api/index/comment'

export default {
  name: 'CommentView',
  data () {
    return {
      loading: false,
      commentData: []
    }
  },
  mounted () {
    this.getCommentList()
  },
  methods: {
    handleClickTitle (record) {
      let text = this.$router.resolve({name: 'detail', query: {id: record.book}})
      window.open(text.href, '_blank')
    },
    getCommentList () {
      this.loading = true
      const userId = this.$store.state.user.userId
      listMyCommentsApi({userId: userId, order: 'recent'}).then(res => {
        this.commentData = res.data
        this.loading = false
      }).catch(err => {
        this.$message.error(err.msg || '网络异常')
        this.loading = false
      })
    }
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
  flex: 1;

  .list-title {
    color: #152844;
    font-weight: 600;
    font-size: 18px;
    //line-height: 24px;
    height: 48px;
    margin-bottom: 4px;
    border-bottom: 1px solid #cedce4;
  }
}

.comment-view {
  overflow: hidden;

  .comment-list {
    margin: 8px auto;
  }

  .comment-item {
    padding: 15px 0;

    .avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      margin-right: 8px;
    }

    .infos {
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
    }

    .name {
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      cursor: pointer;
    }

    h3 {
      color: #152844;
      font-weight: 600;
      font-size: 14px;
      margin: 0;
    }

    .traingle {
      width: 0;
      height: 0;
      border-left: 6px solid #c3c9d5;
      border-right: 0;
      border-top: 4px solid transparent;
      border-bottom: 4px solid transparent;
      margin: 0 12px;
    }

    .time {
      color: #5f77a6;
      font-size: 12px;
      line-height: 16px;
      height: 16px;
      margin: 2px 0 8px;
    }

    .content {
      color: #484848;
      font-size: 14px;
      line-height: 22px;
      padding-right: 30px;
    }
  }
}
</style>
