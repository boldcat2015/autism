## Purpose
Train a model to help diagnosing **autism** based on description of behavior, by learning Q&As on [好大夫网](http://www.haodf.com/jibing/zibizheng.htm).

We focus on Professor Li [(李斐)](http://dflifei.haodf.com/zixun/list.htm?type=&p=1) first.

## Process
- [Data scraping](#data-scraping)
- [Data structure](#data-structure)
- [Natural language processing](#natural-language-processing)
- [Machine learning](#machine-learning)

#### Data scraping
Pages on the website contain:

1. questions raised on-line first, classified with **blue indices**, followed by doctor's short reply. [(Example)](http://www.haodf.com/wenda/dflifei_g_4649622403.htm)

2. summary of the consultation on phone call, usually with no text reply. [(Example)](http://www.haodf.com/wenda/dflifei_g_4539164407.htm)

3. follow-up questions after being diagnosed in hospitals.  [(Example)](http://www.haodf.com/wenda/dflifei_g_4619605283.htm)

4. notices of meeting time, notices of time changing, gift tickets and other irrelevant information.

We train our model mainly on data of the first class.

_By yyyy.mm.dd, we have obtained xxx valid data out of XXX posts._
#### Data structure
Data are stored in this way:

#### Natural language processing

#### Machine learning