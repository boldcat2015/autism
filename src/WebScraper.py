
# coding: utf-8

# In[1]:

# Web scraper of Q&As on Haodf.com

# import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
import numpy as np

webheader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4)         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}

def getObj(pageurl): # from url to soup
    '''
    r = requests.get(url=pageurl, headers = webheader)
    if r.status_code == requests.codes.ok:
        bsObj = BeautifulSoup(r.content, "lxml")
        return bsObj
    else:
        print('\033[33m Warning:\033[0m Fail to open:', pageurl)
        return None
    '''
    try:
        req = urllib.request.Request(url=pageurl, headers=webheader)
        webPage = urllib.request.urlopen(req)
        bsObj = BeautifulSoup(webPage, "lxml")
        return bsObj
    except:
        print('\033[33m Warning:\033[0m Fail to open:', pageurl)
        return None


# In[2]:

def getText(bsObj, feature): # feature with blue index
    try:
        target = bsObj.find(lambda tag: tag.get_text() == feature + '：')
        text = filter(lambda x:x.name != 'div' and x.name != 'script',                       target.next_siblings) # avoid bingli attachment
        text = ''.join(list(map(str, text))).replace('<br/>', '')
        text = re.sub(r'<[^>]+>([^<>]*)</[^>]+>', r'\1', text)
        text = re.sub(r'\n|\r', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    except:
        # print('\033[33m Warning:\033[0m Fail to get', feature)
        return None
        
def getTag(pageurl): # official name of jibing
    bsObj = getObj(pageurl)
    try:
        pos = bsObj.find("div", {"class":" content"})
        tag = pos.find("h1").get_text()
        return tag
    except:
        print('\033[33m Warning:\033[0m Fail to get tag:', pageurl)
        return None

def getQA(pageurl): # build each row of the database 
    bsObj = getObj(pageurl)
    if not bsObj:
        return None
    trigger = bsObj.find(class_='cblues1')
    if not trigger: # bad format (see README.md)
        return None
    # nicely formatted Q&A
    try:
        question = trigger.parent.parent
        QA = dict()
        QA['url'] = pageurl
        QA['咨询标题'] = question.find("h3").get_text().replace('咨询标题：', '')
        jibing = question.find("h2")
        QA['疾病'] = re.sub(r'\n', '', jibing.get_text())
        tag = jibing.find("a")
        if tag:
            QA['标签网址'] = tag['href']
            QA['标签'] = getTag(tag['href'])

        features = ['病情描述','希望提供的帮助','所就诊医院科室','用药情况','治疗情况','既往病史']
        for f in features:
            text = getText(bsObj, f)
            if text:
                QA[f] = text

        block = question.parent.parent.parent # any better solution?
        QA['咨询时间'] = block.find("div", {"class":"yh_l_times"}).get_text().strip()
        for reply in block.next_siblings: # A follows Q
            try:
                answer = reply.find("div", {"class":"h_s_cons_docs"})
                answer = answer.find("h3").get_text()
            except:
                continue # not a reply by doctor, keep searching...
            else: # valid Q&A completes here
                QA['大夫回复'] = answer
                QA['回复时间'] = reply.find("div", {"class":"yh_l_times"}).get_text().strip()
                break # only the first reply is valid
        return QA
    except:
        print('\033[33m Warning:\033[0m Fail to get Q&A:', pageurl)
        return None

# testqa = 'http://www.haodf.com/wenda/dflifei_g_4459684754.htm'
# getQA(testqa)


# In[3]:

def getPosts(pageurl): # one page of Q&As
    bsObj = getObj(pageurl)
    QAs = list()
    posts = bsObj.find("div", {"class":"zixun_list"}).findAll("a", {"class":"td_link"})
    for post in posts:
        print('    Now scraping post', post['href'])
        QA = getQA(post['href'])
        if QA:
            QAs.append(QA)
    df = pd.DataFrame(QAs,         columns=['咨询标题','咨询时间','疾病','病情描述','希望提供的帮助','所就诊医院科室','用药情况',                  '治疗情况','既往病史','标签','标签网址','大夫回复','大夫','回复时间','url'])
    return df

# testposts = 'http://dflifei.haodf.com/zixun/list.htm'
# getPosts(testposts)


# In[4]:

def getDaifu(pageurl): # all Q&A of one doctor
    bsObj = getObj(pageurl)
    df = pd.DataFrame(         columns=['咨询标题','咨询时间','疾病','病情描述','希望提供的帮助','所就诊医院科室',                 '用药情况','治疗情况','既往病史','标签','标签网址','回复时间','大夫回复','url'])
    
    totalposts = int(bsObj.find("span", {"class":"f14 orange1"}).get_text())
    n = bsObj.find("a", {"class":"page_turn_a","rel":"true"}).get_text()
    n = int(re.sub(r'[^0-9]','',n))
    for i in range(1, n+1): # 1-n pages, each has 25 posts at most
        listurl = pageurl + '?type=&p=' + str(i)
        print('  Now scraping page', i)
        df = df.append(getPosts(listurl), ignore_index=True)
    print(totalposts, n, len(df))
    return df

# testdaifu = 'http://dflifei.haodf.com/zixun/list.htm'
# df = getDaifu(testdaifu)


# In[5]:

def getDocSite(pageurl): # doctor's personal website
    bsObj = getObj(pageurl)
    docs = list()
    for doc in bsObj.findAll("li", {"class":"hp_doc_box_serviceStar"}):
        site = doc.find("a", {"class":"personweb-sickness-btn"})
        name = doc.find("a", {"class":"blue_a3"})
        if site: # doctor has personal website
            docs.append({'医生姓名':name.get_text(), '个人网站':site['href']+'zixun/list.htm'})
    return docs

def getJibing(pageurl): # get all doctors good at this disease
    docurl = re.sub(r'.htm$', '/daifu_1_all_all_all_all.htm', pageurl)
    bsObj = getObj(docurl)
    docs = list()
    n = int(bsObj.find("font", {"class":"black pl5 pr5"}).get_text().strip())
    for i in range(1, n+1):
        docsurl = re.sub(r'.htm$', '/daifu_'+str(i)+'_all_all_all_all.htm', pageurl)
        docs = docs + getDocSite(docsurl)
    return docs

# testjibing = 'http://www.haodf.com/jibing/zibizheng.htm'
# getJibing(testjibing)

