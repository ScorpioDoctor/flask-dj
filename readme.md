
# FlaskAlpha [0.1.3]
![Bitbucket Pipelines branch](https://img.shields.io/bitbucket/pipelines/atlassian/adf-builder-javascript/task/SECO-2168.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) 

> 反正吧，更像django那个格式了
> 使用vscode,且pip安装flask扩展后直接能运行

### 运行测试
```bash
    cd 你的目录
    manage
    flask
    flask run    
```

### 调试
> 用vscode调试app.py就行, 注意不是myproject目录的app.py

### python 3.6.5 安装依赖(用cmd或者终端执行)
```bash
    pip install flask==1.0.2 flask_login==0.4.1 flask_babelex==0.9.3 flask_admin==1.5.1 flask_sqlalchemy==2.3.2 flask_bootstrap==3.3.7.1 flask_migrate==2.1.1 flask_moment==0.6.0 flup-py3==1.0.3 flask-cli==0.4.0
```

### python所需依赖对应的版本(用pip安装)
```
pip              10.0.1

click            6.7
Flask            1.0.2
Flask-Admin      1.5.1
Flask-BabelEx    0.9.3
Flask-Bootstrap  3.3.7.1
Flask-Login      0.4.1
Flask-Migrate    2.1.1
Flask-Moment     0.6.0
Flask-SQLAlchemy 2.3.2
flup-py3         1.0.3
Flask-CLI        0.4.0
```

```

### 数据库初始化
> 同步表结构,保留数据(注意删除字段和删表除外)
```bash
    cd 你的工程
    manage      # 设置flask变量
    flask
    flask db init
```
 
### 数据库同步 (syncdb.bat)
> 同步表结构,保留数据(注意删除字段和删表除外)

```bash
    cd 你的工程
    manage      # 设置flask变量
    flask
    flask db migrate
    flask db upgrade
```

### 部署模式
> 记得config设置DEBUG=FALSE, 必须配置nginx.conf
> config的SERVER_NAME和nginx.conf的fcgi_pass的ip端口必须一致
```bash
    cd 你的工程
    manage      # 设置flask变量
    flask
    flask runfcgi 
```

### 超级傻瓜教程
```
    1.卸载你的电脑上所有python，且把目录删除干净
    2.安装python 3.6.5
    3.执行pip安装扩展，命令在上面
    4.打开你的调试器，设置app.py为启动文件
    5.没了，就这样
    6.看readme, 看注释，别JB乱写
```

### 怎么添加蓝图
```
    把blueprint那个test目录复制一遍就行
    如果blueprint_app_url的数组长度>1 就会注册蓝图
```
