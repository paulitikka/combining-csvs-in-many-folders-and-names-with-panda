# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:11:14 2020

@author: pauli
"""

#%%Combining matrices:
#%These columns are ok, but still missing:
#1) If no value available, then insert: nan
#2) Publication date (see below:)

#•	Journal name, OK
#•	Year of publication, available, but not feched/set with all
#•	Month of publication,available, but not feched/set with all
#•	Day of publication, available, but not feched/set with all
#•	Article title, OK
#•	Link for publication, available, but not feched/set with all
#•	Reviewer name, i.e. Reviewer
#•	Reviewer title, i.e. Status of Reviewer
#•	Reviewer institution, i.e. Institution, but the name reviewer institution is better
#•	Word count (of peer review) OK
#•	Link for peer review, available, but not feched/set with all
#%%
import pandas as pd #for importing files
# https://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.DataFrame.html
import numpy as np  #for calculations, array manipulations
import glob
#https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
path = r'C:\python\all_csvs\bmj' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
#%
resulta=[]
resulta=['Journal Name','Title of Article', \
               'Writers of Article', \
               'Date of Publication',\
               'Link to Publication', \
               'Reviewer Name', \
               'Review Word Count', \
               'Reviewing Date', \
               "Reviewer's Title", \
               "Reviewer's Institution", \
               'Link to All Reviews',
               'Link to PDF of Review']
frame = frame[resulta] 
#%
frame.rename(columns={'Link to PDF of Review':'Link to PDF of Reviewer'}, inplace=True)
path = r'C:\python\all_csvs\bmc' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame1 = pd.concat(li, axis=0, ignore_index=True)
resulta=[]
resulta=['Journal Name','Title of Article', \
               'Writers of Article', \
               'Date of Publication',\
               'Link to Publication', \
               'Reviewer Name', \
               'Review Word Count', \
               'Reviewing Date', \
               "Reviewer's Title", \
               "Reviewer's Institution", \
               'Link to All Reviews',
               'Link to PDF of Reviewer']
frame1 = frame1[resulta] 
path = r'C:\python\all_csvs\plos' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame2 = pd.concat(li, axis=0, ignore_index=True)
    #%LOS is tricky:
resulta=[]
resulta=['Journal Name','Title of Article', \
               'Writers of Article', \
               'Date of Publication',\
               'Link to Publication', \
               'Reviewer Name', \
               'Review Word Count', \
               'Reviewing Date', \
               "Reviewer's Title", \
               "Reviewer's Institution", \
               'Link to All Reviews',
               'Link to PDF of Reviewer']
frame2 = frame2[resulta] 
#% Some info regarding:   
#https://cmdlinetips.com/2018/03/how-to-change-column-names-and-row-indexes-in-pandas/
#https://kite.com/python/answers/how-to-reorder-columns-in-a-pandas-dataframe-in-python
#https://kite.com/python/answers/how-to-sum-rows-of-a-pandas-dataframe-in-python
#https://datascience.stackexchange.com/questions/41448/how-to-rename-columns-that-have-the-same-name
#%https://datascience.stackexchange.com/questions/41448/how-to-rename-columns-that-have-the-same-name
tot_res=[]
tot_res=pd.concat([frame,frame1,frame2], axis=0, ignore_index=True)
tot_res.to_csv('all_journals_tikka1520.csv', index=False, na_rep='NA')
#https://stackoverflow.com/questions/50890989/pandas-changing-the-format-of-nan-values-when-saving-to-csv

#%Curating word counts folder:
tot_res=[]
tot_res = pd.read_csv('all_journals_tikka1520.csv')
#%
tot_res=tot_res[tot_res['Review Word Count']!=0]
#%
tot_res=tot_res[tot_res['Review Word Count']<=5200]

tot_res=tot_res.replace(np.nan, 'NA', regex=True)
#%Replacing names
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
tot_res=tot_res.replace('Journal Reviewer', 'NA')
tot_res=tot_res.replace('Journal Reviewer Title', 'NA')
tot_res=tot_res.replace('xx', 'NA')
tot_res=tot_res.replace('Journal Institution', 'NA')
#https://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string
#%%
#%The absolute index as written comes with loc:
#nati=tot_res.loc[319,:]
#tot_res=tot_res[tot_res.index!=319]
tot_res.to_csv('all_journals_tikka1520_ok.csv', index=False, na_rep='NA')
#%%
tot_res2=tot_res[tot_res['Review Word Count']>=20]
#%%
tot_res.to_csv('all_journals_tikka1520_ok2.csv', index=False, na_rep='NA')
