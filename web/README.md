# 说明文档

> web前端代码，前端风格借鉴了豆瓣、图灵、亚马逊、ant等多种网站风格。


### 部署步骤

1. 安装node，本人用的是15.14.0

2. 安装依赖
```
npm install
```
3. 修改配置
修改constants.js文件，将BASE_URL改为你自己的后端接口地址

4. 打包
```
npm run build
```

打包后，修改index.html里面的title成你自己的网站名称，然后将dist文件夹放到nginx服务器配置目录中

5. 安装nginx，并修改nginx.conf
```
server {
    listen       8001;
    server_name  localhost;

    location / {
        root   E:\dist;
        index  index.html index.htm;
    }
}

```
5. 访问你的域名即可




## 参考链接

- https://blog.csdn.net/C_ZhangSir/article/details/100989902
- https://blog.csdn.net/weixin_45748897/article/details/103701003
- https://blog.csdn.net/itzhongzi/article/details/73330681
- https://www.jianshu.com/p/ef348d1c8f2b
- https://juejin.cn/post/7013325675129995272
- http://idea.94goo.com/key




