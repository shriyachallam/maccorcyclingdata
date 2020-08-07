def import_schedules(file_path, file_name):
	df = pd.read_excel(file_path + file_name) #create a df from the xlxs
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
	    while pd.isnull(df['step'][x + 1]): #each time the line after the first line of the multi-line group has a null value at the step it is appended to the arrays with respect to the column, once the next line returns a not null value at the step column, it means it has moved on to the next step
	        end_type.append(df['step_end_type'][x + 1])
	        op.append(df['step_end_type_op'][x + 1])
	        value.append(df['step_end_type_value'][x + 1])
	        goto.append(df['goto_step'][x + 1])
	        df = df.drop([df.index[1 + x]]) #delete the row whose values were just appended to the arrays
	        df = df.reset_index(drop=True) #by resetting the index the while loop is activated again
	    df_update = pd.DataFrame({'step_end_type': [end_type], 'step_end_type_op': [op], 'step_end_type_value': [value], 'goto_step': [goto]}, index=[x])
	    df.update(df_update) #add the arrays into their respective places in the original df
	    
	#set the type of the step and step_limit_value columns to int and float, the rest of the columns have the type as object, even if you force the type as a str, they remain as type object
	df = df.astype({'step': int, 'step_limit_value': float})
	#this sets the nan values in columns step and step_limit_value to 0
	#df[['step','step_limit_value']] = df[['step','step_limit_value']].fillna(0)
	#this sets the nan values in the remaining columns to blank strings
	#df[['step_type', 'step_mode', 'step_mode_value', 'step_limit', 'step_end_type', 'step_end_type_op', 'step_end_type_value', 'goto_step', 'report_type', 'report_type_value', 'options', 'step_note']] = df[['step_type', 'step_mode', 'step_mode_value', 'step_limit', 'step_end_type', 'step_end_type_op', 'step_end_type_value', 'goto_step', 'report_type', 'report_type_value', 'options', 'step_note']].fillna('')   
	return df
