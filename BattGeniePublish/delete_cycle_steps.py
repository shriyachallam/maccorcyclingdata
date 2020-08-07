import pandas as pd
import numpy as np

def delete_cycle_steps(df, steps_to_delete, decrement=False):
	'''
    Given the testdata dataframe and a list of integers (step numbers that you want to delete), this function
    will delete all rows from the dataframe that have a cycle step index that matches any in the list of integers 
    
    The function has an optional argument (default false) which, if set to True, would decrement all cycle steps 
    ahead any steps that are deleted. 
	
	Parameters
	----------
    df: the dataframe that you want to delete steps from
    steps_to_delete: an array that has the step numbers you want to delete
    decrement: optional boolean, if true will shift step numbers to compensate for the deleted steps

    Outputs
    -------
    df: the dataframe with the corresponding steps deleted
    
	Notes
	-----
	the decrement parameter is optional. The default value if False.

	'''
    for x in steps_to_delete:
        to_be_deleted = df.index[df['step'] == x]
    
        if decrement:
            to_be_shifted = df.index[df['step'] > x]
            all_values_larger = ((df['step'][to_be_shifted]) - 1)
            df['step'][to_be_shifted] = all_values_larger
            
    df = df.drop(to_be_deleted)  

    df = df.reset_index(drop = True)           
    return df