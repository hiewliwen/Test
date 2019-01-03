# Import external modules
import os
import tkinter
import pandas as pd
from file_operation import select_files, destroy_window, split_file_name, group_data_files
from data_processing import create_kt_df, create_rt_df, find_max_rt
from plotting_data import plot_rt, destroy_figure, plot_rt_peaks
import matplotlib.pyplot as plt

G = 0.0980665                   # Gravitation constant (conventional standard value)
ANGLE_CRITERIA = [0.4,14,44]    # Kt angles criteria. User editable.
KT_TORQUE_UNIT = r'N*mm/A'
RT_TORQUE_UNIT = r'N*mm'
RT_START_ANGLE = 0
RT_END_ANGLE = 10

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
    ''' Rt Operation '''
      
    file_full_path = select_files()
    df = group_data_files(file_full_path, 'rt')
    unique_vcm = df.VCM.unique()
    
    frames = create_rt_df(unique_vcm, df)
    df_frames = pd.concat(frames, axis=1, names=['VCM', 'Variables'])
    df_rt = df_frames.xs(RT_TORQUE_UNIT, axis = 1, level = 1)
    
    ### SPLIT VCM SAMPLE ###
    
    
    df_max_rt = find_max_rt(df_rt, RT_START_ANGLE, RT_END_ANGLE)
    
    df_rt.plot(kind = 'line', title = 'Rt ({})'.format(RT_TORQUE_UNIT))
    df_max_rt.plot(y = 'Rt', kind = 'box', title = 'Max Rt ({})'.format(RT_TORQUE_UNIT))
       
#    
#    '''
#    # Writing data back into Excel
#    writer = pd.ExcelWriter('test.xlsx')
#    peaks_array.to_excel(writer, 'Sheet1', index = False)
#    writer.save()
#    '''

    
def kt():
    ''' Kt Operation '''
      
    file_full_path = select_files()             # Get user to select data file(s)
    
     ### BROKEN ###
#    are_files_valid(file_names_full_path)                         # Check whether the files are valid
    
    df = group_data_files(file_full_path, 'kt')
    unique_vcm = df.VCM.unique()
     
    df_kt_criteria = pd.DataFrame() 
    
    frames = create_kt_df(unique_vcm, df)
    df_frames = pd.concat(frames, axis=1, names=['VCM', 'Variables'])
    d = df_frames.xs(KT_TORQUE_UNIT, axis = 1, level = 1)
    
    for angle in ANGLE_CRITERIA:
        df_kt_criteria[angle] = d.iloc[d.index.get_loc(angle, method='nearest')]

    d.plot()
    df_kt_criteria.plot(kind = 'box')
    plt.show()



if __name__ == '__main__':
    init()
#    rt()
    kt()