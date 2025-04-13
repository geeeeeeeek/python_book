> 一直想做一款管理系统，看了很多优秀的开源项目但是发现没有合适的。于是利用空闲休息时间开始自己写了一套管理系统。技术栈包括： python, django, vue.js, mysql。现将部分源码开源，如需完整源码，可以联系客服微信：lengqin1024


### 演示地址

前台地址： http://book.gitapp.cn

后台地址：http://book.gitapp.cn/#/admin

后台管理帐号：

用户名：admin123
密码：admin123

### 功能介绍

平台采用B/S结构，后端采用主流的Python语言进行开发，前端采用主流的Vue.js进行开发。

整个平台包括前台和后台两个部分。

- 前台功能包括：首页、图书详情页、用户中心模块。
- 后台功能包括：总览、借阅管理、图书管理、分类管理、标签管理、评论管理、用户管理、运营管理、日志管理、系统信息模块。


### 代码结构

- bookproject目录是后端代码
- web目录是前端代码

### 部署运行

#### 后端运行步骤

(1) 安装python 3.8

(2) 安装依赖。进入bookproject目录下，执行 pip install -r requirements.txt

(3) 安装mysql 5.7数据库，并创建数据库，命名为book，创建SQL如下：
```
CREATE DATABASE IF NOT EXISTS book DEFAULT CHARSET utf8 COLLATE utf8_general_ci
```
(4) 恢复SQL数据。在cmd命令行执行如下命令：

```
mysql> use book;
mysql> source xxx/xxx.sql
```

(5) 启动django服务。在bookproject目录下执行：
```
python manage.py runserver
```

#### 前端运行步骤

(1) 安装node 16.14或以上

(2) 进入web目录下，安装依赖，执行:
```
npm install 
```
(3) 运行项目
```
npm run serve
```


### 界面预览

首页

![首页](https://raw.githubusercontent.com/geeeeeeeek/book/master/bookproject/upload/img/a.png)

后台首页

![后台首页](https://raw.githubusercontent.com/geeeeeeeek/book/master/bookproject/upload/img/b.png)

后台借阅管理

![后台借阅管理](https://raw.githubusercontent.com/geeeeeeeek/book/master/bookproject/upload/img/c.png)


### 参考论文

[点击查看](doc/python_book.docx)


### 付费咨询

微信：lengqin1024

### 打赏作者

<img src="https://raw.githubusercontent.com/geeeeeeeek/python_book/master/bookproject/upload/img/weixin-pay.jpg" width=400/>



