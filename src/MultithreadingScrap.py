
# coding: utf-8

# In[6]:

# Multithreading scrapers

from WebScraper import *


# In[7]:

# docs = pd.DataFrame(getJibing(testjibing), columns=['医生姓名','个人网站'])
# docs = docs.to_csv('../data/doctors.csv', encoding='GBK')
docs = pd.read_csv('../data/doctors.csv', encoding='GBK', index_col=0)


# In[2]:

data = pd.DataFrame(         columns=['咨询标题','咨询时间','疾病','病情描述','希望提供的帮助','所就诊医院科室','用药情况',                  '治疗情况','既往病史','标签','标签网址','大夫回复','大夫','回复时间','url'])

for i in docs.index:
    print('Now scraping page', docs.ix[i]['医生姓名'])
    df = getDaifu(docs.ix[i]['个人网站'])
    df['大夫'] = docs.ix[i]['医生姓名']
    data = data.append(df, ignore_index=True)

data.to_csv('../data/data-'                 + datetime.datetime.today().strftime('%Y-%m-%d-%H.%M.%S')                 + '.csv', encoding='utf-8')

