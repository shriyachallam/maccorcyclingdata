import pandas as pd
import numpy as np

def get_num_cycles(df):
	'''
    Given the testdata dataframe, this function will return the number of cycles.
	
	Parameters
	----------
	df: the testdata dataframe

	Outputs
	-------
	number_of_cycles: an integer of the number of cycles in the dataframe
	
	'''

    number_of_cycles = int(max(df['Cyc#']))
    return number_of_cycles 