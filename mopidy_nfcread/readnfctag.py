from __future__ import absolute_import, unicode_literals

import logging
import os
import sys
import time
import inspect

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"nfc")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import nfc

logger = logging.getLogger(__name__)
__logprefix__ = 'NFCread: '

class ReadTag():
    def __init__(self, devicepath, onreadcallback):
        self.devicepath = devicepath        
        self.clf = None
        self.onreadcallback = onreadcallback
        self._running = True

    def start(self):
        while self.run_once() and self._running:
	    time.sleep(1)
            logger.info(__logprefix__ + 'Watiting for NFC Tag')

    def stop(self):
        self._running = False
        raise SystemExit        

    def __on_rdwr_connect(self, tag):
        if tag.ndef:
            record = tag.ndef.message[0]
            if record.type == "urn:nfc:wkt:T":
                ndef_text = nfc.ndef.TextRecord(record).text
                self.onreadcallback(ndef_text)
            else:
                logger.warning(__logprefix__ + 'NDEF data not of type "urn:nfc:wkt:T" (text)')
        else:
            logger.warning(__logprefix__ + 'No NDEF data found')
        return True

    def run_once(self):
	if not self._running:
	    return false	
        try:
            self.clf = nfc.ContactlessFrontend(self.devicepath)
            return self.clf.connect(rdwr={
                'on-connect': self.__on_rdwr_connect
            })
        finally:
            self.clf.close()
	    logger.info(__logprefix__ + 'Reader shut down')
