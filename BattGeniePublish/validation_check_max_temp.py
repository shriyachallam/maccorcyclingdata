import pandas as pd
import numpy as np

def validation_check_max_temp(validation_df, df, max_temp, temp_tol=3):
	'''
	This function will validate the testdata against the max temperature by making sure no steps surpass the max.
	
	Parameters
	----------
	validation_df = the validation dataframe where any errors will be recorded
	df = testdata dataframe
	max_temp = integer, the threshold for the highest temperature allowed

	Outputs
	-------
	validation_df = the validation dataframe with any errors listed
	
    Notes
    -----
    There are 3 possibilities of error messages:
    1. warning - temperature approaching the max! (current temperature + tol > max)
    2. error - temperature has surpassed the max! (current temperature >= max)
    3. ABORT - temperature is way too hot! (current temperature > max + tol)

	'''

    if ((max_temp-tol) <= (df['thermocouple_temp_c'][i]) <= (max_temp+tol)):
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - temperature has surpassed the max!'}, ignore_index=True)
    elif ((df['thermocouple_temp_c'][i]) > (max_temp+tol)):
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'ABORT - temperature is way too hot!'}, ignore_index=True)
    elif ((max_temp-tol) < (df['thermocouple_temp_c'][i])):
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'warning - temperature approaching the max!'}, ignore_index=True)
    return validation_df
