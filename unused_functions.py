# (Function) Read the Excel or CSV file that is passed into this function
def read_rt_from_file (file_name, method = 'Auto'):
    ''' (tuple of str, [str or int]) -> DataFrame
    Return a Pandas DataFrame that contains the FRF data.
    Method = 'Auto' by default. DataFrame will be automatically cleaned of non-number
    data. If an integer is passed into method, then the same number of rows will be skipped
    during import.
    '''
    
    col_names = ['Angle','g-cm']        # Assign column names
    
    if file_name.lower().endswith(('.xls','.xlsx')):
        if method == 'Auto':
            df = pd.DataFrame(pd.read_excel(file_name,
                                            header = None,
                                            names = col_names,
                                            usecols = 1))
#            trim_start_data(df)
            df = df_to_numeric(df)

        elif str(method).isdigit():         
            df = pd.DataFrame(pd.read_excel(file_name,
                                            header = None,
                                            skiprows = 1,
                                            names = col_names,
                                            usecols = 1))
                                            # Use Pandas to read excel data into DataFrame
        else:
            messagebox.showerror('Error','Unsupported Method in "read_rt_from_file - excel"')
            sys.exit('Error')
                                        
    else:
        if messagebox.askokcancel('CSV 1.2 is not supported.', 'Please check the CSV version.',
                               icon = 'warning') == False:
            sys.exit('CSV 1.2')
            
        if method == 'Auto':
            df = pd.DataFrame(pd.read_csv(file_name, 
                                          header = None,
                                          names = col_names))
            
            df = df_to_numeric(df)
            
        elif str(method).isdigit():
            df = pd.DataFrame(pd.read_csv(file_name, 
                                          header = None,
                                          names = col_names,
                                          index_col = False,
                                          skiprows = method))
                
        else:
            messagebox.showerror('Error','Unsupported Method in "read_rt_from_file - csv"')
            sys.exit('Error')
              
#        df.drop(df.index[-10:], inplace = True) # Remove the last 10 results. Usually errorenous... 
#                                                # due to loadcell hitting hardstop
    
    df = trim_data(df,10,0)
    # to be replaced ^ with pd.clip()
    
    return df


def trim_start_data(df):
    ''' (DataFrame -> DataFrame)
    Check whether the first data point is 0°. If it is not, the function
    will attempt to search for it and remove preceding lines. 
    '''
    
    if df.Angle[0] != 0:
        try:
            smallest_angle = df.loc[df.Angle == 0].index[0]
        except:
            smallest_angle = df.Angle.idxmin(axis = 'Angle')
        
        df.drop(df.index[:smallest_angle], inplace = True)


def trim_data (df, max_angle, min_angle = 0):
    ''' (DataFrame, float, float) -> Dataframe
    Trim Rt data to angles between rtMaxAngle and rtMinAngle.
    This will remove the errorenous data when actuator hits the hardstop.
    '''
    
    if (max_angle <= min_angle) or (not isinstance(max_angle, (float, int))):
        max_angle = df['Angle'].iloc[-11]
    
    if (min_angle >= max_angle) or (not isinstance(min_angle, (float, int))):
        min_angle = df['Angle'].iloc[0]
        
    df = df[(df['Angle'] >= min_angle) & (df['Angle']<= max_angle)]
    df = df.reset_index(drop=True)
    
    if df.empty: df_isempty()
    
    return df
    

def df_to_numeric(df):
    ''' (DataFrame) -> DataFrame
    Remove all non-numeric data in DataFrame, cast the DataFrame to float and 
    finally reset the index.
    '''
    
    df = df[pd.to_numeric(df.Angle, errors='coerce').notnull()]
    df = df.astype('float32')
    df.reset_index(inplace = True, drop = True)
    return df

def df_isempty():
    '''
    DataFrame is empty after conversion to numeric. An error has occurred.
    '''
    
    from tkinter import messagebox
    messagebox.showerror('Critical Error','Check that 1st Column of Excel File is Angle Data!')
    sys.exit('Wrong Data Structure')


# (Function) Convert g-cm to N-mm
def convert_gcm_to_nmm (df_rt):
    ''' (list of DataFrame) -> list of DataFrame
    Return a Pandas DataFrame that converts data in 'g-cm' to N-mm and 
    adds a new column to the original DataFrame
    '''
    
    df_rt['N-mm'] = df_rt['g-cm'] * G       # Convert g-cm to N-mm
    return df_rt                            


# (Function) Find peaks in data frames
def find_peak_in_rt(df_rt):
    ''' (list of DataFrame) -> list of Series

    Return the peak index on N-mm using Pandas idxmax function
    '''
    
    idx_peak = df_rt['N-mm'].idxmax(axis = 'N-mm')  # Find the index of peak in column ('N-mm')
    return df_rt.iloc[idx_peak]                     # Return the values at peak row in the DataFrame


def combine_rt_peaks(rt_peak):
    return pd.DataFrame(rt_peak)