import pandas as pd
from BattGeniePublish.clean_maccor_df import clean_maccor_df

def import_maccor_data(file_path , file_name):
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
	This function sets the header as the second line **

	'''
	
	df = pd.read_csv(file_path+file_name,sep='\t', header = 2)  # Read data from .txt is the line the data starts on

	df = clean_maccor_df(df)
    
	return df