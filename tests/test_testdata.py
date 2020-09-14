import unittest
import maccorcyclingdata.testdata as testdata
import os
import pytest
import pandas as pd
from pandas._testing import assert_frame_equal

expath = "example_data/"
exmult = "example_data/multiple_csv/"
exfile = "testdata_errors.csv"

def test_import_maccor_data_BadIn():

    expath1 = 1
    with pytest.raises(TypeError):
        testdata.import_maccor_data(expath1, exfile)

    exfile1 = 0
    with pytest.raises(TypeError):
        testdata.import_maccor_data(expath, exfile1)
    
    header1 = ''
    with pytest.raises(TypeError):
        testdata.import_maccor_data(expath, exfile, header1)

    exfile2 = 'false_df.csv'
    with pytest.raises(NotADirectoryError):
        testdata.import_maccor_data(expath, exfile2)

    return

def test_import_multiple_csv_BadIn():

    expath1 = 1
    with pytest.raises(TypeError):
        testdata.import_multiple_csv_data(expath1)

    expath2 = 'false_path/'
    with pytest.raises(NotADirectoryError):
        testdata.import_multiple_csv_data(expath2)
        
    return

def test_clean_maccor_df_BadIn():

    df = 'not dataframe'
    with pytest.raises(TypeError):
        testdata.clean_maccor_df(df)
    
    df_cols = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    with pytest.raises(IndexError):
        testdata.clean_maccor_df(df_cols)

    return

def test_delete_cycle_steps_BadIn():
    steps_to_delete = []
    df = pd.DataFrame()

    df1 = 'not dataframe'
    with pytest.raises(TypeError):
        testdata.delete_cycle_steps(df1)
    
    steps_to_delete1 = "not list"
    with pytest.raises(TypeError):
        testdata.delete_cycle_steps(df, steps_to_delete1)
    
    decrement = "not boolean"
    with pytest.raises(TypeError):
        testdata.delete_cycle_steps(df, steps_to_delete, decrement)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        testdata.delete_cycle_steps(df2, steps_to_delete)

    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10, 11])
    with pytest.raises(IndexError):
        testdata.delete_cycle_steps(df3, steps_to_delete)

    return

def test_get_index_range_BadIn():
    cyc_range = []
    df = pd.DataFrame()

    df1 = 'not dataframe'
    with pytest.raises(TypeError):
        testdata.get_index_range(df1, cyc_range)
    
    cyc_range1 = "not list"
    with pytest.raises(TypeError):
        testdata.get_index_range(df, cyc_range1)
    
    cycle_steps_idx1 = "not list"
    with pytest.raises(TypeError):
        testdata.get_index_range(df, cyc_range, cycle_steps_idx1)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        testdata.get_index_range(df2, cyc_range)

    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10, 11])
    with pytest.raises(IndexError):
        testdata.get_index_range(df3, cyc_range)

    return

def test_get_cycle_data_BadIn():
    headings = []
    cyc_range = []
    df = pd.DataFrame()

    df1 = 'not dataframe'
    with pytest.raises(TypeError):
        testdata.get_cycle_data(df1, headings, cyc_range)
    
    cyc_range1 = "not list"
    with pytest.raises(TypeError):
        testdata.get_cycle_data(df, headings, cyc_range1)
    
    cycle_steps_idx1 = "not list"
    with pytest.raises(TypeError):
        testdata.get_cycle_data(df, headings, cyc_range, cycle_steps_idx1)

    headings1 = "not list"
    with pytest.raises(TypeError):
        testdata.get_cycle_data(df, headings1, cyc_range)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        testdata.get_cycle_data(df2, headings, cyc_range)

    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10, 11])
    with pytest.raises(IndexError):
        testdata.get_cycle_data(df3, headings, cyc_range)

    return

def test_num_cycles_BadIn():
    df = pd.DataFrame()

    df1='not dataframe'
    with pytest.raises(TypeError):
        testdata.get_num_cycles(df1)
    
    df2 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10])
    with pytest.raises(IndexError):
        testdata.get_num_cycles(df2)

    df3 = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10, 11])
    with pytest.raises(IndexError):
        testdata.get_num_cycles(df3)

    return

def test_import_maccor_data_Out():
    df_test = pd.DataFrame(data={"cyc": [0,0,0,0,0], "step": [1,1,1,1,1], "test_time_s": [240.00,300.00,360.00,360.00,360.00], "step_time_s": [1,1,1,1,1], "capacity_mah": [0.0000,0.0000,0.0000,0.0000,0.0000], "current_ma": [0.0000,0.0000,0.0000,0.0000,0.0000], "voltage_v": [3.7095,3.7094,3.7095,3.7095,3.7095], "dpt_time": [1,1,1,1,1], "thermocouple_temp_c": [32.67,49.00,32.71,51.00,57.00], "ev_temp": [0,0,0,0,0]})
    df_test = df_test.astype('object').dtypes
    
    df = testdata.import_maccor_data(expath, exfile)
    assert(df['cyc'].iloc[-1] == 1)
    df = df.astype('object').dtypes

    assert(df.equals(df_test))

    return

def test_import_mutiple_csv_data_Out():
    df = testdata.import_multiple_csv_data(exmult)
    assert(df['cyc'].iloc[-1] == 900)
    df = df.astype('object').dtypes
    
    df_test = pd.DataFrame(data={"cyc": [869,869,869,869,869], "step": [11,11,11,11,11], "test_time_s": [5577644.47,5577649.47,5577654.47,5577659.47,5577664.47], "step_time_s": ['  0d 00:22:05.05','  0d 00:22:10.05','  0d 00:22:15.05','  0d 00:22:20.05','  0d 00:22:25.05'], "capacity_mah": [552.0699,554.1531, 556.2364,558.3196,560.4029], "current_ma": [1499.8856,1499.8856,1500.1144,1499.9619,1499.8856], "voltage_v": [3.92,3.9209,3.922,3.9226,3.9235], "dpt_time": [1,1,1,1,1], "thermocouple_temp_c": [30.08,30.13,30.2,30.2,30.1], "ev_temp": [0,0,0,0,0]})
    df_test = df_test.astype('object').dtypes

    assert(df.equals(df_test))
    return

def test_delete_cycle_steps_Out():
    df = testdata.import_maccor_data(expath, exfile)
   
    df_deleted = pd.DataFrame(data={"cyc": [1], "step": [27], "test_time_s": [0.0], "step_time_s": [0], "capacity_mah": [0.0], "current_ma": [0.0], "voltage_v": [0.0], "dpt_time": [0], "thermocouple_temp_c": [0.0], "ev_temp": [0]})
    df_deleted = df_deleted.astype('object').dtypes
    df_test = testdata.delete_cycle_steps(df, [1, 2, 15, 16, 10, 5], decrement=False)
    df_test = df_test.astype('object').dtypes
    assert(df_test.equals(df_deleted))

    df_deleted1 = pd.DataFrame(data={"cyc": [1], "step": [1], "test_time_s": [0.0], "step_time_s": [0], "capacity_mah": [0.0], "current_ma": [0.0], "voltage_v": [0.0], "dpt_time": [0], "thermocouple_temp_c": [0.0], "ev_temp": [0]})
    df_deleted1 = df_deleted1.astype('object').dtypes
    df_test1 = testdata.delete_cycle_steps(df, [1, 2, 15, 16, 10, 5], decrement=True)
    df_test1 = df_test1.astype('object').dtypes
    assert(df_test1.equals(df_deleted1))
    return

def test_get_index_range_Out():
    df = testdata.import_maccor_data(expath, exfile)
    row_num = testdata.get_index_range(df, [1], cycle_step_idx = [27])
    assert(row_num == 19)
    return

def test_get_cycle_data_Out():
    df = testdata.import_maccor_data(expath, exfile)
    df_27 = pd.DataFrame(data={"cyc": [1], "step": [27], "current_ma": [0.0]})
    df_test = testdata.get_cycle_data(df, ['current_ma'], [1], [27])
    assert(df_test.equals(df_27))
    return

def test_get_num_cycles_Out():
    df = testdata.import_maccor_data(expath, exfile)
    assert(testdata.get_num_cycles(df)==2)
    return
