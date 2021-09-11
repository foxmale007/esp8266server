import network
ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid='AP8266', password='abcd1234')

import webserver
from webserver import Json,File

app = webserver.App(__name__)

@app.route('/')
def index():
    return File('index.html.gz')

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
'''
@app.route('/up')
def up():
    return Json({'method': app.request.method,
                 'headers': app.request.headers,
                 'path': app.request.path,
                 'body': app.request.body,
                 'json': app.request.json()})
    return Json({'hello': 'world'})
'''

print('start server')
app.run()
