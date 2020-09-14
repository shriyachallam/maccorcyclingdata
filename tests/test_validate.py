import unittest
import maccorcyclingdata.validate as validate
import os
import pytest
import pandas as pd
import maccorcyclingdata.schedules as schedules
import maccorcyclingdata.testdata as testdata

validation_df = pd.DataFrame(columns=["time", "run", "cell_num", "row_number", "error"])
df = pd.DataFrame(columns=['cyc', 'step', 'test_time_s', 'step_time_s', 'capacity_mah', 'current_ma', 'voltage_v', 'dpt_time', 'thermocouple_temp_c', 'ev_temp'])
schedule_df = pd.DataFrame(columns=['step', 'step_type', 'step_mode', 'step_mode_value', 'step_limit', 'step_limit_value', 'step_end_type', 'step_end_type_op', 'step_end_type_value', 'goto_step', 'report_type', 'report_type_value', 'options', 'step_note'])
time_interval = 60
i = 1
cell_id = 7
temp_interval = 5
discharge_neg = False
maximum_step = 25
max_temp = 50
expath = 'example_data/'
exfile = 'testdata_errors.csv'
sched_file = 'schedule_errors.csv'

def test_validation_check_time_intervalBadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_time_interval(validation_df1, df, time_interval, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_time_interval(validation_df2, df, time_interval, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_time_interval(validation_df3, df, time_interval, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_time_interval(validation_df, df1, time_interval, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_time_interval(validation_df, df2, time_interval, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_time_interval(validation_df, df3, time_interval, i, cell_id)

    time_interval1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_time_interval(validation_df, df, time_interval1, i, cell_id)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_time_interval(validation_df, df, time_interval, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_time_interval(validation_df, df, time_interval, i, cell_id1)

    return

def test_validation_check_temp_interval_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_temp_interval(validation_df1, df, temp_interval, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_temp_interval(validation_df2, df, temp_interval, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_temp_interval(validation_df3, df, temp_interval, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_temp_interval(validation_df, df1, temp_interval, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_temp_interval(validation_df, df2, temp_interval, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_temp_interval(validation_df, df3, temp_interval, i, cell_id)

    temp_interval1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_temp_interval(validation_df, df, temp_interval1, i, cell_id)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_temp_interval(validation_df, df, temp_interval, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_temp_interval(validation_df, df, temp_interval, i, cell_id1)

    return

def test_validation_check_advanced_cycle_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_advanced_cycle(validation_df1, df, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_advanced_cycle(validation_df2, df, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_advanced_cycle(validation_df3, df, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_advanced_cycle(validation_df, df1, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_advanced_cycle(validation_df, df2, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_advanced_cycle(validation_df, df3, i, cell_id)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_advanced_cycle(validation_df, df, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_advanced_cycle(validation_df, df, i, cell_id1)

    return

def test_validation_check_charging_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_charging(validation_df1, df, schedule_df, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_charging(validation_df2, df, schedule_df, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_charging(validation_df3, df, schedule_df, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_charging(validation_df, df1, schedule_df, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_charging(validation_df, df2, schedule_df, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_charging(validation_df, df3, schedule_df, i, cell_id)

    schedule_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_charging(validation_df, df1, schedule_df1, i, cell_id)
    
    schedule_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_charging(validation_df, df2, schedule_df2, i, cell_id)
    
    schedule_df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    with pytest.raises(IndexError):
        validate.validation_check_charging(validation_df, df3, schedule_df3, i, cell_id)

    char_tol = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_charging(validation_df, df, schedule_df, i, cell_id, char_tol)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_charging(validation_df, df, schedule_df, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_charging(validation_df, df, schedule_df, i, cell_id1)

    return

def test_validation_check_discharging_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_discharging(validation_df1, df, schedule_df, i, cell_id, discharge_neg)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_discharging(validation_df2, df, schedule_df, i, cell_id, discharge_neg)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_discharging(validation_df3, df, schedule_df, i, cell_id, discharge_neg)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_discharging(validation_df, df1, schedule_df, i, cell_id, discharge_neg)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_discharging(validation_df, df2, schedule_df, i, cell_id, discharge_neg)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_discharging(validation_df, df3, schedule_df, i, cell_id, discharge_neg)

    schedule_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_discharging(validation_df, df1, schedule_df1, i, cell_id, discharge_neg)
    
    schedule_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_discharging(validation_df, df2, schedule_df2, i, cell_id, discharge_neg)
    
    schedule_df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    with pytest.raises(IndexError):
        validate.validation_check_discharging(validation_df, df3, schedule_df3, i, cell_id, discharge_neg)

    char_tol = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_discharging(validation_df, df, schedule_df, i, cell_id, discharge_neg, char_tol)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_discharging(validation_df, df, schedule_df, i1, cell_id, discharge_neg)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_discharging(validation_df, df, schedule_df, i, cell_id1, discharge_neg)

    return

def test_validation_check_max_step_num_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_max_step_num(validation_df1, df, maximum_step, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_max_step_num(validation_df2, df, maximum_step, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_max_step_num(validation_df3, df, maximum_step, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_max_step_num(validation_df, df1, maximum_step, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_max_step_num(validation_df, df2, maximum_step, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_max_step_num(validation_df, df3, maximum_step, i, cell_id)

    maximum_step1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_step_num(validation_df, df, maximum_step1, i, cell_id)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_step_num(validation_df, df, maximum_step, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_step_num(validation_df, df, maximum_step, i, cell_id1)

    return

def test_validation_check_max_temp_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_max_temp(validation_df1, df, max_temp, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_max_temp(validation_df2, df, max_temp, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_max_temp(validation_df3, df, max_temp, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_max_temp(validation_df, df1, max_temp, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_max_temp(validation_df, df2, max_temp, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_max_temp(validation_df, df3, max_temp, i, cell_id)

    max_temp1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_temp(validation_df, df, max_temp1, i, cell_id)

    temp_tol1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_temp(validation_df, df, max_temp1, i, cell_id, temp_tol1)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_temp(validation_df, df, max_temp, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_max_temp(validation_df, df, max_temp, i, cell_id1)

    return

def test_validation_check_rest_BadIn():

    validation_df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_rest(validation_df1, df, i, cell_id)

    validation_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_rest(validation_df2, df, i, cell_id)

    validation_df3 = pd.DataFrame(columns=[1,2,3,4,5])
    with pytest.raises(IndexError):
        validate.validation_check_rest(validation_df3, df, i, cell_id)

    df1 = 1
    with pytest.raises(TypeError):
        validate.validation_check_rest(validation_df, df1, i, cell_id)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validation_check_rest(validation_df, df2, i, cell_id)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validation_check_rest(validation_df, df3, i, cell_id)

    i1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_rest(validation_df, df, i1, cell_id)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validation_check_rest(validation_df, df, i, cell_id1)

    return

def test_validate_test_data_BadIn():

    df1 = 1
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df1, cell_id, time_interval, temp_interval, max_temp, discharge_neg)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validate_test_data(schedule_df , df2, cell_id, time_interval, temp_interval, max_temp, discharge_neg)
    
    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        validate.validate_test_data(schedule_df , df3, cell_id, time_interval, temp_interval, max_temp, discharge_neg)

    schedule_df1 = 1
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df1 , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg)
    
    schedule_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11])
    with pytest.raises(IndexError):
        validate.validate_test_data(schedule_df2 , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg)
    
    schedule_df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    with pytest.raises(IndexError):
        validate.validate_test_data(schedule_df3 , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg)

    char_tol1 = "not an integer"
    temp_tol=3
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg, temp_tol, char_tol1)

    time_interval1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id, time_interval1, temp_interval, max_temp, discharge_neg)

    temp_interval1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval1, max_temp, discharge_neg)

    max_temp1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp1, discharge_neg)

    temp_tol1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg, temp_tol1)

    discharge_neg1 = "not an boolean"
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg1)

    cell_id1 = "not an integer"
    with pytest.raises(TypeError):
        validate.validate_test_data(schedule_df , df, cell_id1, time_interval, temp_interval, max_temp, discharge_neg)

    return

def test_validate_test_data_Out():
    schedule_df = schedules.import_schedules(expath, sched_file)
    df = testdata.import_maccor_data(expath, exfile)
    validation_df = validate.validate_test_data(schedule_df , df, cell_id, time_interval, temp_interval, max_temp, discharge_neg, temp_tol=3, char_tol=2)
    validation_df = validation_df.astype('object').dtypes
    test_df = pd.DataFrame(data={"time": ['14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41,','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41','14/09/2020 14:39:41'],"run":['in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'in progress', 'run complete'],"cell_num":[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],"row_number":[1,1,2,3,3,4,4,5,6,6,8,10,10,11,12,13,15,15,16,17,18,19,19,20,20,20,'-'],"error":['max temp warning - temperature approaching the max of 50!',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'max temp error - temperature has surpassed the max of 50!',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'ABORT - temperature is way too hot! It has far surpassed the max of 50!',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'time interval anomaly - more than 60 seconds has passed since the last collected data',
        'rest step error - current is not at 0 during rest step',
        'max step error - this step number surpasses the steps in cycler schedule',
        'time interval anomaly - more than 60 seconds has passed since the last collected data',
        'discharging error - current_ma or voltage_v is at the wrong value',
        'discharging error - current_ma or voltage_v is at the wrong value',
        'max step error - this step number surpasses the steps in cycler schedule',
        'max step error - this step number surpasses the steps in cycler schedule',
        'time interval anomaly - more than 60 seconds has passed since the last collected data',
        'max step error - this step number surpasses the steps in cycler schedule',
        'max step error - this step number surpasses the steps in cycler schedule',
        'max step error - this step number surpasses the steps in cycler schedule',
        'time interval anomaly - more than 60 seconds has passed since the last collected data',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'max step error - this step number surpasses the steps in cycler schedule',
        'time interval anomaly - more than 60 seconds has passed since the last collected data',
        'temp interval anomaly - jump in temperature (more than 5 degrees)',
        'rest step error - current is not at 0 during rest step',
        'errors listed above']})
    test_df = test_df.astype('object').dtypes
    assert(test_df.equals(validation_df))
    return
