# flask-dj  [gpl-2.0]
# flask结构化导入蓝图

只需要在config.py 插入一行代码，就能轻松解决循环导入的问题

```python
# 插入蓝图
INSTALL_APP = {
    'App.Base': '', # 蓝图和url
}
```