import pandas as pd
import numpy as np
from BattGeniePublish.get_index_range import get_index_range

def get_cycle_data(df, Headings , cyc_range):
    '''
    This function gets the data specified in the "Headings" for each sample within the specified cyc_range.
   
     Parameters
    ----------
    df = testdata dataframe
    Headings = array with the headers you want the data for
    cyc_range = array of the cycle numbers you want data for

    Outputs
    -------
    data = a numpy array where the columns correspond to the headings and the rows correspond to the data point
    '''
   
    # Find the index range for the specified cycle(s)
    index_range = get_index_range(df,cyc_range)
 
    # Create a numpy array to hold the headings values Each column will be a heading, each row will be a data point
    data = np.zeros([len(index_range),len(Headings)])
    for i in range(0,len(Headings)):
            data[:,i] = df[Headings[i]][index_range].values

    return data