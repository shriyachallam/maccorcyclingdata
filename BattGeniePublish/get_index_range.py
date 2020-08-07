import pandas as pd
import numpy as np

def get_index_range(df, cyc_range, cycle_step_idx = []):
    '''
    Given the testdata dataframe, this function returns the index range for the specified cycle range, 
    or if a cycle step index is passed, as subset of each cyle for only that specific cycle step.

    Parameters
    ----------
    df: the testdata dataframe
    cyc_range: array of the cycles you want the indices for
    cycle_step_idx: optional array with the step numbers that you want the indices if

    Outputs
    -------
    index_range = a vector of the range of df indices for the specified cycle range
	
'''
    # If we are passed a cycle step index, then we provide the indicies for only that step.
    if cycle_step_idx:
        index_range = []
        # There is probably a better way to do this, but it works and the number of cycles is never that high
        for i in range(cyc_range[0],cyc_range[1]+1):  # Need the '+1' so that we include the upper cycle.
            index_range = np.append( index_range,
                                       np.where((df['Cyc#'] == i) & (df["Step"] == cycle_step_idx[0]))[0][:])
    else:
        index_range = np.where(np.logical_and(df['Cyc#'] >= cyc_range[0] , df['Cyc#']<= cyc_range[1] ))[0][:]

    return index_range