import pandas as pd
import numpy as np

def validation_check_rest(validation_df, df, rest_steps):
	'''
	This function will validate the testdata against the rest steps by making sure the current is at 0 when resting.
	
	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	rest_steps = array of the rest steps from the schedule file

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
	'''

    if df['step'][i] in rest_steps:
        if df['current_ma'][i] != 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is not at 0 during rest step'}, ignore_index=True)
    return validation_df
