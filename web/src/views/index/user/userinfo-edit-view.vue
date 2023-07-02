<template>
  <div class="content-list">
    <div class="list-title">设置</div>
    <a-spin :spinning="loading" style="min-height: 200px;">
      <div class="list-content">
      <div class="edit-view" userid="602081">
        <div class="item flex-view">
          <div class="label">头像</div>
          <div class="right-box avatar-box flex-view">
            <img :src="avatarUrl" class="avatar">
            <div class="change-tips flex-view">
                <a-upload
                  name="file"
                  accept="image/*"
                  :multiple="false"
                  :before-upload="beforeUpload"
                >
                  <label>点击更换头像</label>
                </a-upload>
              <p class="tip">图片格式支持 GIF、PNG、JPEG，尺寸不小于 200 PX，小于 4 MB</p>
            </div>
          </div>
        </div>
        <div class="item flex-view">
          <div class="label">昵称</div>
          <div class="right-box">
            <input type="text" v-model="form.nickname" placeholder="请输入昵称" maxlength="20" class="input-dom">
            <p class="tip">支持中英文，长度不能超过 20 个字符</p>
          </div>
        </div>
        <div class="item flex-view">
          <div class="label">手机号</div>
          <div class="right-box">
            <input type="text" v-model="form.mobile" placeholder="请输入邮箱" maxlength="100" class="input-dom web-input">
          </div>
        </div>
        <div class="item flex-view">
          <div class="label">邮箱</div>
          <div class="right-box">
            <input type="text" v-model="form.email" placeholder="请输入邮箱" maxlength="100" class="input-dom web-input">
          </div>
        </div>
        <div class="item flex-view">
          <div class="label">个人简介</div>
          <div class="right-box">
          <textarea v-model="form.description" placeholder="请输入简介" maxlength="200" class="intro">
          </textarea>
            <p class="tip">限制200字以内</p>
          </div>
        </div>
        <button class="save mg" @click="submit()">保存</button>
      </div>
    </div>
    </a-spin>
  </div>
</template>

<script>
import {infoApi, updateApi} from '@/api/index/user'

export default {
  data () {
    return {
      loading: false,
      form: {
        avatarUrl: undefined,
        avatar: undefined,
        nickname: undefined,
        email: undefined,
        mobile: undefined,
        description: undefined,
      }
    }
  },
  mounted () {
    this.getUserInfo()
  },
  methods: {
    beforeUpload (file) {
      // 改文件名
      const fileName = new Date().getTime().toString() + '.' + file.type.substring(6)
      const copyFile = new File([file], fileName)
      console.log(copyFile)
      this.form.avatar = copyFile
      return false
    },
    getUserInfo () {
      this.loading = true
      let userId = this.$store.state.user.userId
      infoApi({id: userId}).then(res => {
        this.form = res.data
        if (this.form.avatar) {
          this.avatarUrl = this.$BASE_URL + this.form.avatar
          this.form.avatar = undefined
        }
        this.loading = false
      }).catch(err => {
        console.log(err)
        this.loading = false
      })
    },
    submit () {
      let userId = this.$store.state.user.userId

      const formData = new FormData()
      if (this.form.avatar) {
        formData.append('avatar', this.form.avatar)
      }
      if (this.form.nickname) {
        formData.append('nickname', this.form.nickname)
      }
      if (this.form.email) {
        formData.append('email', this.form.email)
      }
      if (this.form.mobile) {
        formData.append('mobile', this.form.mobile)
      }
      if (this.form.description) {
        formData.append('description', this.form.description)
      }
      updateApi({id: userId}, formData).then(res => {
        this.form = res.data
        if (this.form.avatar) {
          this.avatarUrl = this.$BASE_URL + this.form.avatar
          this.form.avatar = undefined
        }
        this.$message.success('保存成功')
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped lang="less">
input, textarea {
  border-style: none;
  outline: none;
  margin: 0;
  padding: 0;
}

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
    line-height: 48px;
    height: 48px;
    margin-bottom: 4px;
    border-bottom: 1px solid #cedce4;
  }

  .edit-view {
    .item {
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      margin: 24px 0;

      .label {
        width: 100px;
        color: #152844;
        font-weight: 600;
        font-size: 14px;
      }

      .right-box {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
      }

      .avatar {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        margin-right: 16px;
      }

      .change-tips {
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -ms-flex-wrap: wrap;
        flex-wrap: wrap;
      }

      label {
        color: #4684e2;
        font-size: 14px;
        line-height: 22px;
        height: 22px;
        cursor: pointer;
        width: 100px;
        display: block;
      }

      .tip {
        color: #6f6f6f;
        font-size: 14px;
        height: 22px;
        line-height: 22px;
        margin: 0;
        width: 100%;
      }

      .right-box {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
      }

      .input-dom {
        width: 400px;
      }

      .input-dom {
        background: #f8fafb;
        border-radius: 4px;
        height: 40px;
        line-height: 40px;
        font-size: 14px;
        color: #152844;
        padding: 0 12px;
      }

      .tip {
        font-size: 12px;
        line-height: 16px;
        color: #6f6f6f;
        height: 16px;
        margin-top: 4px;
      }

      .intro {
        resize: none;
        background: #f8fafb;
        width: 100%;
        padding: 8px 12px;
        height: 82px;
        line-height: 22px;
        font-size: 14px;
        color: #152844;
      }
    }

    .save {
      background: #4684e2;
      border-radius: 32px;
      width: 96px;
      height: 32px;
      line-height: 32px;
      font-size: 14px;
      color: #fff;
      border: none;
      outline: none;
      cursor: pointer;
    }

    .mg {
      margin-left: 100px;
    }
  }
}

</style>
