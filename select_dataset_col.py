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
                      
df=pd.read_csv('~/Downloads/report-3kHgNEBph-run-nXPEvxtw7.csv')
print ( df.shape)
clean_txt=pd.DataFrame([ remove_tags(str(row)) for row in df['content']])
clean_txt.to_csv('~/Downloads/eaters_large_dataset.csv',index=False)


