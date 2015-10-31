from __future__ import absolute_import, unicode_literals

import threading
import logging
import pykka

from mopidy import core
from .readnfctag import ReadTag

logger = logging.getLogger(__name__)
__logprefix__ = 'NFCread: '

class NFCread(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(NFCread, self).__init__()
        self.core = core
        self.devicepath = str(config['nfcread']['devicepath'])
        self.tagReader = None
        self.tagReaderThread = None

    def ndef_read_callback(self, data):
        self.core.playback.play()

    def on_start(self):
        self.tagReader = ReadTag(self.devicepath, self.ndef_read_callback)
        self.tagReaderThreaded = threading.Thread(target=self.tagReader.start)
        self.tagReaderThreaded.start()        
        logger.info(__logprefix__ + 'started')

    def on_stop(self):
        logger.warning(__logprefix__ + 'stopping extension')
        self.tagReader.stop()


