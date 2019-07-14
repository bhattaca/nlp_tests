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
    return BeautifulSoup(input, features="lxml").text

def cleaning(doc):
    txt = [token.lemma_ for token in doc if not token.is_stop]
    return ' '.join(txt)


set_pandas_options()
#### spacy load model
nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser']) # disabling Named Entity Recognition for speed
print(nlp.pipe_names)


#read in the raw data.
df=pd.read_csv('/Users/arindam/Documents/Projects/kraken/data/rider_cancellation.csv')


tmp = df[1:20]
tmp = tmp[tmp.requester_type == 'Rider']

print ("INFO|SHAPE>",df.shape)
print ("INFO|SHAPE>", tmp.shape)


txt = [strip_html(el) for el in tmp['hm.content']]
print ( txt)
#txt = [cleaning(doc) for doc in nlp.pipe(tmp['hm.content'], batch_size=500, n_threads=4)]

#print ( "func strip_html >", strip_html(tmp['hm.content']), "\n")

