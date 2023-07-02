<template>
  <div class="content-list">
    <div class="list-title">我的积分</div>
    <div class="my-score-view">
      <div class="score-title">积分余额：{{score}}</div>
    </div>
  </div>
</template>

<script>
import {infoApi} from '@/api/index/user'

export default {
  name: 'ScoreView',
  data () {
    return {
      score: 0
    }
  },
  mounted () {
    this.getUserInfo()
  },
  methods: {
    // 积分逻辑：每次还书的时候积分加1
    getUserInfo () {
      this.loading = true
      let userId = this.$store.state.user.userId
      infoApi({id: userId}).then(res => {
        if (res.data) {
          this.score = res.data.score
        }
        this.loading = false
      }).catch(err => {
        console.log(err)
        this.loading = false
      })
    },
  }
}
</script>
<style scoped lang="less">
.flex-view {
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

.my-score-view {
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  margin-top: 16px;

  .score-title {
    color: #111111;
    font-size: 14px;
    font-weight: 700;
  }

}
</style>
