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

只需要在globals.py定义flask扩展的全局变量
把base文件夹复制一份，然后在config.py插入"App.xxx"
然后改一下复制的代码flask改怎么用就怎么用


除了以下两句代码，请不要胡乱导入flask_dj文件夹中的其他文件
如果需要访问config的变量，正确的做法是app对象中的config
```python
from flask_dj import app
from flask_dj.globals import *
```


