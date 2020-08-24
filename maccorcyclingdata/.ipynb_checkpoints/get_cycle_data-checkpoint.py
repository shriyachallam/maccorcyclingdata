'''
This function gets the data specified in the "Headings" for each sample within the specified cyc_range.
If a cycle_step_idx argument is passed, then it only passes values for that subset of the cycle.
Note: As of 1/29/20, if you pass a cycle_step_idx, you can only get the data for one cycle range,
otherwise the time scale will be screwed up.

Outputs:
    time_range.values = The time at each step. takes step zero of cyc_range[0] to be the zero time.
    cyc_range = The range of cycle steps to pull data from. 
    cycle_step_idx = The specific cycle steps to get the data for. If no step is set,
                     then data is pulled for the whole cycle
'''
def get_cycle_data(df, Headings , cyc_range , cycle_step_idx = []):
    
    # Find the index range for the specified cycle(s)
    index_range = get_index_range(df,cyc_range,cycle_step_idx)
 
    # Create a numpy array to hold the headings values Each column will be a heading, each row will be a data point
    data = np.zeros([len(index_range),len(Headings)])
    for i in range(0,len(Headings)):
            data[:,i] = df[Headings[i]][index_range].values

    return data