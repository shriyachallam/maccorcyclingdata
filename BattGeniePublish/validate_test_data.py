import pandas as pd
import numpy as np
from BattGeniePublish/sort_scheduler_steps import sort_scheduler_steps
from BattGeniePublish/validation_check_rest import validation_check_rest
from BattGeniePublish/validation_check_advanced_cycle import validation_check_advanced_cycle
from BattGeniePublish/validation_check_charging import validation_check_charging
from BattGeniePublish/validation_check_discharging import validation_check_discharging
from BattGeniePublish/validation_check_max_step_num import validation_check_max_step_num
from BattGeniePublish/validation_check_max_temp import validation_check_max_temp
from BattGeniePublish/validation_check_time_interval import validation_check_time_interval
from BattGeniePublish/validation_check_temp_interval import validation_check_temp_interval

def validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp):
	'''
    This is a wrapper function that validates the testdata against the schedule file.
    The sub-functions that are validated are: 
    - validation_check_rest(validation_df, df, rest_steps)
    - validation_check_charging(validation_df, df, charge_steps)
    - validation_check_discharging(validation_df, df, discharge_steps)
    - validation_check_advanced_cycle(validation_df, df, advance_steps)
    - validation_check_max_step_num(validation_df, df, max_step)
    - validation_check_max_temp(validation_df, df, max_temp)
    - validation_check_time_interval(validation_df, df, time_interval)
    - validation_check_temp_interval(validation_df, df, temp_interval)
	
	Parameters
	----------
    schedule_df = the dataframe of the cleaned schedule file
    df = testdata dataframe
    cell_id = the cell id of the testdata
    time_interval = integer, the maximum interval of how often the cycler should be recording data
	temp_interval = integer, the maximum interval of a temperature change
    max_temp = integer, the threshold for the highest temperature allowed

	Outputs
	-------
    validation_df = a dataframe that lists all (if any) errors
    Headers of the validation_df:
    1. time (the current time of when the validation occurs)
    2. run (tells whether the validation function is in progress or complete)
    3. cell_num (the cell number of the testdata)
    4. row_number (the row number where the error occurs)
    5. error (what the error is)

    NOTES 
    -----
    for the max temperature error, there are 3 possibilities of error messages:
    1. warning - temperature approaching the max! (current temperature + tol > max)
    2. error - temperature has surpassed the max! (current temperature >= max)
    3. ABORT - temperature is way too hot! (current temperature > max + tol)

	'''

    column_names = ["time", "run", "cell_num", "row_number", "error"]
    validation_df = pd.DataFrame(columns = column_names)
    rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step = sort_scheduler_steps(schedule_df)
    for i in df.index: 
        validation_df = validation_check_rest(validation_df, df, rest_steps)
        validation_df = validation_check_charging(validation_df, df, charge_steps)
        validation_df = validation_check_discharging(validation_df, df, discharge_steps)
        validation_df = validation_check_advanced_cycle(validation_df, df, advance_steps)
        validation_df = validation_check_max_step_num(validation_df, df, max_step)
        validation_df = validation_check_max_temp(validation_df, df, max_temp)
        validation_df = validation_check_time_interval(validation_df, df, time_interval)
        validation_df = validation_check_temp_interval(validation_df, df, temp_interval)

    if validation_df.empty:
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'run complete', 'cell_num': cell_id, 'row_number': '-', 'error': 'there are no errors'}, ignore_index=True)
        return validation_df
    validation_df = validation_df.append({'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'run complete', 'cell_num': cell_id, 'row_number': '-', 'error': 'errors listed above'}, ignore_index=True)
    return validation_df
