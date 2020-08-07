import pandas as pd
from BattGeniePublish.clean_maccor_df import clean_maccor_df

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