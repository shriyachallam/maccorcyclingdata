import unittest
import maccorcyclingdata.schedules as schedules
import os
import pytest
import pandas as pd

expath = "example_data/"
exfile = "schedule_short.csv"

def test_import_schedules_BadIn():

    expath1 = 1
    with pytest.raises(TypeError):
        schedules.import_schedules(expath1, exfile)

    exfile1 = 0
    with pytest.raises(TypeError):
        schedules.import_schedules(expath, exfile1)

    exfile2 = 'false_df.csv'
    with pytest.raises(NotADirectoryError):
        schedules.import_schedules(expath, exfile2)

    return

def test_sort_scheduler_steps_BadIn():

    schedule_df = 'not a dataframe'
    with pytest.raises(TypeError):
        schedules.sort_scheduler_steps(schedule_df)

    schedule_df1 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        schedules.sort_scheduler_steps(schedule_df1)

    schedule_df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    with pytest.raises(IndexError):
        schedules.sort_scheduler_steps(schedule_df2)

    return

def test_import_schedules_Out():
    schedule_df = schedules.import_schedules(expath, exfile)
    schedule_df = schedule_df.astype('object').dtypes
    df_test = pd.DataFrame(data={"step": [1,2,3,4,5,6,7], "step_type": ['Rest','Discharge','Charge','Advance Cycle','Do3','End',''], "step_mode": ['','Current','Current','','','',''], "step_mode_value": ['',0.75,0.75,'','','',''], "step_limit": ['','Voltage','Voltage','','','',''], "step_limit_value": ['',2.5,4.2,'','','',''], "step_end_type": ['Step Time','Voltage','Current','','','',''], "step_end_type_op": ['=','<=','<=','','','',''], "step_end_type_value": ['5:00:00','2.5','0.15','','','',''], "goto_step": [2,3,6,'','','',''], "report_type": ['Step Time','Step Time','Step Time','','','',''], "report_type_value": ['0:01:00','0:00:05','0:00:05','','','',''], "options": ['4NNN','4NNN','4NNN','','','',''], "step_note": ['','','','','','','']})
    df_test = df_test.astype('object').dtypes
    assert(df_test.equals(schedule_df))
    return

def test_sort_scheduler_steps_Out():
    schedule_df = schedules.import_schedules(expath, exfile)
    rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step = schedules.sort_scheduler_steps(schedule_df)
    assert(rest_steps == [1])
    assert(charge_steps == [3])
    assert(advance_steps == [4])
    assert(discharge_steps == [2])
    assert(end_steps == [6])
    assert(max_step == 7) 
    return
