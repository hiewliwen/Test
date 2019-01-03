import sys
import pandas as pd
from tkinter import messagebox

G = 0.0980665       # Gravitation constant (conventional standard value)


def read_data_from_file (file_full_path, method = 'Auto'):
    ''' (tuple of str, [str or int]) -> DataFrame
    Return a Pandas DataFrame that contains the FRF data.
    Method = 'Auto' by default. DataFrame will be automatically cleaned of non-number
    data. If an integer is passed into method, then the same number of rows will be skipped
    during import.
    '''
    
    if file_full_path.lower().endswith(('.xls','.xlsx')):
        if method == 'Auto':
            df = pd.DataFrame(pd.read_excel(file_full_path,
                                            header = 0,
                                            index_col = 0,
                                            usecols = 1,
                                            dtype = 'float'))

        elif str(method).isdigit():         
            df = pd.DataFrame(pd.read_excel(file_full_path,
                                            header = None,
                                            skiprows = int(method),
                                            index_col = 0,
                                            usecols = 1,
                                            dtype = 'float'))
                                            # Use Pandas to read excel data into DataFrame
        else:
            messagebox.showerror('Error','Unsupported paramenter in "read_rt_from_file - excel"')
            sys.exit('Error')
                                        
    else:
        if messagebox.askokcancel('CSV 1.2 is not supported.', 'Please check the CSV version.',
                                   icon = 'warning') == False:
            sys.exit('CSV 1.2')
            
        if method == 'Auto':
            df = pd.DataFrame(pd.read_csv(file_full_path, 
                                          header = 0,
                                          index_col = 0,
                                          usecols = 1,
                                          dtype = 'float'))
                    
        elif str(method).isdigit():
            df = pd.DataFrame(pd.read_csv(file_full_path, 
                                          header = 0,
                                          index_col = False,
                                          skiprows = int(method),
                                          usecols = 1,
                                          dtype = 'float'))
                                          # Use Pandas to read excel data into DataFrame
        else:
            messagebox.showerror('Error','Unsupported Method in "read_rt_from_file - csv"')
            sys.exit('Error')

    return df


def create_kt_df(df_unique, df, rep = '1'):    
    
    frames = {}
    
    for vcm in df_unique:

        vcm_data_pair = df.loc[(df.VCM == vcm) & (df.Rep == rep)].reset_index(drop = True)
           
        fp_250 = (vcm_data_pair.loc[(vcm_data_pair.Current =='250') , 'FPath']).values[0] 
        fp_150 = (vcm_data_pair.loc[(vcm_data_pair.Current =='150') , 'FPath']).values[0]
        
        df_kt_250 = (read_data_from_file(fp_250))
        df_kt_150 = (read_data_from_file(fp_150))

        df_kt = pd.concat([df_kt_250, df_kt_150], axis = 1)
        df_kt.index.rename('Angle', inplace = True)
        df_kt.columns = ['250mA', '150mA']
        
        df_kt[r'g*cm/A'] = (df_kt['250mA'] - df_kt['150mA']) * 10
        df_kt[r'N*mm/A'] = df_kt[r'g*cm/A'] * G
        
        frames[vcm] = df_kt
        
    return frames
    

def create_rt_df(df_unique, df, rep = '1'):    
    
    frames = {}
    
    for vcm in df_unique:
        
        fp = df.loc[(df.VCM == vcm), 'FPath'].values[0]
        
        df_rt = (read_data_from_file(fp))

        df_rt.index.rename('Angle', inplace = True)
        df_rt.columns = [r'g*cm']
        df_rt[r'N*mm'] = df_rt[r'g*cm'] * G
        
        frames[vcm] = df_rt
        
    return frames


def find_max_rt(df_rt, RT_START_ANGLE, RT_END_ANGLE):
    
    df = pd.DataFrame()
    
    df_rt = df_rt.truncate(before = RT_START_ANGLE, after = RT_END_ANGLE)

    df['Angle'] = df_rt.idxmax(axis = 0)
    df['Rt'] = df_rt.max(axis = 0)
    
    return df
    
    
    