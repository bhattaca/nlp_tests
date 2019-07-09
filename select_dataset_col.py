# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ( 'this is a test')
import pandas as pd
import re


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
def keep_alpha_numeric(text):
    #return text
    return re.compile('[\W_]+', re.UNICODE).sub(' ', text)
                      
df=pd.read_csv('~/Downloads/report-3kHgNEBph-run-Fkj5hnMYb.csv')
print ( df.shape)
clean_txt=pd.DataFrame([ remove_tags(str(row)) for row in df['content']])
clean_txt=pd.DataFrame([ keep_alpha_numeric(str(row)) for row in clean_txt.iloc[:,0]])
clean_txt.to_csv('/Users/arindam/Downloads/driver_cancellation_dataset.csv',index=False)
print ("done")




#remove share detials tag
text = open("/Users/arindam/Downloads/driver_cancellation_dataset.csv", "r")




text = ''.join([i for i in text]) \
    .replace("Share Details", "") \
    .replace("::","") \
    .replace(":","") \
    .replace("&#39;","\'") \
    .replace("\"","")
         
x = open("/Users/arindam/Downloads/driver_cancellation_datase_clean.csv","w")
x.writelines(text)
x.close()