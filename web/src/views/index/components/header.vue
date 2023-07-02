<template>
  <div class="main-bar-view">
    <div class="logo">
      <img src="@/assets/images/front-logo.png" class="search-icon" @click="$router.push({name:'portal'})">
    </div>
    <div class="search-entry">
      <img src="@/assets/images/search-icon.svg" class="search-icon">
      <input placeholder="输入关键词" ref="keyword" @keyup.enter="search" />
    </div>
    <div class="right-view">
      <a href="/#/admin" target="__black" type="a-link" style="line-height: 32px;width:60px;">后台入口</a>
      <template v-if="$store.state.user.username">
        <a-dropdown>
          <a class="ant-dropdown-link" @click="e => e.preventDefault()">
            <img src="@/assets/images/avatar.jpg" class="self-img" >
          </a>
          <a-menu slot="overlay">
            <a-menu-item>
              <a @click="goUserCenter('borrowView')">借阅中心</a>
            </a-menu-item>
            <a-menu-item>
              <a @click="goUserCenter('userInfoEditView')">个人设置</a>
            </a-menu-item>
            <a-menu-item>
              <a @click="quit()">退出</a>
            </a-menu-item>
          </a-menu>
        </a-dropdown>
<!--        <div class="right-icon">-->
<!--          <img src="@/assets/cart-icon.svg">-->
<!--          <span>3</span>-->
<!--        </div>-->
      </template>
      <template v-else>
        <button class="login btn hidden-sm" @click="goLogin()">登录</button>
      </template>

      <div class="right-icon" @click="msgVisible=true">
        <img src="@/assets/images/message-icon.svg">
        <span class="msg-point" style=""></span>
      </div>
      <div>
        <a-drawer
          title="我的消息"
          placement="right"
          :closable="true"
          :maskClosable="true"
          :visible="msgVisible"
          @close="onClose"
        >
          <a-spin :spinning="loading" style="min-height: 200px;">
            <div class="list-content">
              <div class="notification-view">
                <div class="list">
                  <div class="notification-item flex-view" v-for="item in msgData">
                    <!---->
                    <div class="content-box">
                      <div class="header">
                        <span class="title-txt">{{item.title}}</span>
                        <br/>
                        <span class="time">{{ item.create_time }}</span>
                      </div>
                      <div class="head-text">
                      </div>
                      <div class="content">
                        <p>{{ item.content }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </a-spin>
        </a-drawer>
      </div>
    </div>
  </div>
</template>

<script>
import {listApi} from '@/api/index/notice'

export default {
  name: 'Header',
  data () {
    return {
      loading: false,
      msgVisible: false,
      msgData: []
    }
  },
  mounted () {
    this.getMessageList()
  },
  methods: {
    getMessageList () {
      this.loading = true
      listApi().then(res => {
        this.msgData = res.data
        this.loading = false
      }).catch(err => {
        console.log(err)
        this.loading = false
      })
    },
    search () {
      const keyword = this.$refs.keyword.value
      if (this.$route.name === 'search') {
        this.$router.push({name: 'search', query: {keyword: keyword}})
      } else {
        let text = this.$router.resolve({name: 'search', query: {keyword: keyword}})
        window.open(text.href, '_blank')
      }
    },
    goLogin () {
      this.$router.push({name: 'login'})
    },
    goUserCenter (menuName) {
      this.$router.push({name: menuName})
    },
    quit () {
      this.$store.dispatch('Logout').then(res => {
        this.$router.push({name: 'portal'})
      })
    },
    onClose () {
      this.msgVisible = false;
    }
  }
}
</script>

<style scoped lang="less">
.main-bar-view {
  position: fixed;
  top: 0;
  left: 0;
  height: 56px;
  width: 100%;
  background: #fff;
  border-bottom: 1px solid #cedce4;
  padding-left: 48px;
  z-index: 16;
  display: flex;
  flex-direction: row;
  //justify-content: center; /*水平居中*/
  align-items: center; /*垂直居中*/
}

.logo {
  margin-right: 24px;
  img {
    width: 32px;
    height: 32px;
    cursor: pointer;
  }
}

.search-entry {
  position: relative;
  width: 400px;
  min-width: 200px;
  height: 32px;
  background: #ecf3fc;
  padding: 0 12px;
  border-radius: 16px;
  font-size: 0;
  cursor: pointer;

  img {
    max-width: 100%;
    height: auto;
  }
  .search-icon {
    width: 18px;
    margin: 7px 8px 0 0;
  }
  input {
    position: absolute;
    top:4px;
    width: 85%;
    height: 24px;
    border: 0px;
    outline:none;
    color: #000;
    background: #ecf3fc;
    font-size: 14px;
  }
}

.right-view {
  padding-right: 36px;
  flex:1;
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: flex-end; /* 内容右对齐 */

  .username {
    height: 32px;
    line-height: 32px;
    text-align: center;
  }
  button {
    outline: none;
    border: none;
    cursor: pointer;
  }
  img {
    cursor: pointer;
  }
  .right-icon {
    position: relative;
    width: 24px;
    margin: 4px 0 0 4px;
    cursor: pointer;
    display: inline-block;
    font-size: 0;
    span {
      position: absolute;
      right: -15px;
      top: -3px;
      font-size: 12px;
      color: #fff;
      background: #4684e2;
      border-radius: 8px;
      padding: 0 4px;
      height: 16px;
      line-height: 16px;
      font-weight: 600;
      min-width: 20px;
      text-align: center;
    }
    .msg-point {
      position: absolute;
      right: -4px;
      top: 0;
      min-width: 8px;
      width: 8px;
      height: 8px;
      background: #4684e2;
      border-radius: 50%;
    }
  }

  .self-img {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    vertical-align: middle;
    cursor: pointer;
  }
  .btn {
    background: #4684e2;
    font-size: 14px;
    color: #fff;
    border-radius: 32px;
    text-align: center;
    width: 66px;
    height: 32px;
    line-height: 32px;
    vertical-align: middle;
    margin-left: 32px;
  }
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

.notification-item {
  padding-top: 16px;

  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    margin-right: 8px;
  }

  .content-box {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    border-bottom: 1px dashed #e9e9e9;
    padding: 4px 0 16px;
  }

  .header {
    margin-bottom: 12px;
  }

  .title-txt {
    color: #315c9e;
    font-weight: 500;
    font-size: 14px;
  }

  .time {
    color: #a1adc5;
    font-size: 14px;
  }

  .head-text {
    color: #152844;
    font-weight: 500;
    font-size: 14px;
    line-height: 22px;

    .name {
      margin-right: 8px;
    }
  }

  .content {
    margin-top: 4px;
    color: #484848;
    font-size: 14px;
    line-height: 22px;
  }

}

</style>
