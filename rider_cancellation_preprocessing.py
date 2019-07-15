#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:07:29 2019

@author: arindam

Rider Cancellation | datasets.
input is the raw data and output is the cleaned dataset.
"""
import pandas as pd
import re

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

import spacy  # For preprocessing



def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

def set_pandas_options() -> None:
    pd.options.display.max_columns = 1000
    pd.options.display.max_rows = 1000
    pd.options.display.max_colwidth = 250
    pd.options.display.width = None
    # pd.options.display.precision = 2  # set as needed

def strip_html(input):
    return str(BeautifulSoup(input, features="lxml").text).lower()

def cleaning(doc):
    #txt = [(token.lemma_) for token in doc if ((not token.is_stop) and str(token.pos) == "NOUN")]
    txt = [str(token.text) for token in doc if (str(token.pos_) in ("VERB"))]
    # for token in doc:
    #   print(token.text, token.dep_, token.head.text, token.head.pos_,
    #           [child for child in token.children])
    return ' '.join(txt)


set_pandas_options()
#### spacy load model
nlp = spacy.load('en_core_web_lg', disable=['ner', 'parser']) # disabling Named Entity Recognition for speed
print(nlp.pipe_names)


#read in the raw data.
df=pd.read_csv('/Users/arindam/Documents/Projects/kraken/data/rider_cancellation.csv')


tmp = df[1:150]  #set1
#tmp = df[151:300]
tmp = tmp[tmp.requester_type == 'Rider']

print ("INFO|SHAPE>",df.shape)
print ("INFO|SHAPE>", tmp.shape)


txt = [strip_html(el) for el in tmp['hm.content']]
txt = [el.rpartition(':')[2] for el in txt]
#txt = [el+'\n' for el in txt if el !=""]
print(len(txt))

file = open("/Users/arindam/Documents/Projects/kraken/data/rider_cancellation_pre_process.txt","w")
for el in range(1,len(txt)):
  file.write(tmp['btt.ancestor_2_name'].iloc[el]\
    + "%" + tmp['btt.ancestor_3_name'].iloc[el]\
      + "%" +tmp['btt.ancestor_4_name'].iloc[el]\
        + "%" + txt[el]\
          +"\n")
file.close()

## SPACY PARSER
txt = [cleaning(doc) for doc in nlp.pipe(txt, batch_size=5, n_threads=4)]

file = open("/Users/arindam/Documents/Projects/kraken/data/rider_cancellation_pre_process_parsed.csv","w",encoding='utf-8')
for el in txt:
  file.write(el)
  file.write(":")
file.close()
