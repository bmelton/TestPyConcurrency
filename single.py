import logging
from time import time
import os
from links import urls, download

logger = logging.getLogger(__name__)

def main():
    ts = time()
    for url in urls:
        if "headers" in url:
            download(url["url"], headers=url["headers"])
        else:
            download(url["url"])

    print('Took {}s'.format(time() - ts))

if __name__ == "__main__":
    main()
