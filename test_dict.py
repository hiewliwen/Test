# Import external modules
import os
import sys
from tkinter import filedialog, messagebox,Tk
import pandas as pd
from file_operation import select_files, are_files_valid, destroy_window, split_kt_file_name, group_data_files
from data_processing import read_rt_from_file, find_peak_in_rt, convert_gcm_to_nmm, combine_rt_peaks,read_kt_from_file, df_to_numeric
from plotting_data import plot_rt, destroy_figure, plot_rt_peaks

G = 0.0980665                   # Gravitation constant (conventional standard value)
angle_criteria = [0.4,14,44]    # Kt angles criteria. User editable.
torque_unit = r'N*mm/A'

def init():
    ''' Perform initialization '''
    
    root = Tk()         # Assign a name to the main Tkinter GUI
    root.withdraw()             # Hide that window from view
    
    try:                        # Try to perform cleaning of workspace by...
        destroy_window()        # closing the main Tkinter GUI and... 
        destroy_figure()        # closing all created figures 
    except:                     # If they cannot be closed...
        pass                    # do nothing. They may not have existed



def kt():
    ''' Kt Operation '''
    
#    kt_peak, peaks_to_excel, title, files_list = ([] for i in range(4))     # Initialized variables
    
    file_full_path = select_files('Kt')                           # Get user to select data file(s)
    
     ### BROKEN ###
#    are_files_valid(file_names_full_path)                         # Check whether the files are valid
    
    df = group_data_files(file_full_path)
    unique_vcm = df.VCM.unique()
     
    df_kt_criteria = pd.DataFrame() 
    
    frames = create_kt_df(unique_vcm, df)
    df_frames = pd.concat(frames, axis=1, names=['VCM', 'Variables'])
    d = df_frames.xs(torque_unit, axis = 1, level = 1)
    
    for angle in angle_criteria:
        df_kt_criteria[angle] = d.iloc[d.index.get_loc(angle, method='nearest')]

    d.plot()
    df_kt_criteria.plot.box()
    


def read_kt_from_file2 (file_full_path, method = 'Auto'):
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
            messagebox.showerror('Error','Unsupported Method in "read_rt_from_file - excel"')
            sys.exit('Error')
                                        
    else:
        if messagebox.askokcancel('CSV 1.2 is not supported.', 'Please check the CSV version.',
                               icon = 'warning') == False:
            sys.exit('CSV 1.2')
            
        if method == 'Auto':
            df = pd.DataFrame(pd.read_csv(file_full_path, 
                                          header = None,
                                          names = col_names))
            
            df = df_to_numeric(df)
            
        elif str(method).isdigit():
            df = pd.DataFrame(pd.read_csv(file_full_path, 
                                          header = None,
                                          names = col_names,
                                          index_col = False,
                                          skiprows = method))
                
        else:
            messagebox.showerror('Error','Unsupported Method in "read_rt_from_file - csv"')
            sys.exit('Error')
    

    return df
    
    
def create_kt_df(df_unique, df, rep = "1"):    
    
    frames = {}
    
    for vcm in df_unique:

        vcm_data_pair = df.loc[(df.VCM == vcm) & (df.Rep == rep)].reset_index(drop = True)
           
        fp_250 = (vcm_data_pair.loc[(vcm_data_pair.Current =="250") , "FPath"]).values[0] 
        fp_150 = (vcm_data_pair.loc[(vcm_data_pair.Current =="150") , "FPath"]).values[0]
        
        df_kt_250 = (read_kt_from_file2(fp_250))
        df_kt_150 = (read_kt_from_file2(fp_150))

        df_kt = pd.concat([df_kt_250, df_kt_150], axis = 1)
        df_kt.index.rename('Angle', inplace = True)
        df_kt.columns = ['250mA', '150mA']
        
        df_kt[r'g*cm/A'] = (df_kt['250mA'] - df_kt['150mA']) * 10
        df_kt[r'N*mm/A'] = df_kt[r'g*cm/A'] * G
        
        frames[vcm] = df_kt
        
    return frames
        

if __name__ == "__main__":
    init()
#    rt()
    kt()