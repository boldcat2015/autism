## Purpose
Train a model to help diagnosing **autism** based on behavior description, by learning Q&As on [好大夫网](http://www.haodf.com/).

We focus on Professor Li [(李斐)](http://www.haodf.com/doctor/DE4r0BCkuHzdexpWxIb1qIYC2U8VE.htm) first.

## Process
- [Data scraping](#data-scraping)
- [Data structure](#data-structure)
- [Natural language processing](#natural-language-processing)
- [Machine learning](#machine-learning)

#### Data scraping
Pages on the website contain:

1. questions raised on-line first, in text, information classified with **blue indices**. [(Example)](http://www.haodf.com/wenda/dflifei_g_4649622403.htm)

2. summary of the consult on phone call, in text. [(Example)](http://www.haodf.com/wenda/dflifei_g_4539164407.htm)

3. follow-up questions after being diagnosed in hospitals.  [(Example)](http://www.haodf.com/wenda/dflifei_g_4619605283.htm)

4. notices of meeting time, etc. [(Example)](http://www.haodf.com/wenda/dflifei_g_4663141326.htm)

5. gift tickets and other irrelevant information.

We train our model mainly on data of the first class.

_By yyyy.mm.dd, we have obtained xxx valid data._
#### Data structure
Data are stored in this way:

#### Natural language processing

#### Machine learning