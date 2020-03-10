rq-data
==============

获取ricequant中数据, 其中期货数据默认为vnpy格式。

<br>
<br>


准备工作：
1. 公网IP的网络（若没有可以使用ngrok工具，详细使用方法自行google或参照本目录下的word教程）
2. 安装配置mongodb数据库（或根据自己需求，修改rpc的回调函数，存其它数据库，或者csv）

使用步骤：
1. 在拥有公网ip的电脑上运行rpc服务器端 `rqdata/mongo/mongo_server.py`,并配置其中的mongodb以及rpc服务器端口
2. 将`rqdata/rpc/client.py` 上传到 ricequant研究中的notebook中，放到文件夹rpc下，重命名为rpc.py
3. 在研究中新建notebook名为：test.ipynb, 并将`rqdata/scripts/`中`[future1m.py, stock1m.py, rq.py]`中的某个代码copy进去，修改其中的rpc客户端地址和端口，或者参照自行编写其它数据获取代码。（vnpy格式数据代码在future1m.py中）


##### 若手动下载直接运行第3步中代码，每日自动更新继续下述配置

准备工作：
1. 配置selenium环境（下载chromewebdriver，并将其路径添加到环境变量PATH中，自行翻墙下载或见群文件）


使用步骤：
1. 在`rqdata/scripts/passwd.py中配置ricequant的用户名密码
2. 将`driver.get("https://www.ricequant.com/research/user/user_xxxxx/notebooks/test.ipynb")`中的
url路径改为步骤3中test.ipynb的路径。
3. 运行`rqdata/scripts/rice_auto.py`

