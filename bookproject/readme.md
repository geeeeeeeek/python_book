### 后端部署步骤

> 部署过程中，如遇问题可咨询作者：lengqin1024（微信）

1. 安装mysql数据库，启动服务
2. 打开cmd命令行，进入mysql，并新建数据库
```
mysql -u root -p
CREATE DATABASE IF NOT EXISTS book DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
3. 恢复sql数据
```
use book
source xxxx.sql
```
4. 复制资源，将upload文件夹复制到bookproject目录下
5. 安装python 3.8
6. 安装依赖包
```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```
运行项目
```
python manage.py runserver 0.0.0.0:9001
```
7. 后期维护改动

将修改的py文件覆盖服务器的py文件即可，重启django

### 删除数据库

drop database if exists book;

### 创建数据库

CREATE DATABASE IF NOT EXISTS book DEFAULT CHARSET utf8 COLLATE utf8_general_ci;


### 迁移数据库表

```
python manage.py makemigrations;

python manage.py migrate;

python manage.py makemigrations myapp;

python manage.py migrate myapp;
```

### 跨域配置

django-cors-headers

### 多对多技术参考

https://www.cnblogs.com/SunshineKimi/p/14140900.html

### 二级分类设计
https://blog.csdn.net/weixin_47971206/article/details/124199978

### 常见问题

多对多的查询可通过related_name别名查询
join查询
ForeignKey的时候字段会自动加_id后缀
学习SerializerMethodField
跨域配置 django-cors-headers
数据库备份命令:
mysqldump -u root -p --databases 数据库名称 > xxx.sql
创建管理员命令：
insert into b_user(username,password,role,status) values('admin111',md5('admin111'),1,'0');

接口请求频次限制

借书逻辑：库存减1
还书逻辑：库存加1, 积分加1

### 登录接口

调login -> 生成token

### 注意

update接口的时候，如果model里面存在多对多字段，则需要设置explode






