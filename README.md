## Purpose
Train a model to help diagnosing **autism** based on description of behavior, by learning Q&As on [好大夫网](http://www.haodf.com/jibing/zibizheng.htm).

## Process
- [Data scraping](#data-scraping)
- [Data structure](#data-structure)
- [Natural language processing](#natural-language-processing)
- [Machine learning](#machine-learning)

### Data scraping
Pages on the website contain:

1. questions raised on-line first, classified with **blue indices**, followed by doctor's short reply. [(Example)](http://www.haodf.com/wenda/dflifei_g_4649622403.htm)

2. summary of the consultation on phone call, usually with no text reply. [(Example)](http://www.haodf.com/wenda/dflifei_g_4539164407.htm)

3. follow-up questions after being diagnosed in hospitals.  [(Example)](http://www.haodf.com/wenda/dflifei_g_4619605283.htm)

4. notices of meeting time, notices of time changing, gift tickets and other irrelevant information.

We train our model mainly on data of the first class.

_By 2016.08.26, we have obtained 1657 valid data out of 2400 posts._
### Data structure
Data are stored as pandas.DataFrame object:

    columns=[  
    '咨询标题','咨询时间','疾病','病情描述','希望提供的帮助',  
    '所就诊医院科室','用药情况','治疗情况','既往病史','标签',  
    '标签网址','大夫回复','大夫','回复时间','url'])

saved in csv file, encoding in utf-8.

### Natural language processing

Tool: [Jieba](https://github.com/fxsjy/jieba)(结巴分词) -- Python Chinese word segmentation module


### Machine learning