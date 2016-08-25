## Purpose
Train a model to help diagnosing autism based on behavior description, by learning Q&As of Professor Li (李斐), using data on [this](http://dflifei.haodf.com/) website.

## Process
- [Data scraping](#data-scraping)
- [Data structure](#data-structure)
- [Natural language processing](#natural-language-processing)
- [Machine learning](#machine-learning)

#### Data scraping
Locate Q&As by the upper-right icon "患" or "医".

Pages on the website contain:

1. questions raised on-line first, in text, information classified with **blue indices**. [(Example)](http://www.haodf.com/wenda/dflifei_g_4649622403.htm)

2. summary of the consult on phone call, in text. [(Example)](http://www.haodf.com/wenda/dflifei_g_4539164407.htm)

3. follow-up questions after being diagnosed in hospitals.  [(Example)](http://www.haodf.com/wenda/dflifei_g_4619605283.htm)

4. notices of meeting time, etc. [(Example)](http://www.haodf.com/wenda/dflifei_g_4663141326.htm)

5. irrelevant information, gift, etc.

We train our model mainly on data of the first class.

_By yyyy.mm.dd, we have obtained xxx valid data._
#### Data structure
Data are stored in this way:

#### Natural language processing

#### Machine learning