import asyncio  
import aiohttp
from links import urls
from time import time, sleep

def fetch_page(url, headers):  
    t1 = time()
    if not headers == "":
        response = yield from aiohttp.request('GET', url, headers=headers)
    else:
        response = yield from aiohttp.request('GET', url)

    if response.status == 200:
        t2 = time()-t1
        print("%s :: %s :: %s" % (response.status, t2, response.url))
    else:
        print("data fetch failed for: %s" % url)

def main():  
    coros = []
    for url in urls:
        if "headers" in url:
            coros.append(asyncio.Task(fetch_page(url["url"], url["headers"])))
        else:
            coros.append(asyncio.Task(fetch_page(url["url"], "")))
    yield from asyncio.gather(*coros)


if __name__ == '__main__':  
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
