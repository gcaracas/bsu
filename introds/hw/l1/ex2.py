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
        
        
sss = list(finalDataframe[finalDataframe['values']=='day'])
sss
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


pivot_table(df, values='D', index=['A', 'B'],
...                     columns=['C'], aggfunc=np.sum)

pd.pivot_table(finalDataframe, values=['file1','file2'],index=['values'])
#dz1 = finalDataframe.isin({'values': list(wordstmp)})


    
#removing duplicates
#test = pd.DataFrame()
#dic2 = {"words": wordsnd }

#final = dict()
#for n in wordsnd:
#    finalDataframe[finalDataframe['values']==n]
#    final[n]=set(finalDataframe[finalDataframe['values']=='day'])

#list(finalDataframe[finalDataframe['values']=='day'])
#zz = finalDataframe.loc[finalDataframe['values'].isin(wordsnd)]
#zz2 = finalDataframe[finalDataframe['values'].isin([wordsnd])]

#zz2 = list(finalDataframe['values'])
#kseq = zz2
#vseq = 
#a=dict(zip(kseq, list(finalDataframe[kseq])))


#listValues = list(finalDataframe['values'])
#type(finalDataframe)
#finalDataframe.loc[finalDataframe['values'].isin(listValues)]
#df.loc[df['column_name'].isin(some_values)]
"""

with open(files[0], mode="r") as f:
    data = f.read()
    
with open(files[1], mode="r") as f:
    data2 = f.read()
    
# Split data into array or words, non case sensitive
word = re.split(r"\W+", data,  flags=re.IGNORECASE)
word2 = re.split(r"\W+", data2,  flags=re.IGNORECASE)

# Remove withe spaces and empty strings
cleanWord = [line for line in [l.strip() for l in word] if line]
cleanWord2 = [line for line in [l.strip() for l in word2] if line]

# Now we need to extract word by word, although we don't need to
# count the occurances, we will use this so we can build a dictionary
# latter on.
#cntr = Counter(cleanWord)
words = list(set(cleanWord))
words2 = list(set(cleanWord))


dict2 = {"filename":files[0], "value":pd.Series(words2)}
dict3 = pd.DataFrame(dict2)




#dd = dict3.melt()

#result=cntr.most_common()

# Now create a dictionary for all the words on this file
#dictioary1=dict(result)

#kseq=cleanWord
#vseq = "filename"
#aa=dict(zip(kseq, vseq))
"""