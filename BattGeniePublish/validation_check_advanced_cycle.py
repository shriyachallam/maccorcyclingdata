import pandas as pd
import numpy as np

def validation_check_advanced_cycle(validation_df, df, advance_steps):
	'''
	This function will validate the testdata against the advance cycle steps by making sure the cycle advances

	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	advance_steps = array of the advance_cycle steps from the schedule file

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
	'''

    if df['step'][i] in advance_steps:
        if df['cyc'][i] != (df['cyc'][i-1] + 1):
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - the cycle did not advance properly'}, ignore_index=True)
    return validation_df
