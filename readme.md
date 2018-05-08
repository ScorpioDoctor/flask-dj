
# flask结构化导入蓝图

使用vscode安装依赖后直接能运行

### python 3.6.5 安装依赖
```bash
    pip install flask flask_login flask_babelex flask_admin flask_sqlalchemy flask_bootstrap flask_migrate flask_moment
```
### 依赖对应的版本
```
Babel            2.5.3
click            6.7
Flask            1.0.2
Flask-Admin      1.5.1
Flask-BabelEx    0.9.3
Flask-Bootstrap  3.3.7.1
Flask-Login      0.4.1
Flask-Migrate    2.1.1
Flask-Moment     0.6.0
Flask-SQLAlchemy 2.3.2
pip              10.0.1
SQLAlchemy       1.2.7
```
### 防止导入循环，请遵循规则
```python 
    # 顶级目录的app.py 一般不需要修改
    # flask_dj目录
    #   app.py      禁止导入models.py，可以导入蓝图
    #   models.py   只能在蓝图导入，所有蓝图的都必须写在这
    #   globals.py  只能定义flask扩展以及类初始化，不能写其他代码
    #   config.py   只能写静态变量
```