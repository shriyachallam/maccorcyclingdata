import pandas as pd
import numpy as np
from maccorcyclingdata.schedules import sort_scheduler_steps

def validation_check_time_interval(validation_df, df, temp_interval):
    """
    This function will validate the testdata to make sure the temperature does not fluctuate suddenly.

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    temp_interval : integer
        The maximum interval with any errors listed

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_time_interval
    >>> validation_check_time_interval(validation_df, df, 5)
    """

    if i != 0:
        if (df['thermocouple_temp_c'][i] >= (df['thermocouple_temp_c'][i-1] + temp_interval)) or (df['thermocouple_temp_c'][i] <= (df['thermocouple_temp_c'][i-1] - temp_interval)):
                validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'anomaly - jump in temperature (more than 5 degrees)'}, ignore_index=True)
         
    return validation_df

def validation_check_advanced_cycle(validation_df, df, advance_steps):
    """
    This function will validate the testdata against the advance cycle steps by making sure the cycle advances

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    advance_steps : array
        An array of the advance_cycle steps from the schedule file

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_advanced_cycle
    >>> validation_check_advanced_cycle(validation_df, df, [2, 4, 5])
    """

    if df['step'][i] in advance_steps:
        if df['cyc'][i] != (df['cyc'][i-1] + 1):
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - the cycle did not advance properly'}, ignore_index=True)
    return validation_df

def validation_check_charging(validation_df, df, charge_steps):
    """
    This function will validate the testdata against the charging steps by making sure the current is positive

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    charge_steps : array
        An array of the charging steps from the schedule file

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_charging
    >>> validation_check_charging(validation_df, df, [1, 3])
    """

    if df['step'][i] in charge_steps:
        if df['current_ma'][i] <= 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is negative during charging'}, ignore_index=True)
    return validation_df


def validation_check_discharging(validation_df, df, discharge_steps):
    """
    This function will validate the testdata against the discharging steps by making sure the current is negative

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    discharge_steps : array
        An array of the discharging steps from the schedule file

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_discharging
    >>> validation_check_discharging(validation_df, df, [6, 7])
    """

    if df['step'][i] in discharge_steps:
        if df['current_ma'][i] >= 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is positive during discharging'}, ignore_index=True)
    return validation_df

def validation_check_max_step_num(validation_df, df, max_step):
    """
    This function will validate the testdata against the max step by making sure no steps surpass the max.

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    max_step : integer
        The last step from the schedule file

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_max_step_num
    >>> validation_check_max_step_num(validation_df, df, 23)
    """

    if df['step'][i] > max_step:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - this step number surpasses the steps in scheduler'}, ignore_index=True)
    return validation_df

def validation_check_max_temp(validation_df, df, max_temp, temp_tol=3):
    """
    This function will validate the testdata against the max temperature by making sure no steps surpass the max.

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    max_temp : integer
        The threshold for the highest temperature allowed

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Notes
    ------
    There are 3 possibilities of error messages:

    1. warning - temperature approaching the max! (current temperature + tol > max)

    2. error - temperature has surpassed the max! (current temperature >= max)

    3. ABORT - temperature is way too hot! (current temperature > max + tol)


    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_max_temp
    >>> validation_check_max_temp(validation_df, df, 40, 4)
    """

    if ((max_temp-tol) <= (df['thermocouple_temp_c'][i]) <= (max_temp+tol)):
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - temperature has surpassed the max!'}, ignore_index=True)
    elif ((df['thermocouple_temp_c'][i]) > (max_temp+tol)):
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'ABORT - temperature is way too hot!'}, ignore_index=True)
    elif ((max_temp-tol) < (df['thermocouple_temp_c'][i])):
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'warning - temperature approaching the max!'}, ignore_index=True)
    return validation_df

def validation_check_rest(validation_df, df, rest_steps):
    """
    This function will validate the testdata against the rest steps by making sure the current is at 0 when resting.

    Parameters
    -----------
    validation_df : pandas dataframe
        The validation dataframe where any errors will be recorded

    df : pandas dataframe
        The testdata dataframe
    
    rest_steps : array
        An array of the rest steps from the schedule file

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors listed    
    
    Examples
    ---------
    >>> from maccorcyclingdata.validate import validation_check_rest
    >>> validation_check_rest(validation_df, df, 40, [8, 9])
    """

    if df['step'][i] in rest_steps:
        if df['current_ma'][i] != 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is not at 0 during rest step'}, ignore_index=True)
    return validation_df


def validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp, tol=3):
    """
    This is a wrapper function that validates the testdata against the schedule file.
    The sub-modules that are validated are: 

    - validation_check_rest(validation_df, df, rest_steps)

    - validation_check_charging(validation_df, df, charge_steps)

    - validation_check_discharging(validation_df, df, discharge_steps)

    - validation_check_advanced_cycle(validation_df, df, advance_steps)

    - validation_check_max_step_num(validation_df, df, max_step)

    - validation_check_max_temp(validation_df, df, max_temp)

    - validation_check_time_interval(validation_df, df, time_interval)

    - validation_check_temp_interval(validation_df, df, temp_interval)

    Parameters
    -----------
    schedule_df : pandas dataframe
        The dataframe of the cleaned schedule file

    df : pandas dataframe
        The testdata dataframe
    
    cell_id : integer
        The cell id of the testdata

    time_interval : integer
        The maximum interval of how often the cycler should be recording data

    temp_interval : integer
        The maximum interval of a temperature change

    max_temp : integer
        The threshold for the highest temperature allowed

    tol : integer
        Sets the tolerance between warning, error, and ABORT messages. Default is 3 degrees.

    Returns
    --------
    validation_df : pandas dataframe
        The validation dataframe with any errors (if any) listed    
        Headers of the validation_df:

        1. time (the current time of when the validation occurs)

        2. run (tells whether the validation function is in progress or complete)

        3. cell_num (the cell number of the testdata)

        4. row_number (the row number where the error occurs)

        5. error (what the error is)

    Notes
    ------
    There are 3 possibilities of error messages:

    1. warning - temperature approaching the max! (current temperature + tol > max)

    2. error - temperature has surpassed the max! (current temperature >= max)

    3. ABORT - temperature is way too hot! (current temperature > max + tol)


    Examples
    ---------
    >>> from maccorcyclingdata.validate import validate_test_data
    >>> validate_test_data(schedule_df , df, 7, 5, 5, 40, 4)
    """

    column_names = ["time", "run", "cell_num", "row_number", "error"]
    validation_df = pd.DataFrame(columns = column_names)
    rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step = sort_scheduler_steps(schedule_df)
    for i in df.index: 
        validation_df = validation_check_rest(validation_df, df, rest_steps)
        validation_df = validation_check_charging(validation_df, df, charge_steps)
        validation_df = validation_check_discharging(validation_df, df, discharge_steps)
        validation_df = validation_check_advanced_cycle(validation_df, df, advance_steps)
        validation_df = validation_check_max_step_num(validation_df, df, max_step)
        validation_df = validation_check_max_temp(validation_df, df, max_temp, tol)
        validation_df = validation_check_time_interval(validation_df, df, time_interval)
        validation_df = validation_check_temp_interval(validation_df, df, temp_interval)

    if validation_df.empty:
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'run complete', 'cell_num': cell_id, 'row_number': '-', 'error': 'there are no errors'}, ignore_index=True)
        return validation_df
    validation_df = validation_df.append({'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'run complete', 'cell_num': cell_id, 'row_number': '-', 'error': 'errors listed above'}, ignore_index=True)
    return validation_df
