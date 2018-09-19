import glob
import os
import re
import pandas as pd
import numpy as np
from collections import Counter
path = "files/"
files = glob.glob(path+"*.txt")

# first we need a list of all words in all files.
finalDataframe = pd.DataFrame()
for file in files:
    with open(file, mode="r") as f:
        data = f.read()
        # Split data into array of words, non case sensitive
        word = re.split(r"\W+", data,  flags=re.IGNORECASE)
        # Remove withe spaces and empty strings
        cleanWords = [line for line in [l.strip() for l in word] if line]
        # Remove duplicates, we don't want them
        words = list(set(cleanWords))
        # Add data into dictionary
        dictionary = {"filename":file, "values":pd.Series(words)}
        finalDataframe = finalDataframe.append(pd.DataFrame(dictionary))
        
        
# list of words in total
wordstmp = finalDataframe['values']
dic2 = { "words" : wordstmp }
df1 = pd.DataFrame(dic2)
df1 = df1.set_index("words")

sss2 = [finalDataframe['filename']=='files/file2.txt']
sss1 = [finalDataframe['filename']=='files/file1.txt']
sss1[0]

dd1=list(sss1[0])
df1['file1']= dd1

dd2=list(sss2[0])
df1['file2']=dd2

finalDataframe['file1']=dd1
finalDataframe['file2']=dd2

test1=pd.pivot_table(finalDataframe, values=['file1','file2'],index=['values'])

test3 = pd.crosstab(finalDataframe['values'], finalDataframe['filename'], margins=True)


# Remove last column which is the total. We don't need this.
test3 = test3.drop(columns=['All'])
for file in list(test3.columns.values):
    test3[file].replace([0,1],['',file],inplace=True)

chale1=test3.apply(lambda x: x.tolist(), axis=1)
