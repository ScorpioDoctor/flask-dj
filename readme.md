# flask-dj  [gpl-2.0]
# flask结构化导入蓝图

只需要在config.py 插入一行代码，就能轻松解决循环导入的问题

```python
# 插入蓝图
INSTALL_APP = {
    'App.Base': '', # 蓝图和url
}
```

Moment只做初始化，未配置
计划加入邮件，权限, WTF
```python
from flask_moment import Moment         # 全球化统一时间
```