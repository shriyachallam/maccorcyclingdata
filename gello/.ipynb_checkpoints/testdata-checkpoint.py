import pandas as pd
import numpy as np

def import_maccor_data(file_path , file_name, header=2):
	'''
	Given the file_path and file name of the testdata .csv file, this function will import the csv datafile as a df
	and clean it.
	
	Parameters
	----------
	file_path: a string of the file path
	file_name: a string of the file name

	Outputs
	-------
	df: the cleaned testdata file as a pandas df
	
	Notes
	-----
	Optional input: set the header to a line number.
    The default value is 2.

	'''
	
	df = pd.read_csv(file_path+file_name,sep='\t', header)  # Read data from .txt is the line the data starts on

	df = clean_maccor_df(df)
    
	return df

def import_multiple_csv_data(file_path):
	'''
    Given the file path that holds multiple csv files (testdata files), this function will import and append 
    all of the csv files to one another as one dataframe. Returns a cleaned version of that dataframe. 
	
	Parameters
	----------
    file_path: string with the file path to the directory of the csv files

	Outputs
	-------
    df: a dataframe with all of the cleaned csv files appended to one another
	
	Notes
	-----
	This function will append the csv files to one another depending on the order they appear in the directory.

	'''

    df = pd.DataFrame()
    # r=root, d=directories, f = files
    for r, d, files in os.walk(file_path):

        # We only want to parse files that are CSVs
        files = [ file for file in files if file.endswith( ('.CSV') ) ]
        files.sort()

        for file in files:
            print(file)
            temp_df = pd.read_csv(file_path+file) # Read data from .csv file
            df = df.append(temp_df, ignore_index = True)
    
    df = clean_maccor_df(df)

    return df


def clean_maccor_df(df):
	'''
	Given the testdata dataframe, this function will rename the headers and drop unnecessary columns. 
	
	Parameters
	----------
	df: the testdata dataframe

	Outputs
	-------
	Outputs the cleaned dataframe.
	
	Notes
	-----
	Maccor mislabels the Voltage column (as of 5/05/2020) so this function also changes the units of Voltage.
	Changes the datatype of the Watt-hr column to numeric

	'''
	df['Watt-hr'] = pd.to_numeric(df['Watt-hr'], errors='coerce')

	# Rename various columns to use
	df.rename(columns={'Cyc#':'cyc'}, inplace=True)
	df.rename(columns={'Step':'step'}, inplace=True)
	df.rename(columns={'TestTime(s)':'test_time_s'}, inplace=True)
	df.rename(columns={'StepTime(s)':'step_time_s'}, inplace=True)
	df.rename(columns={'Capacity(Ah)':'capacity_mah'}, inplace=True)
	df.rename(columns={'Watt-hr':'energy_wh'}, inplace=True)
	df.rename(columns={'Current(A)':'current_ma'}, inplace=True)
	df.rename(columns={'Voltage(V)':'voltage_mv'}, inplace=True)
	df.rename(columns={'DPt Time':'dpt_time'}, inplace=True)
	df.rename(columns={'ACR':'acr'}, inplace=True)
	df.rename(columns={'DCIR':'dcir'}, inplace=True)
	df.rename(columns={'Temp 1':'thermocouple_temp_c'}, inplace=True)
	df.rename(columns={'EV Temp':'ev_temp'}, inplace=True)
	df.rename(columns={'Unnamed: 13':'nnnamed'}, inplace=True)
    
	# drop the ones we dont want
	df = df.drop(columns=['acr', 'dcir', 'nnnamed']) 
    
	# Change the units
	df.voltage_mv = df.voltage_mv * 1e3
    
	return df

def delete_cycle_steps(df, steps_to_delete, decrement=False):
	'''
    Given the testdata dataframe and a list of integers (step numbers that you want to delete), this function
    will delete all rows from the dataframe that have a cycle step index that matches any in the list of integers 
    
    The function has an optional argument (default false) which, if set to True, would decrement all cycle steps 
    ahead any steps that are deleted. 
	
	Parameters
	----------
    df: the dataframe that you want to delete steps from
    steps_to_delete: an array that has the step numbers you want to delete
    decrement: optional boolean, if true will shift step numbers to compensate for the deleted steps

    Outputs
    -------
    df: the dataframe with the corresponding steps deleted
    
	Notes
	-----
	the decrement parameter is optional. The default value if False.

	'''
    for x in steps_to_delete:
        to_be_deleted = df.index[df['step'] == x]
    
        if decrement:
            to_be_shifted = df.index[df['step'] > x]
            all_values_larger = ((df['step'][to_be_shifted]) - 1)
            df['step'][to_be_shifted] = all_values_larger
            
    df = df.drop(to_be_deleted)  

    df = df.reset_index(drop = True)           
    return df

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

def get_num_cycles(df):
	'''
    Given the testdata dataframe, this function will return the number of cycles.
	
	Parameters
	----------
	df: the testdata dataframe

	Outputs
	-------
	number_of_cycles: an integer of the number of cycles in the dataframe
	
	'''

    number_of_cycles = int(max(df['Cyc#']))
    return number_of_cycles 

