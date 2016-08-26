## Purpose
Train a model to help diagnosing **autism** based on description of behavior, by learning Q&As on [好大夫网](http://www.haodf.com/jibing/zibizheng.htm).

We start with Q&A posts of one certain doctor first.
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

  symptom | symptom_time | diagnosis | diagnosis_time | url
  :--- | :---: | :--- | :---: | :---
  小孩不愿意做作业…… | 2015-12-29 | 家长您好，建议您…… | 2015-12-30 | [http://www.haodf.com/...](http://www.haodf.com/wenda/dflifei_g_4039325820.htm)

saved in pickle file.

### Natural language processing

### Machine learning