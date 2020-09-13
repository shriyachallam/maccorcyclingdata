import unittest
import maccorcyclingdata.testdata as testdata
import os

expath = "example_data/"
exmult = "example_data/multiple_csv/"
exfile = "testdata.csv"


def test_data_is_csv():
    assert((expath + exfile).endswith(".csv"))

def test_columns_check():
    df = testdata.import_maccor_data(expath , exfile, header=0)
    columns = list(df.columns)
    correct_columns = ['cyc', 'step', 'test_time_s', 'step_time_s', 'capacity_mah', 'current_ma', 'voltage_v', 'dpt_time', 'thermocouple_temp_c', 'ev_temp']
    assert(columns == correct_columns)
