<template>
  <div class="content-list">
    <!--    <div class="list-title">我的地址</div>-->
    <div class="list-title">
      <span>地址管理</span>
      <span class="add-new-btn" @click="handleAdd">新建地址</span>
    </div>
    <div class="list-content">
      <div class="address-item flex-view" v-for="item in addressData">
        <div class="infos">
          <div class="name-box">
            <span class="name">{{item.name}}</span>
            <span class="tel">{{item.mobile}}</span>
          </div>
          <p class="address-box">{{item.desc}}</p>
        </div>
        <div class="do-box">
          <div class="btns">
            <span class="edit" @click="handleEdit(item)">编辑</span>
            <a-popconfirm
              title="确定删除？"
              ok-text="是"
              cancel-text="否"
              @confirm="handleDelete(item)"
            >
              <span class="delete">删除</span>
            </a-popconfirm>
          </div>
          <div class="default-box" v-if="item.default">
            <img src="@/assets/images/address-right-icon.svg">
            <span>默认地址</span>
          </div>
        </div>
      </div>
      <div class="no-data" style="display: none;">暂无地址</div>
    </div>
  </div>
</template>

<script>
import EditAddress from '@/views/index/user/modal/edit-address'
import {listApi, deleteApi} from '@/api/index/address'

export default {
  name: 'AddressView',
  data () {
    return {
      addressData: []
    }
  },
  mounted () {
    this.listAddressData()
  },
  methods: {
    listAddressData () {
      let userId = this.$store.state.user.userId
      listApi({userId: userId}).then(res => {
        this.addressData = res.data
      }).catch(err => {
        console.log(err)
      })
    },
    handleDelete (item) {
      deleteApi({ids: item.id}).then(res => {
        this.listAddressData()
      }).catch(err => {
        console.log(err)
      })
    },
    handleAdd () {
      this.$dialog(
        EditAddress,
        {
          on: {
            ok: () => {
              this.page = 1
              this.listAddressData()
            }
          }
        },
        {
          title: '新增地址',
          width: '480px',
          centered: true,
          bodyStyle: {
            maxHeight: 'calc(100vh - 200px)',
            overflowY: 'auto'
          }
        }
      )
    },
    handleEdit (item) {
      this.$dialog(
        EditAddress,
        {
          address: Object.assign({}, item),
          modifyFlag: true,
          on: {
            ok: () => {
              this.page = 1
              this.listAddressData()
            }
          }
        },
        {
          title: '编辑地址',
          width: '480px',
          centered: true,
          bodyStyle: {
            maxHeight: 'calc(100vh - 200px)',
            overflowY: 'auto'
          }
        }
      )
    },
  }
}
</script>
<style scoped lang="less">
progress {
  vertical-align: baseline;
}

.flex-view {
  display: flex;
}

input, textarea {
  outline: none;
  border-style: none;
}

button {
  padding: 0;
}

.content-list {
  flex: 1;

  .list-title {
    color: #152844;
    font-weight: 600;
    font-size: 18px;
    //line-height: 24px;
    height: 48px;
    margin-bottom: 20px;
    border-bottom: 1px solid #cedce4;
  }
  .add-new-btn {
    color: #4684e2;
    font-size: 14px;
    float: right;
    font-weight: 400;
    cursor: pointer;
  }
}

.address-item {
  background: #f7f9fb;
  border-radius: 4px;
  margin-bottom: 12px;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  padding: 16px;

  .name-box {
    color: #152844;
    font-weight: 500;
    font-size: 14px;
    line-height: 22px;
    height: 22px;
  }

  .name {
    margin-right: 16px;
  }

  .address-box {
    color: #484848;
    font-size: 14px;
    line-height: 22px;
    height: 22px;
    margin-top: 4px;
  }

  .btns {
    font-size: 14px;
    cursor: pointer;
    height: 22px;
    line-height: 22px;
  }

  .edit {
    color: #4684e2;
    margin-right: 24px;
  }

  .delete {
    color: #f62a2a;
  }

  .default-box {
    margin-top: 4px;
    font-size: 0;

    img {
      position: relative;
      top: -1px;
      width: 16px;
      height: 16px;
      margin-right: 4px;
      vertical-align: middle;
    }

    span {
      color: #6f6f6f;
      font-size: 14px;
      vertical-align: middle;
    }
  }
}
</style>
