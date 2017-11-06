import os
import psutil

cmdline_name = ['node', 'websocket-relay.js', 'secret', '10001', '10002']

for proc in psutil.process_iter():
    if proc.cmdline() == cmdline_name:
        print('stop server [kill -15 %d]' % proc.pid)
        os.system('kill -15 %d' % proc.pid)