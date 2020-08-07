import pandas as pd
import numpy as np

def validation_check_time_interval(validation_df, df, temp_interval):
	'''
	This function will validate the testdata to make sure the temperature does not fluctuate suddenly.
	
	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	temp_interval = integer, the maximum interval of a temperature change

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
	'''

    if i != 0:
        if (df['thermocouple_temp_c'][i] >= (df['thermocouple_temp_c'][i-1] + temp_interval)) or (df['thermocouple_temp_c'][i] <= (df['thermocouple_temp_c'][i-1] - temp_interval)):
                validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'anomaly - jump in temperature (more than 5 degrees)'}, ignore_index=True)
         
  return validation_df
