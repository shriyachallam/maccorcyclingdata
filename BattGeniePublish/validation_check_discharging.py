import pandas as pd
import numpy as np

def validation_check_discharging(validation_df, df, discharge_steps):
	'''
	This function will validate the testdata against the discharging steps by making sure the current is negative
	
	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	discharge_steps = array of the discharging steps from the schedule file

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
	'''

    if df['step'][i] in discharge_steps:
        if df['current_ma'][i] >= 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is positive during discharging'}, ignore_index=True)
    return validation_df
