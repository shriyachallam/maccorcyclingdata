import pandas as pd
import numpy as np

def validation_check_max_step_num(validation_df, df, max_step):
	'''
	This function will validate the testdata against the max step by making sure no steps surpass the max.
	
	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	max_step = integer, the last step from the schedule file

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
	'''

    if df['step'][i] > max_step:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - this step number surpasses the steps in scheduler'}, ignore_index=True)
    return validation_df
