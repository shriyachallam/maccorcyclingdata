import pandas as pd
import numpy as np
import os

def import_maccor_data(file_path , file_name, header=0):
    """
    Given the file path and file name of the testdata file, this function will import the csv file as a pandas df
    and clean it.

    Parameters
    -----------
    file_path : string
        File path

    file_name : string
        Filename
    
    header : integer
        Optional input that sets the header to a line number (default=2)
    
    Returns
    --------
    df : pandas dataframe
        The cleaned testdata file as a pandas df

    Examples
    ---------
    >>> import maccorcyclingdata.testdata as testdata
    >>> df = testdata.import_maccor_data('example_data/', 'testdata.csv')
    >>> df.head(5)
    """
    
    df = pd.read_csv(file_path+file_name, header =int(header))
    df = clean_maccor_df(df)
    return df

def import_multiple_csv_data(file_path):
    """
    Given the file path that holds multiple csv files (testdata files), this function will import and append 
    all of the csv files to one another as one dataframe. Returns a cleaned version of that dataframe.

    Parameters
    -----------
    file_path : string
        File path

    Returns
    --------
    df : pandas dataframe
        All of the cleaned csv files appended to one another as a pandas df

    Notes
    -----
    This function will append the csv files to one another depending on the order they appear in the directory.

    Examples
    ---------
    >>> import maccorcyclingdata.testdata as testdata
    >>> mult_df = testdata.import_multiple_csv_data('example_data/multiple_csv/')
    >>> mult_df.head(5)
    """

    df = pd.DataFrame()
    # r=root, d=directories, f = files
    for r, d, files in os.walk(file_path):
        # We only want to parse files that are CSVs
        files = [ file for file in files if file.endswith( ('.csv') ) ]
        files.sort()
        for file in files:
            file_loc = str(file_path+file)
            temp_df = pd.read_csv(file_loc, header=0)
            df = df.append(temp_df, ignore_index = True)
    df = clean_maccor_df(df)
    return df


def clean_maccor_df(df):
    """
    Given the testdata dataframe, this function will rename the headers and drop unnecessary columns. It will also change some of the units to match the column name and will remove all commas.

    Parameters
    -----------
    df : pandas dataframe
        The testdata dataframe

    Returns
    --------
    df : pandas dataframe
        The cleaned pandas df of the testdata

    Notes
    -----
    If the following columns exist, the function will delete these: ``ACR``, ``DCIR``, ``Watt-hr``, and ``nnnamed``.
    Examples
    ---------
    >>> import maccorcyclingdata.testdata as testdata
    >>> df = testdata.clean_maccor_df(df)
    >>> df.head(5)
    """
    
    if 'Watt-hr' in df.columns:
        df = df.drop(columns=['Watt-hr']) 
    if 'ACR' in df.columns:
        df = df.drop(columns=['ACR']) 
    if 'DCIR' in df.columns:
        df = df.drop(columns=['DCIR']) 
    if 'Unnamed: 13' in df.columns:
        df = df.drop(columns=['Unnamed: 13']) 
    df.replace(',','', regex=True, inplace=True)
    df.columns = ['cyc', 'step', 'test_time_s', 'step_time_s', 'capacity_mah', 'current_ma', 'voltage_v', 'dpt_time', 'thermocouple_temp_c', 'ev_temp'] #rename the column headers

    df[["cyc", "step", "test_time_s", "capacity_mah", "current_ma", "voltage_v", "thermocouple_temp_c", "ev_temp"]] = df[["cyc", "step", "test_time_s", "capacity_mah", "current_ma", "voltage_v", "thermocouple_temp_c", "ev_temp"]].apply(pd.to_numeric)
    
    return df

def delete_cycle_steps(df, steps_to_delete, decrement=False):
    """
    Given the testdata dataframe and a list of integers (step numbers that you want to delete), this function
    will delete all rows from the dataframe that have a cycle step index that matches any in the list of integers 
    
    Parameters
    -----------
    df : pandas dataframe
        The testdata dataframe

    steps_to_delete : array
        An array that has the step numbers you want to delete

    decrement : boolean
        If set to True, would shift cycle steps to adjust for the deleted steps

    Returns
    --------
    df : pandas dataframe
        The dataframe with the corresponding steps deleted

    Examples
    ---------
    >>> import maccorcyclingdata.testdata as testdata
    >>> del_df = testdata.delete_cycle_steps(df, [1], True)
    >>> del_df.head(5)
    """
    for x in steps_to_delete:
        to_be_deleted = df.index[df['step'] == x]
        df = df.drop(to_be_deleted)

    if decrement:
        steps_to_delete.sort(reverse = True) 
        for x in steps_to_delete:
            to_be_shifted = df.index[df['step'] > x]
            mini = min(df['step'][to_be_shifted].values)
            gap = mini-x
            all_values_larger = ((df['step'][to_be_shifted].values) - gap)
            df.loc[to_be_shifted, 'step'] = all_values_larger

    df = df.reset_index(drop = True)           
    return df

def get_index_range(df, cyc_range, cycle_step_idx = []):
    """
    Given the testdata dataframe, this function returns the index range for the specified cycle range, 
    or if a cycle step index is passed, as subset of each cyle for only that specific cycle step.
    
    Parameters
    -----------
    df : pandas dataframe
        The testdata dataframe

    cyc_range : array
        An array of the cycles you want the indices for

    cycle_step_idx : array
        The step numbers that you want the indices of. Default value is all steps within each cycle.

    Returns
    --------
    index_range : vector
        A vector of the range of df indices for the specified cycle range

    Examples
    ---------
    >>> from maccorcyclingdata.testdata import get_index_range
    >>> ind = testdata.get_cycle_data(df, [1, 3, 5], [12])
    >>> print(ind[:6])
    """
    
    # If we are passed a cycle step index, then we provide the indicies for only that step.
    if len(cycle_step_idx) > 0:
        index_range = []
        # There is probably a better way to do this, but it works and the number of cycles is never that high
        for i in range(cyc_range[0],cyc_range[1]+1):  # Need the '+1' so that we include the upper cycle.
            index_range = np.append( index_range,
                                       np.where((df['cyc'] == i) & (df["step"] == cycle_step_idx[0]))[0][:])
    else:
        index_range = np.where(np.logical_and(df['cyc'] >= cyc_range[0] , df['cyc']<= cyc_range[1] ))[0][:]

    return index_range

def get_cycle_data(df, Headings , cyc_range, cycle_step_idx=[]):
    """
    This function gets the data specified in the "Headings" for each sample within the specified cyc_range.
    
    Parameters
    -----------
    df : pandas dataframe
        The testdata dataframe

    Headings : array
        An array with the headers you want the data for

    cyc_range : array
        An array of the cycle numbers you want data for

    cycle_step_idx : array
        The step numbers within each cycle that you want the data for. Default value is all steps within each cycle.

    Returns
    --------
    data_df : pandas dataframe
        A pandas dataframe that has the data for the specified headers at the specified cycles and steps.

    Examples
    ---------
    >>> from maccorcyclingdata.testdata import get_cycle_data
    >>> data = testdata.get_cycle_data(df, ['current_ma', 'voltage_v'], [1, 3, 5], [12])
    >>> print(data[:6])
    """

    # Find the index range for the specified cycle(s)
    index_range = get_index_range(df,cyc_range, cycle_step_idx)
    np.set_printoptions(suppress=True)
    # Create a numpy array to hold the headings values Each column will be a heading, each row will be a data point
    data = np.zeros([len(index_range),len(Headings)])

    data_df = pd.DataFrame()
    data_df['cyc'] = df['cyc'][index_range].values
    data_df['step'] = df['step'][index_range].values

    for i in range(0,len(Headings)):
        data[:,i] = df[Headings[i]][index_range]
        data_df[Headings[i]] = data[:,i]

    return data_df

def get_num_cycles(df):
    """
    Given the testdata dataframe, this function will return the number of cycles.
    
    Parameters
    -----------
    df : pandas dataframe
        The testdata dataframe

    Returns
    --------                                   
    number_of_cycles : integer
        An integer of the number of cycles in the dataframe

    Notes
    ------
    This function assumes that the first cycle is cycle 0.

    Examples
    ---------
    >>> from maccorcyclingdata.testdata import get_num_cycles
    >>> get_num_cycles(df)
    """

    number_of_cycles = int(max(df['cyc'])) + 1
    return number_of_cycles 

