import Modal from 'ant-design-vue/es/modal'

export default (Vue) => {
  function dialog (component, componentProps, modalProps) {
    const _vm = this
    modalProps = modalProps || {}
    if (!_vm || !_vm._isVue) {
      return
    }
    let dialogDiv = document.querySelector('body>div[type=dialog]')
    if (!dialogDiv) {
      dialogDiv = document.createElement('div')
      dialogDiv.setAttribute('type', 'dialog')
      document.body.appendChild(dialogDiv)
    }

    const handle = function (checkFunction, afterHandel) {
      if (checkFunction instanceof Function) {
        const res = checkFunction()
        if (res instanceof Promise) {
          res.then(c => {
            c && afterHandel(c)
          }).catch(() => {
            // afterHandel(false)
          })
        } else {
          // res && afterHandel()
          res || afterHandel(false)
        }
      } else {
        // checkFunction && afterHandel()
        checkFunction || afterHandel()
      }
    }

    const dialogInstance = new Vue({
      data () {
        return {
          visible: true,
          confirmLoading: false
        }
      },
      router: _vm.$router,
      store: _vm.$store,
      mounted () {
        this.$on('close', (v) => {
          this.handleClose()
        })
      },
      methods: {
        handleClose () {
          handle(this.$refs._component.onCancel, () => {
            this.visible = false
            this.$refs._component.$emit('close')
            this.$refs._component.$emit('cancel')
            dialogInstance.$destroy()
          })
        },
        handleOk () {
          // this.confirmLoading = true
          // setTimeout(() => {
          //   this.confirmLoading = false
          // }, 1000)
          handle(this.$refs._component.onOK || this.$refs._component.onOk, (res) => {
            // if (res) {
              this.visible = false
              this.$refs._component.$emit('close')
              this.$refs._component.$emit('ok', res)
              dialogInstance.$destroy()
            // } else {
            //   this.confirmLoading = false
            // }
          })
        }
      },
      render: function (h) {
        const that = this

        const modalModel = modalProps && modalProps.model
        if (modalModel) {
          delete modalProps.model
        }
        const ModalProps = Object.assign({}, modalModel && { model: modalModel } || {}, {
          attrs: Object.assign({
            class: 'handle-modal'
          }, {
            ...(modalProps.attrs || modalProps)
          }, {
            confirmLoading: this.confirmLoading,
            visible: this.visible
          }),
          on: Object.assign({}, {
            ...(modalProps.on || modalProps)
          }, {
            ok: () => {
              that.handleOk()
            },
            cancel: () => {
              that.handleClose()
            }
          })
        })

        const componentModel = componentProps && componentProps.model
        if (componentModel) {
          delete componentProps.model
        }
        const ComponentProps = Object.assign({}, componentModel && { model: componentModel } || {}, {
          ref: '_component',
          attrs: Object.assign({}, {
            ...((componentProps && componentProps.attrs) || componentProps)
          }),
          on: Object.assign({}, {
            ...((componentProps && componentProps.on) || componentProps)
          })
        })
        return h(Modal, ModalProps, [
          h(component, ComponentProps)
        ])
      }
    }).$mount(dialogDiv)
    return dialogInstance
  }

  Object.defineProperty(Vue.prototype, '$dialog', {
    get: () => {
      return function () {
        const Instance = dialog.apply(this, arguments)
        return Instance
      }
    }
  })
}
