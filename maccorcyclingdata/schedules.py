import pandas as pd
import numpy as np

def import_schedules(file_path, file_name):
    """
    Given the file path and file name (of the schedule file that is inputted into the Maccor Cycler), this 
    function will import and clean the schedule file and return it as a df. 

    Parameters
    -----------
    file_path : string
        File path

    file_name : string
        Filename

    Returns
    --------
    df : pandas dataframe
        A cleaned schedule df

    Notes
    ------
    The schedule file should be input as a csv.
    
    Examples
    ---------
    >>> import maccorcyclingdata.schedules as schedules
    >>> schedule_df = schedules.import_schedules('example_data/','schedule.csv')
    >>> schedule_df.head(5)
    """

    df = pd.read_csv(file_path + file_name)
    df = df.dropna(how='all') #delete the rows that are completely blank
    df.columns = ['step', 'step_type', 'step_mode', 'step_mode_value', 'step_limit', 'step_limit_value', 'step_end_type', 'step_end_type_op', 'step_end_type_value', 'goto_step', 'report_type', 'report_type_value', 'options', 'step_note'] #rename the column headers
    df = df.reset_index(drop=True) #reset the df index
    #this section of the function creates an array that has the indices of the row where the multi-row step starts    
    arr = []
    for ind in df.index: 
        if pd.isnull(df['step'][ind]):
            arr.append((ind-1)) #array contains all indices of when the step is "nan" - 1 (basically, the logic is that the row before the row where the step is nan is when the multi-line step begins)
    for x in range((len(arr) - 1), -1, -1): #iterates through the array backwards (however, since the multi-line steps are not just two lines long and can be three/four/etc lines long, if the values are consecutive it means it is still a part of the previous multi-line group so it needs to be deleted)
        if (arr[x]) == (arr[x - 1] + 1):
            del arr[x]
    for x in arr:
        #the only columns that have multi-line steps are end_type, op, value, and goto, so make an array for each of those columns (the arrays hold the value of the first line of multi-line step group)
        end_type = [df['step_end_type'][x]]
        op = [df['step_end_type_op'][x]]
        value = [df['step_end_type_value'][x]]
        goto = [df['goto_step'][x]]
        ind = x + 1
        while pd.isnull(df['step'][ind]): #each time the line after the first line of the multi-line group has a null value at the step it is appended to the arrays with respect to the column, once the next line returns a not null value at the step column, it means it has moved on to the next step
            end_type.append(df['step_end_type'][ind])
            op.append(df['step_end_type_op'][ind])
            value.append(df['step_end_type_value'][ind ])
            goto.append(df['goto_step'][ind])
            #df = df.drop([df.index[ind]]) #delete the row whose values were just appended to the arrays
            ind += 1
        df_update = pd.DataFrame({'step_end_type': [end_type], 'step_end_type_op': [op], 'step_end_type_value': [value], 'goto_step': [goto]}, index=[x])
        df.update(df_update) #add the arrays into their respective places in the original df

    df = df.dropna(subset=['step'])
    #set the type of the step columns to int
    df = df.astype({'step': int})
    df = df.reset_index(drop=True) #reset the df index
    return df

def sort_scheduler_steps(schedule_df):
    """
    Given the schedule_df (the df of the schedule file), this function will sort rest, charge, discharge, advance
    cycle, and end step numbers.

    Parameters
    -----------
    schedule_df : pandas dataframe
        The cleaned dataframe of the schedule file

    Returns
    --------
    rest_steps : array
        An array of the steps from the schedule file that correlate to rest steps
    
    charge_steps : array 
        An array of the steps from the schedule file that correlate to charging steps
    
    advance_steps : array 
        An array of the steps from the schedule file that correlate to steps when the cycle is advanced
    
    discharge_steps : array 
        An array of the steps from the schedule file that correlate to discharging steps
    
    end_steps : array 
        An array of the steps from the schedule file that correlate to ending steps
    
    max_step : integer 
        The last step from the schedule file

    Examples
    ---------
    >>> import maccorcyclingdata.schedules as schedules
    >>> rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step = sort_scheduler_steps(schedule_df)
    """

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
        if (str(schedule_df['step_type'][i])).startswith("Do"):
            do = str(schedule_df['step_type'][i])
            do = do.replace("Do", "")
            do = int(do)
            done = False
            while not done:
                if (str(schedule_df['step_type'][do-1])).startswith("Do"):
                    do = str(schedule_df['step_type'][do-1])
                    do = do.replace("Do","")
                    do = int(do)
                    done = False
                else:
                    if schedule_df['step_type'][do-1] == "Rest":
                        rest_steps.append(i+1)
                    if schedule_df['step_type'][do-1] == "Charge":
                        charge_steps.append(i+1)
                    if schedule_df['step_type'][do-1] == "Discharge":
                        discharge_steps.append(i+1)
                    if schedule_df['step_type'][do-1] == "Advance Cycle":
                        advance_steps.append(i+1)
                    if schedule_df['step_type'][do-1] == "End":
                        end_steps.append(i+1)
                    done = True
    return rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step
