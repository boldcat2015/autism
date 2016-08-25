#!/usr/bin/python
# test web scraping a single page

import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

weburl = "http://www.haodf.com/wenda/dflifei_g_4649622403.htm"
webheader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
req = urllib.request.Request(url=weburl, headers=webheader)
webPage = urllib.request.urlopen(req)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
bsObj = BeautifulSoup(webPage, "lxml")
question = bsObj.findAll("div", {"class":"h_s_cons_info"})
answer = bsObj.findAll("div", {"class":"h_s_cons_docs"})
for q in question:
    print("Q:")
    print(q.get_text())
for a in answer:
    print("A:")
    print(a.get_text())
