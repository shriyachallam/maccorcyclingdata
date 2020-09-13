import unittest
import maccorcyclingdata.schedules as schedules
import os

expath = "example_data/"
exfile = "schedule.csv"

def test_schedules_columns():
    df = schedules.import_schedules(expath , exfile)
    columns = list(df.columns)
    correct_columns = ['step', 'step_type', 'step_mode', 'step_mode_value', 'step_limit', 'step_limit_value', 'step_end_type', 'step_end_type_op', 'step_end_type_value', 'goto_step', 'report_type', 'report_type_value', 'options', 'step_note']
    assert(columns == correct_columns)

#def test_scheduler_steps_order(self):
#    df = schedules.import_schedules(expath , exfile)