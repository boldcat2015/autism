
# coding: utf-8

# In[ ]:

# scrape and store all Q&A of one doctor

from WebScraper import *

# usage: python Scrape.py index foldername
index = sys.argv[1]
foldername = sys.argv[2]
path = '../data/'+foldername+'/'+str(index).zfill(3)
sys.stdout = open(path+'.log', 'a')
sys.stderr = open(path+'.log', 'a')
docs = pd.read_csv('../data/doctors.csv', encoding='GBK', index_col=0)
pageurl = docs.ix[int(index)]['个人网站']
name = docs.ix[int(index)]['医生姓名']
df = getDaifu(pageurl, name)
df.to_csv(path+'.csv', encoding='utf-8')

