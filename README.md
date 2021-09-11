# esp8266server
a esp8266 http web server with micropython v1.16

一个简易的基于异步IO的micropython http server，支持简单的页面及文件下传，以及application/json模式的数据传输
文件下传支持gzip模式，只需要用gzip将文件压缩成.gz格式

典型调用：

import network
ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid='AP8266', password='abcd1234')

import webserver
from webserver import Json,File

app = webserver.App(__name__)

@app.route('/')
def index():
    return File('index.html.gz')

#智能小车控制
@app.route('/control', methods=['POST'])
def up():
    data = app.request.json(False)['data']
    print('control=' + data)
    if data == 'forward':
        pass
    if data == 'back':
        pass
    if data == 'left':
        pass
    if data == 'right':
        pass
    return Json({'status': 'ok'})

print('start server')
app.run()

