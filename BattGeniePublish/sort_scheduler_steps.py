import pandas as pd
import numpy as np

def sort_scheduler_steps(schedule_df):
	'''
    Given the schedule_df (the df of the schedule file), this function will sort rest, charge, discharge, advance
    cycle, and end step numbers.
	
	Parameters
	----------
    schedule_df: the cleaned dataframe of the schedule file

	Outputs
	-------
    rest_steps: array of the steps from the schedule file that correlate to rest steps
	charge_steps: array of the steps from the schedule file that correlate to charging steps
    advance_steps: array of the steps from the schedule file that correlate to steps when the cycle is advanced
    discharge_steps: array of the steps from the schedule file that correlate to discharging steps
    end_steps: array of the steps from the schedule file that correlate to ending steps
    max_step: integer of the last step from the schedule file

	'''

    rest_steps = []
    charge_steps = []
    advance_steps = []
    discharge_steps = []
    end_steps = []
    for i in schedule_df.index:
        if schedule_df['step_type'][i] == "Rest":
            rest_steps.append(i+1)
        if schedule_df['step_type'][i] == "Charge":
            charge_steps.append(i+1)
        if schedule_df['step_type'][i] == "Discharge":
            discharge_steps.append(i+1)
        if schedule_df['step_type'][i] == "Advance Cycle":
            advance_steps.append(i+1)
        if schedule_df['step_type'][i] == "End":
            end_steps.append(i+1)        
        max_step = schedule_df["step"].iloc[-1]
    return rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step
