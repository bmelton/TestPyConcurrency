import json
import logging
from time import time
import os

urls = [
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "https://api.technopedia.com/api/v1/sw_release/", "headers" : {"Authorization" : "apikey tpui:e54b64ad813c66669467daa110bffb25ba27e829"} },
    { "url" : "http://bdna.com/", },
    { "url" : "http://ctls.bdna.com/", },
    { "url" : "http://vendordata.bdna.com/", },
    { "url" : "http://dmi.bdna.com/", }
]

def download(url, headers=None):
    from requests_futures.sessions import FuturesSession
    session = FuturesSession()
    if headers and not headers == "":
        data = session.get(url, headers=headers)
    else:
        data = session.get(url)
    print(data.result())

if __name__ == "__main__":
    pass
