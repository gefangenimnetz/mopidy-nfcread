import time
import threading

from readnfctag import ReadTag


def readcallback(data):
    print 'data read: ' + data

reader = ReadTag('tty:AMA0:pn532', readcallback)
reader.start()

while True:
    print 'waiting'
    time.sleep(3)
