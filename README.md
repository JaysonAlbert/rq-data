rq-data
==============

获取ricequant中数据, 其中期货数据默认为vnpy格式。

<br>
<br>


准备工作：
1. 公网IP的网络（若没有可以使用ngrok工具，详细使用方法自行google）
2. 配置selenium环境
3. 安装配置mongodb数据库（或根据自己需求，修改rpc的回调函数，存其它数据库，或者csv）

使用步骤：
1. 在拥有公网ip的电脑上运行rpc服务器端 `rqdata/mongo/mongo_server.py`,并配置其中的mongodb以及rpc服务器端口
2. 将`rqdata/rpc/client.py` 上传到 ricequant研究中的notebook中，放到文件夹rpc下，重命名为rpc.py
3. 在研究中新建notebook名为：test.ipynb, 并将`rqdata/scripts/`中`[future1m.py, stock1m.py, rq.py]`中的某个代码copy进去，修改其中的rpc客户端地址和端口，或者参照自行编写其它数据获取代码。（vnpy格式数据代码在future1m.py中）
4. 在`rqdata/scripts/passwd.py中配置ricequant的用户名密码
5. 将`driver.get("https://www.ricequant.com/research/user/user_xxxxx/notebooks/test.ipynb")`中的
url路径改为步骤3中test.ipynb的路径。
6. 运行`rqdata/scripts/rice_auto.py`

有任何问题，欢迎加QQ群434588628解惑。
