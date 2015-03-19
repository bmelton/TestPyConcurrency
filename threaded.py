import json
import logging
from time import time
import os
from links import urls, download

logger = logging.getLogger(__name__)

from queue import Queue
from threading import Thread

class DownloadWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue

   def run(self):
       while True:
            # Get the work from the queue and expand the tuple
            url, headers = self.queue.get()
            if not headers == "":
                download(url, headers)
            else:
                download(url)
            self.queue.task_done()

def main():
    ts = time()
    queue = Queue()
    for x in range(8):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

    for url in urls:
        logger.info('Queueing {}'.format(url["url"]))
        if "headers" in url:
            queue.put((url["url"], url["headers"]))
        else:
            queue.put((url["url"], ""))

    queue.join()
    print('Took {}'.format(time() - ts))

if __name__ == "__main__":
    main()
