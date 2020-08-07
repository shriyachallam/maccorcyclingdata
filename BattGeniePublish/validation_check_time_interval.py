import pandas as pd
import numpy as np

def validation_check_time_interval(validation_df, df, time_interval):
	'''
	This function will validate the testdata to make sure data has been collected at every time interval.
	
	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	time_interval = integer, the maximum interval of how often the cycler should be recording data

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
	'''

    if i != 0:
        if df['test_time_s'][i] > (df['test_time_s'][i-1] + time_interval):
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'anomaly - more than ' + str(time_interval) + ' seconds has passed since the last collected data'}, ignore_index=True)
         
  return validation_df
