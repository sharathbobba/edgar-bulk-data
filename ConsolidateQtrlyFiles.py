# There is a new file every quarter, this program consolidates the data of multiple files.

# We will need numpy and pandas. diros since we are going to looping through the contents 
import numpy as np
import pandas as pd
import os as diros

# We will need a few dataframes to hold the filing data
df_10K = pd.DataFrame()
df_10Q = pd.DataFrame()
df_20F = pd.DataFrame()

# A few variables
var_10K = "10-K"
var_10Q = "10-Q"
var_20F = "20-F"
var_CF = "CF"
var_BS = "BS"
var_IS = "IS"
var_fln = var_10K

# Unzip all of the quarterly files into this folder. Each quarterly zip file will need to be in its own folder.
# <Will change in the next pass of updates to avoid the tedious unzipping of files>
# the datasets are available here https://www.sec.gov/dera/data/financial-statement-data-sets.html

folder_edgar = "Folder Location of the Unzipped Files"

# This commands gets the folders in the location into a list
qrt_folders = diros.listdir((folder_edgar))
# Should see the list of folders, one folder for each quarterly datasets
qrt_folders

# This command helps format the numeric data as string
df_col_types = {"sic":str,"cik":str,"fy":str}
# This example is for the 10-K (Annual Filings)
df_10K = pd.DataFrame()

folder_counter = 0
# looping through the list to get the data of every quarter
while folder_counter < len(qrt_folders):

# We get the each folder sequentially
  folder_edgar_quarterly = folder_edgar+"/"+qrt_folders[folder_counter]
  
# Sub has the list of companies that have filed in the quarter    
    df_sub = pd.read_csv((folder_edgar_quarterly+"/sub.txt"),sep="\t",dtype=df_col_types)
    
# We extracting only the key columns, the others can be ignored, "var_fln" specifies the filing (10-K,10-Q,20-F, etc.) of our interest
    df_sub_10q_10k_20F = df_sub[(df_sub["form"] == var_fln)][["adsh","cik","name","sic","countryba","form","period","fy","fp"]]
    
# Pre has the Presentation Materials (financial statements), linking the statement with the accounts
# use pre to identify the statement (BS/IS/CF/etc)    
    df_pre = pd.read_csv((folder_edgar_quarterly+"/pre.txt"),sep="\t",encoding="windows-1254",dtype=df_col_types)
    
# We want the Balance Sheet, Cash Flow and Income Statement
  df_pre_3FS = df_pre[(df_pre["stmt"] == var_CF) | (df_pre["stmt"] == var_BS) | (df_pre["stmt"] == var_IS)]
  
# Sub has the financial elements but not the numbers
    df_subpre = pd.merge(df_sub_10q_10k_20F,df_pre_3FS,on="adsh",how="left")
    df_subpre.sort_values(by=["name","fy","stmt","period","line"],inplace=True)
    df_subpre.rename(columns={"period":"ddate"},inplace=True)
    df_subpre["date_period"] = pd.to_datetime(df_subpre["ddate"],format='%Y%m%d')  
    df_pre_3FS = df_pre_3FS[["adsh","line","stmt","tag","version","plabel","negating"]]
    
# Num has the values, you will need to identify the relevant statements and pick up the values from num 
    df_num = pd.read_csv((folder_edgar_quarterly+"/num.txt"),sep="\t",encoding="windows-1254",dtype=df_col_types)
    df_subprenum = pd.merge(df_subpre,df_num,on=["adsh","tag","ddate"],how="inner")
    
# Add the year and quarter, this is useful to identify the quarter and year if the filing is incorrect ( and there are incorrect years in the filings)
    df_subprenum["FYQ"] = qrt_folders[folder_counter]

# Each Quarter will be appended to the 10K dataframe
    df_10K = df_10K.append(df_subprenum,ignore_index=True)

# These are counters to keep track of the progress
    print(qrt_folders[folder_counter])
    print("Counting")
    print("Entries in SUB")
    print(len(df_sub_10q_10k_20F))
    print("Entries in PRE")
    print(len(df_pre_3FS))
    print("Entries merged in SUB-PRE")
    print(len(df_subpre))
    print("Entries NUM")
    print(len(df_num))
    print("Entries merged in SUB-PRE-NUM")
    print(len(df_subprenum))
#    print("1,4 and 0 Entries Only")
#    print(len(df_ignore_coreg))
    print("Combined Entries")
    print(len(df_10K))   
                         
    folder_counter = folder_counter + 1
    
# Create a File combining all of the data. this is the file that will be used in subsequent steps
df_10K.to_csv((folder_edgar+"/edgar_10K_allentries.csv"))

# New Commit
