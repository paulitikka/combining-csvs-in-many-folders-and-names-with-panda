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
path = r'C:\python\all_csvs2\bmj' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    #%
    li.append(df)
    #%
li[0]=li[0].iloc[:,2:]
li[1]=li[1].iloc[:,2:]    

frame = pd.concat(li, axis=0, ignore_index=True)
#%
resulta=[]
#'Attachments', 'Page Count'
frame['Attachments']='nan'
frame['Page Count']='nan'
resulta=['Journal Name','Title of Article', \
               'Writers of Article', \
               'Date of Publication',\
               'Link to Publication', \
               'Reviewer Name', \
               'Review Word Count', \
               'Reviewing Date', \
               "Reviewer's Title", \
               "Reviewer's Institution", \
               'Link to All Reviews',\
               'Link to PDF of Review','Attachments', 'Page Count']
frame = frame[resulta]
frame=frame.set_index([list(range(len(frame1),len(frame)+len(frame1)))])
#%%
frame['Reviewer\'s Title'] = frame['Reviewer\'s Title'].astype(str) 
frame["Reviewer's Institution"] = frame["Reviewer's Institution"].astype(str) 
#%% If there is still clear mistakes:
#frame=frame.iloc[frame.index!=213,:]
#%% This is important conversion, you may loose an hour if you do not do it!!
frame.rename(columns={'Link to PDF of Review':'Link to PDF of Reviewer'}, inplace=True)
#%%
path = r'C:\python\all_csvs2\bmc' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

#%
frame1 = pd.concat(li, axis=0, ignore_index=True)
resulta=[]
#frame1['Attachments']='nan'
#frame1['Page Count']='nan'
resulta=['Journal Name','Title of Article', \
               'Writers of Article', \
               'Date of Publication',\
               'Link to Publication', \
               'Reviewer Name', \
               'Review Word Count', \
               'Reviewing Date', \
               "Reviewer's Title", \
               "Reviewer's Institution", \
               'Link to All Reviews',\
               'Link to PDF of Reviewer','Attachments', 'Page Count']
frame1 = frame1[resulta] 
frame1=frame1.set_index([list(range(0,len(frame1)))])
#%%
#frame1['Reviewer\'s Title'] = frame1['Reviewer\'s Title'].astype(str) 
#frame1["Reviewer's Institution"] = frame1["Reviewer's Institution"].astype(str) 
#%%
path = r'C:\python\all_csvs2\plos' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
li[0]=li[0].iloc[:,1:]
#%
frame2 = pd.concat(li, axis=0, ignore_index=True)
    #%LOS is tricky:
resulta=[]
frame2['Attachments']='nan'
frame2['Page Count']='nan'
#%
resulta=['Journal Name','Title of Article', \
               'Writers of Article', \
               'Date of Publication',\
               'Link to Publication', \
               'Reviewer Name', \
               'Review Word Count', \
               'Reviewing Date', \
               "Reviewer's Title", \
               "Reviewer's Institution", \
               'Link to All Reviews',\
               'Link to PDF of Reviewer','Attachments', 'Page Count']
frame2 = frame2[resulta] 
frame2=frame2.set_index([list(range(len(frame)+len(frame1),len(frame)+len(frame1)+len(frame2)))])
#% Some info regarding:   
#https://cmdlinetips.com/2018/03/how-to-change-column-names-and-row-indexes-in-pandas/
#https://kite.com/python/answers/how-to-reorder-columns-in-a-pandas-dataframe-in-python
#https://kite.com/python/answers/how-to-sum-rows-of-a-pandas-dataframe-in-python
#https://datascience.stackexchange.com/questions/41448/how-to-rename-columns-that-have-the-same-name
#%%https://datascience.stackexchange.com/questions/41448/how-to-rename-columns-that-have-the-same-name
tot_res=[]
#frame1 = pd.DataFrame(frame1)
totaa=[frame1, frame, frame2]
#https://stackoverflow.com/questions/58698013/error-on-concatenate-2-data-frames-with-indexes-as-a-list-of-strings
tot_res = pd.concat(totaa, axis=0, ignore_index=True, sort=False)
#tot_res.to_csv('all_journals_tikka1520.csv', index=False, na_rep='NA')
#https://stackoverflow.com/questions/50890989/pandas-changing-the-format-of-nan-values-when-saving-to-csv

#%Curating word counts folder:
#tot_res=[]
#tot_res = pd.read_csv('all_journals_tikka1520.csv')
#%%
#tot_res=tot_res[tot_res['Review Word Count']!=0]
#%
#tot_res=tot_res[tot_res['Review Word Count']<=5200]

tot_res=tot_res.replace(np.nan, 'NA', regex=True)
#%Replacing names
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
tot_res=tot_res.replace('Journal Reviewer', 'NA')
tot_res=tot_res.replace('Journal Reviewer Title', 'NA')
tot_res=tot_res.replace('xx', 'NA')
tot_res=tot_res.replace('Journal Institution', 'NA')
#%%
tot_res['Review Word Count'] = tot_res['Review Word Count'].astype(int) 
#In some columns you need to change the type from int/else to string so that when you
#are saving it as excel file, the 'nan' values do not dissapear (in excel)
#https://stackoverflow.com/questions/22005911/convert-columns-to-string-in-pandas
#df['Reviewer\'s Title'] = df['Reviewer\'s Title'].astype(str) 
#https://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string
#%%
#%The absolute index as written comes with loc:
#nati=tot_res.loc[319,:]
tot_res=tot_res[tot_res.index!=4346]
tot_res.to_csv('all_journals_tikka12620_ok.csv', index=False, na_rep='NA')
#%%
#tot_res2=tot_res[tot_res['Review Word Count']>=20]
#%%
tot_res.to_csv('all_journals_tikka12620_ok.csv', index=False, na_rep='NA')
