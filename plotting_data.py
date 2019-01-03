import matplotlib.pyplot as plt
import os


# (Function) Plot Rt with Peaks Individually 
def plot_rt(df_rt, rt_peak, file_names):
    ''' (list of DataFrame, list of Series, tuple of str) -> Figures
    Plot 1 Rt graph with peak marker per data file
    '''
    
    for i in range(len(file_names)):    # Plot as many time as there are files
        title = os.path.splitext(os.path.basename(file_names[i]))[0].upper()
                                        # Remove file extension from file name,
                                        # Change the file name to uppercase
        
        rt_x = df_rt[i]['Angle']        # Assign X values (Angle)
        rt_y = df_rt[i]['N-mm']         # Assign Y values (N-mm)
        peak_x = rt_peak[i]['Angle']    # Assign X peak marker (Angle)
        peak_y = rt_peak[i]['N-mm']     # Assign Y peak marker (N-mm)
        
        
        fig = plt.figure(i+1)           # Name the figures starting at Figure 1
        fig.canvas.set_window_title(title)
        f = fig.add_subplot(111)        # To facilitate adding of data label
        
        plt.plot(rt_x, rt_y, '-',)      # Plot Rt Data
        plt.plot(peak_x, peak_y, 'x',)  # Plot Rt peak marker
        
        plt.title(title)                # Title the chart with file name
        plt.xlabel('Angle (°)')         # Label the X-axis
        plt.ylabel('Rt (N-mm)')         # Label the Y-axis

        
        f.annotate('{:.2f} N-mm'.format(peak_y), # Add Rt peak data label
                   xy=(peak_x, peak_y),
                   xytext=(peak_x, peak_y))
        
    plt.show()     # Display all plots at a go
    return None


def plot_rt_peaks(combine_rt_peaks):
    
    

    plt.figure()
    plt.boxplot(combine_rt_peaks["N-mm"])
    plt.show()
    return None









# Close all created figure(s)
def destroy_figure():
    ''' 
    Destroy all figures
    '''
    
    plt.close("all")
    return None