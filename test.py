import timeit
import pandas as pd
import numpy as np
import os

#def split_kt_file_name(file_full_path):
#    '''
#    Strip the 
#    '''
#    
#    df = file_full_path
#    df = df.apply(lambda x: os.path.splitext(os.path.basename(x))[0])
#    df = df.str.split('-', expand = True)
#    df = df.applymap(str.strip)
#    
#    return df
#
#def series():
#    split_kt_file_name(df_file_full_path)
#    return split_kt_file_name
#
#
#def time_lists(file_full_path):
#    return None
#
#file_full_path = (r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 1 - 150 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 1 - 150 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 1 - 250 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 1 - 250 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 2 - 150 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 2 - 150 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 2 - 250 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 2 - 250 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 3 - 150 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 3 - 150 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 3 - 250 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 3 - 250 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 4 - 150 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 4 - 150 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 4 - 250 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 4 - 250 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 5 - 150 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 5 - 150 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 5 - 250 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Competitor 5 - 250 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Customer Ref - 150 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Customer Ref - 150 - 2.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Customer Ref - 250 - 1.xlsx', 
#                    r'D:/Google Drive/MMI Data Analysis/Rt/Kt Data/Customer Ref - 250 - 2.xlsx')
#
#cycles = 1000
#df_file_full_path = pd.Series(file_full_path)
#
#series_time = timeit.timeit(series, number=cycles)
#
#print('Series = {}sec for {} of cycles\n'.format(series_time, cycles))


d = {'A': pd.DataFrame([0, 1, 2], [2, 2, 4]), 'B': pd.DataFrame([1, 1, 1], [2, 2, 2])}
d

df = pd.concat(d.values(), keys=d.keys())
df

