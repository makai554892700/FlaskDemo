## 该项目为flask项目的demo
[flask官网](http://flask.pocoo.org/)
[flask的git项目地址](https://github.com/pallets/flask)
#### 安装相关工具
    pip3 install -r requirements.txt


#### 初始化

    # 安装必要插件
    pip3 install -r requirements.txt
    # 初始化迁移文件
    python3 manage.py bd init
    # 将模型映射添加到文件中
    python3 manage.py db migrate
    # 将映射文件真正映射到数据库中
    python3 manage.py db upgrade

#### 启动项目

    pip3 manager.py runserver



