# Import external modules
import os
import tkinter
import pandas as pd
from file_operation import select_files, are_files_valid, destroy_window
from data_processing import read_rt_from_file, find_peak_in_rt, convert_gcm_to_nmm
from plotting_data import plot_rt, destroy_figure

def init():
    ''' Perform initialization '''
    root = tkinter.Tk()         # Assign a name to the main Tkinter GUI
    root.withdraw()             # Hide that window from view
    
    try:                        # Try to perform cleaning of workspace by...
        destroy_window()        # closing the main Tkinter GUI and... 
        destroy_figure()        # closing all created figures 
    except:                     # If they cannot be closed...
        pass                    # do nothing. They may not have existed


def rt():
    ''' Main loop '''
    df_rt, rt_peak, peaks_to_excel = ([] for i in range(3))     # Initialized variables
    
    file_names = select_files()                         # Get user to select data file(s)
    are_files_valid(file_names)                         # Check whether the files are valid
    splitted = splitFilename(file_names)
    
#    for i in range(len(file_names)):                    # For each selected file(s)...
#        df_rt.append(read_rt_from_file(file_names[i]))  # Use Pandas to read Excel files
#        convert_gcm_to_nmm(df_rt[i])                    # Convert g-cm to N-mm
#        rt_peak.append(find_peak_in_rt(df_rt[i]))       # Find the max Rt
#    
#    plot_rt(df_rt, rt_peak, file_names)                 # Plot the Rt & max figures


def splitFilename(file_names):
   
    file_name = []
    split_file_name = []
    
    for i in range(len(file_names)):
        _, file_name[i] = os.path.split(file_names[i])
        split_file_name[i] = file_name[i].split("_")
        return split_file_name

#dict_filename = {'File','Model1','Model2','Measurement','Sample','Number'}













'''   
def export(file_names):
    # Writing data back into Excel
    writer = pd.ExcelWriter('test.xlsx')
                 
    for i in range(len(file_names)):                    # Export every Rt data of to individual Excel worksheet
        title = os.path.splitext(os.path.basename(file_names[i]))[0].upper()
        df_rt[i].to_excel(writer, title, index = False) # Using Pandas Excel writer to export the data
    
    writer.save()                                       # Save the Excel
        
    #peaks_to_excel.pd.concat(peaks_array)
    
    
    #for i in range(len(peaks_array)):
    #    peaks_to_excel = pd.concat([peaks_to_excel, peaks_array[i]], axis = 1, join = 'inner')
       
    
    # Writing data back into Excel
    writer = pd.ExcelWriter('test.xlsx')
    peaks_array.to_excel(writer, 'Sheet1', index = False)
    writer.save()
'''


if __name__ == "__main__":
    init()
    rt()