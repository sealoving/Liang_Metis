import numpy as np
import pandas as pd
import os
import glob

def CleanTurnstileReset(x):
    return(x.diff()[(x.diff()>=0) & (x.diff()<50000)].sum())

directory = os.getcwd()+'/data'
files = glob.glob(os.path.join(directory, "turnstile*.txt"))
df = pd.concat(map(pd.read_csv, files))

df = df.drop(['LINENAME','DIVISION'],axis=1)
df = df[df.DESC=='REGULAR'].drop('DESC',axis=1)
byTurnstile = df.groupby(['STATION','DATE','C/A','UNIT','SCP']).agg(CleanTurnstileReset)
byStation = byTurnstile.groupby(['STATION','DATE']).sum()
byStation.to_csv('byStation.csv')

# df = pd.read_csv('byStation.csv')
# df['weekday'] = pd.to_datetime(df['DATE']).dt.weekday_name
# df.set_index(['STATION','DATE'])




