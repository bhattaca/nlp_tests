#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:07:29 2019

@author: arindam

#Rider Cancellation datasets. 
input is the raw data and output is the cleaned dataset. 
"""
import pandas as pd
import re


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')
    
def set_pandas_options() -> None:
    pd.options.display.max_columns = 1000
    pd.options.display.max_rows = 1000
    pd.options.display.max_colwidth = 199
    pd.options.display.width = None
    # pd.options.display.precision = 2  # set as needed

set_pandas_options()
    
    
#read in the raw data. 
df=pd.read_csv('/Users/arindam/Documents/Projects/kraken/data/rider_cancellation.csv')


tmp= df[0:100]
print ( "INFO|SHAPE>",df.shape)
print ( "INFO|SHAPE>",tmp.shape)
print_full ( tmp['hm.content'].to_string())
