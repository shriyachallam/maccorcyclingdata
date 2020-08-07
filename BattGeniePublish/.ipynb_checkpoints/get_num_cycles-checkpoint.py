''' A simple function that just returns the nuber of cycles. I just use it a lot'''
def get_num_cycles(df):
    number_of_cycles = int(max(df['Cyc#']))
    return number_of_cycles 