import re
import os
import pandas as pd
import sys
from tkinter import filedialog, messagebox,Tk

# Use Tkinter as file open dialog GUI
def select_files(operation = ''):
    '''
    Invoke a file open dialog GUI and ask user to select data files.
    '''

    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    files_full_path = filedialog.askopenfilenames(parent = root,
                                                  initialdir = '/', 
                                                  title = 'Select file',
                                                  defaultextension = '.xlsx',
                                                  filetypes = (('Excel','*.xls *.xlsx'),('CSV','*.csv')))
                                                # Use Tkinter built-in file dialog GUI

    destroy_window()                            # Destroy that window after using the file dialog GUI
    files_full_path = pd.Series(files_full_path, dtype = 'str')
    
    return files_full_path


### TODO: COMMENT THIS
def group_data_files(file_full_path, mode):
    
    
    if mode == 'kt':   
        header = ['FPath', 'VCM', 'Current', 'Rep']
    elif mode == 'rt':
        header = ['FPath', 'VCM', 'Rep']
    else:
        messagebox.showerror('Error','Unsupported method in "group_data_files".\n Only "kt" and "rt" are supported.')
        sys.exit('Error')
    
    files_list = pd.DataFrame(split_file_name(file_full_path))
        
    df_files_list = pd.concat([file_full_path, files_list], axis = 1, sort = False)
    df_files_list.columns = header[:len(df_files_list.columns)]
    df_files_list = df_files_list.reindex(columns=header)
    df_files_list.Rep.fillna(1,inplace = True)

    return df_files_list


### TODO: COMMENT THIS 
def split_file_name(df):
    '''
    Strip the 
    '''
    
    df = df.apply(lambda x: os.path.splitext(os.path.basename(x))[0])
    df = df.str.split('[_-]', expand = True)
    df = df.applymap(lambda x: x.strip() if type(x) is str else x)
    
    return df


# Destory Tk window after file dialog
def destroy_window():
    '''
    Destory the Tk GUI window
    '''
    
    global root             # Pull the 'root' variable from the global pool
    try:                    # Try to...
        root.destroy()      # Close root window
    except:                 # If it cannot be closed...
        pass                # do nothing. Root window might not exist at all


# Error handling on (1)no file selected, (2)wrong file type selected
### TODO: Wrong Logic. Decide on every loop check or not. 
def are_files_valid(file_names):
    ''' (list of str) -> bool

    Check whether the file names in the list are valid type by checking for:
    (1) A file is selected.
    (2) The file type is either .xls, .xlsx, .csv
    If any of the file names are not valid, error message is shown and
    application quits

    >>> are_files_valid('')
    sys.exit()

    >>> are_files_valid('A.xls','B.jpg')
    sys.exit

    >>> are_files_valid('A.xls','B.xlsx')
    None    
    '''
    
    if not file_names:          # Check if any file(s) are selected by user
        messagebox.showerror('Open file','No file(s) selected')
        sys.exit('No Files')
    
    for file in file_names:     # Check if file extensions are supported
        if not file.lower().endswith(('.xls','.xlsx','.csv')):
            messagebox.showerror('Open file','File type(s) not supported')
            sys.exit('Wrong File Type')