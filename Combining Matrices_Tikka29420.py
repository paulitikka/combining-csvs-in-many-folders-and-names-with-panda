# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:11:14 2020, updated 17.7.20

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
#%%Start with frame1
import pandas as pd #for importing files
# https://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.DataFrame.html
import numpy as np  #for calculations, array manipulations
import glob
#%https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
path = r'C:\python\all_csvs2\bmj' # use your path
all_files = glob.glob(path + "/*.csv")
#%2016 ei toimi..

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    #%
    li.append(df)
    #%
#li[0]=li[0].iloc[:,2:]
#li[1]=li[1].iloc[:,2:]    

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
               "Reviewer's Institution",\
               'Link to All Reviews',\
               'Link to PDF of Review','Attachments', 'Page Count']
frame = frame[resulta]
frame=frame.set_index([list(range(len(frame1),len(frame)+len(frame1)))])
#%
#frame['Reviewer\'s Title'] = frame['Reviewer\'s Title'].astype(str) 
#frame["Reviewer's Institution"] = frame["Reviewer's Institution"].astype(str) 
#% If there is still clear mistakes:
#frame=frame.iloc[frame.index!=213,:]
#% This is important conversion, you may loose an hour if you do not do it!!
frame.rename(columns={'Link to PDF of Review':'Link to PDF of Reviewer'}, inplace=True)
#%%
import pandas as pd #for importing files
# https://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.DataFrame.html
import numpy as np  #for calculations, array manipulations
import glob
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
#%
path = r'C:\python\all_csvs2\plos' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    #%
li[0]["Attachments"]='no' #if something is not available, mark it with 'nan'
li[0]["Page Count"]='nan' #if something is not available..
li[0]['Link to PDF of Reviewer']='nan'
li[1]['Link to PDF of Reviewer']='nan'

#%
frame2 = pd.concat(li, axis=0, ignore_index=True)
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
               'Link to All Reviews',\
               'Link to PDF of Reviewer','Attachments', 'Page Count']
frame2 = frame2[resulta] 
#frame2.rename(columns={'Link to PDF of Review':'Link to PDF of Reviewer'}, inplace=True)
frame2=frame2.set_index([list(range(len(frame)+len(frame1),len(frame)+len(frame1)+len(frame2)))])
#frame2=frame2.iloc[frame2.index!=6489,:]
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
tot_res['Attachments']=tot_res['Attachments'].replace('nan', 'no', regex=True)
tot_res['Page Count']=tot_res['Page Count'].replace('nan', 'NA', regex=True)
#%
#tot_res['Reviewer Name']=tot_res['Reviewer Name'].replace('', 'NA', regex=True)
#%
#%
tot_res['Review Word Count']=tot_res['Review Word Count'].replace('NA', 0, regex=True)
tot_res['Review Word Count'] = tot_res['Review Word Count'].astype(int) 
#In some columns you need to change the type from int/else to string so that when you
#are saving it as excel file, the 'nan' values do not dissapear (in excel)
#https://stackoverflow.com/questions/22005911/convert-columns-to-string-in-pandas
#df['Reviewer\'s Title'] = df['Reviewer\'s Title'].astype(str) 
#https://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string
#%
#%The absolute index as written comes with loc:
#nati=tot_res.loc[319,:]
#tot_res=tot_res[tot_res.index!==6093]
#%%
tot_res=tot_res[tot_res['Review Word Count']!=0]
#%
tot_res=tot_res[tot_res['Review Word Count']!=1]
#%%
tot_res=tot_res[tot_res['Reviewer Name']!='Qin Nin']
#tot_res=tot_res[tot_res['Link to PDF of Reviewer']!='NA']
#tot_res['Review Word Count'] = tot_res['Review Word Count'].astype(int) 
#%%
import pandas as pd
f =  pd.read_csv('totaxs.txt', header=None)
#https://stackoverflow.com/questions/21546739/load-data-from-txt-with-pandas
#https://www.quora.com/How-do-I-open-a-URL-in-Google-Chrome-in-new-tab-using-Python
import webbrowser
for i in range(len(f)):
    url = f.iloc[i][0]
    webbrowser.open_new_tab(url)
#%%
tot_res=tot_res[tot_res.index!=4826]
#%%
#%%
#tot_res=tot_res.replace(np.nan, 'NA', regex=True)
tot_res.to_csv('all_journals_tikka16720_ok1.csv', index=True, na_rep='NA')
all_journals_tikka16720_ok1
#%%
tot_res = pd.read_csv('all_journals_tikka16720_ok1.csv', index_col=None, header=0)
#tot_res2=tot_res[tot_res['Review Word Count']>=20]
#%%
tot_res.to_csv('all_journals_tikka17720_ok2a.csv', index=False, na_rep='NA')
#%%
import random
test=[]
for i in range(0,8):
    test.append(int(len(tot_res)*random.random()))
    #%
test=np.sort(test)
testa=pd.DataFrame(test)
#%
#testa.to_csv('rnd_chk_tikka7720_ok.csv', index=False, na_rep='NA')
#%
#testa = pd.read_csv('rnd_chk_tikka18620_ok.csv', index_col=None, header=0)
#%
#1)428: 
natax=[]
for i in range(len(testa)):
    natax.append(tot_res.loc[testa.iloc[i,0],['Review Word Count', 'Link to PDF of Reviewer', 'Reviewer Name']])
    #%
#natan=[]
#for i in range(len(testa)):
#    natan.append(tot_res.loc[testa.iloc[i,0],['Reviewer Name']])
    #%
natax = pd.concat(natax, axis=1, ignore_index=True, sort=False)
natax=natax.T
#%%
    #%
#tot_res.loc[testa.iloc[1,0],['Review Word Count', 'Link to PDF of Reviewer']]
#%
#nataa = pd.concat(nata, axis=1, ignore_index=True, sort=False)
#nataa=nataa.T
natax["check"]='nan'
#%
natax=pd.DataFrame(natax)
#%
#nata.iloc[:,0]= nata.iloc[:,0].astype(float) 
#%
#natax["Reviewer Name"]=natan['Reviewer Name']
#%
natax.iloc[:,0]= natax.iloc[:,0].astype(float)  
natax.iloc[:,3]= natax.iloc[:,3].astype(float)   
#%%
nata=pd.concat([nata,natax])
#%% 
nata.to_csv('rnd_chk_ongoing_tikka16720_ok3.csv', index=False, na_rep='NA') 
 #%%
nata=nata[nata['Reviewer Name']!='Susan Janso'] 
#%%
nata=nata[nata.index!=48]
#%%
import pandas as pd
#%%
f =  pd.read_csv('totaxl.txt', header=None)
#https://stackoverflow.com/questions/21546739/load-data-from-txt-with-pandas
#https://www.quora.com/How-do-I-open-a-URL-in-Google-Chrome-in-new-tab-using-Python
import webbrowser
for i in range(len(f)):
    url = f.iloc[i][0]
    webbrowser.open_new_tab(url)  
#%%
nata = pd.read_csv('rnd_chk_ongoing_tikka16720_ok3.csv', index_col=None, header=0)
#%%Results
nata.iloc[:,3]= nata.iloc[:,3].astype(float) 
np.mean(nata.iloc[:,3])
#%%
np.std(nata.iloc[:,3])
#%%
nata.iloc[:,0]= nata.iloc[:,0].astype(float) 
np.mean(nata.iloc[:,0])
#%%
np.std(nata.iloc[:,0])

rng=tot_res2['Review Word Count']
#%
import matplotlib.pyplot as plt
#rng = np.random.RandomState(10)  # deterministic random data
a = np.hstack(rng,)
_ = plt.hist(a, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
Text(0.5, 1.0, "Histogram with 'auto' bins")
plt.show()
#%%
#%%
a=[3928,
4568,
5589,
...,3928]
#%%
#tot_res=tot_res[tot_res.index!=a]
tot_res=tot_res.drop(oo, axis=0)
#%%

#%%
file_handle = open('noss.txt', 'r')
#%
lines_list = file_handle.readlines()
#%
cols= (int(val) for val in lines_list[0].split())
#%
# Do a double-nested list comprehension to get the rest of the data into your matrix
#https://stackoverflow.com/questions/6583573/how-to-read-numbers-from-file-in-python
my_data = [[int(val) for val in line.split()] for line in lines_list[1:]]
#%
oo=[]
for i in range(len(my_data)):
    oo.append(my_data[i][0])
    #%%

tot_res['Reviewer Name']
'Reviewing Date'
#%%
idx = pd.Index(tot_res['Reviewer Name'])
axan=idx.duplicated()
#%%
idx2 = pd.Index(tot_res['Reviewing Date'])
daxan=idx2.duplicated()
#%%
idx3 = pd.Index(tot_res['Date of Publication'])
paxan=idx3.duplicated()
#%%
idx4 = pd.Index(tot_res['Link to PDF of Reviewer'])
taxan=idx4.duplicated()
#%%
jaksan=[]
for i in range(len(daxan)):
    if daxan[i]==True and daxan[i]==True and paxan[i]==True and taxan[i]==True:
        jaksan.append(i)
#%%
tot_res2=tot_res
tot_res2=tot_res2.reset_index(drop=True)
utta=[]
for i in range(len(tot_res2)-1):
    if tot_res2['Reviewer Name'].loc[i]==tot_res2['Reviewer Name'].loc[i+1] and \
    tot_res2['Reviewing Date'].loc[i]==tot_res2['Reviewing Date'].loc[i+1] and \
    tot_res2['Date of Publication'].loc[i]==tot_res2['Date of Publication'].loc[i+1] and \
    tot_res2['Link to PDF of Reviewer'].loc[i]==tot_res2['Link to PDF of Reviewer'].loc[i+1] and \
    tot_res2['Review Word Count'].loc[i]==tot_res2['Review Word Count'].loc[i+1]:
        utta.append(i)
        #%%
idxa = pd.Index(utta)
axn=idxa.duplicated()
#axn0
#%%
tak=[]
for i in range(len(idxa)-1):
    if idxa[i]+1==idxa[i+1]:
        tak.append(idxa[i])
        #%%ok
tak2=[]
for i in range(len(tak)-1):
    if tak[i]+1==tak[i+1]:
        tak2.append(tak[i])        
#%%
tot_res2=tot_res2.drop(tak,axis=0)
#%%
tot_res2.to_csv('all_journals_tikka17720_ok4a.csv', index=False, na_rep='NA')
#%%
np.std(rng)
#%%
#tot_res2=pd.read_csv('all_journals_tikka17720_ok3a.csv', index_col=None, header=0)
