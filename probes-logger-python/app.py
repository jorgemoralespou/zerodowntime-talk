
from __future__ import print_function

import os
import socket

INSTANCE = os.environ.get('INSTANCE', socket.gethostname())

from flask import Flask

READYRET=('OK', 200)
LIVERET=('OK', 200)

application = Flask(__name__)

@application.route('/ws/ready')
def ready():
    return READYRET

@application.route('/ws/live')
def live():
    return LIVERET

@application.route('/ws/setready')
def setready():
    global READYRET
    READYRET=('NOK', 500)
    return 'OK'

@application.route('/ws/setlive')
def setlive():
    global LIVERET
    LIVERET=('NOK', 500)
    return 'OK'

@application.route('/ws/unsetready')
def unsetready():
    global READYRET
    READYRET=('NOK', 500)
    return 'OK'

@application.route('/ws/unsetlive')
def unsetlive():
    global LIVERET
    LIVERET=('NOK', 500)
    return 'OK'

@application.route('/')
def default():
    return 'Hello world!!!'+ INSTANCE

import signal
import sys
import threading
import time
import os

try:
    import Queue as queue
except ImportError:
    import queue

from wsgiref.simple_server import make_server

wakeup = queue.Queue()

def killer():
    delay = wakeup.get()
    print('sleep', delay)
    time.sleep(delay)
    print('killing')
    os.kill(os.getpid(), signal.SIGKILL)

def handler(signum, frame):
    global LIVERET, READYRET

    print('signal', signum)
    READYRET=('NOK', 500)
    LIVERET=('NOK', 500)
    wakeup.put(10.0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, handler)

    thread = threading.Thread(target=killer)
    thread.setDaemon(True)
    thread.start()

    httpd = make_server('', 8080, application)
    httpd.serve_forever()
