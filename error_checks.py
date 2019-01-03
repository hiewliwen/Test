import pandas as pd

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
    
    return df
