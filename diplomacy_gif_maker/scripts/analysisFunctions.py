import os
import pandas as pd
import numpy as np

def results_ratio(country_order_results_reset):
    success_ratio_list = []
    failure_ratio_list = []
    country_list = []
    for i, row in country_order_results_reset.iterrows():
        if i%2==0:
            country_list.append(row['country'])
            success = row['result']        
        if i%2==1:
            failure = row['result']        
        if i%2==1:
            success_ratio_list.append(success/(success + failure))
            failure_ratio_list.append(failure/(success + failure))
    data_tuples = list(zip(country_list, success_ratio_list, failure_ratio_list))
    df = pd.DataFrame(data_tuples, columns=['country', 'success_ratio', 'failure_ratio'])    
    return df