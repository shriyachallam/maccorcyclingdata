'''
This function takes in a data frame and list of integers as arguments. It deletes all rows from the data frame that have a cycle step index that matches any in the list of integers and returns the data frame with the rows deleted. 
The function has an optional argument (default false) which, if set to True, would decrement all cycle steps ahead any steps that are deleted.

'''
def delete_cycle_steps(df, steps_to_delete, decrement=False):
    
    for x in steps_to_delete:
        to_be_deleted = df.index[df['step'] == x]
    
        if decrement:
            to_be_shifted = df.index[df['step'] > x]
            all_values_larger = ((df['step'][to_be_shifted]) - 1)
            df['step'][to_be_shifted] = all_values_larger
            
    df = df.drop(to_be_deleted)  

    df = df.reset_index(drop = True)           
    return df