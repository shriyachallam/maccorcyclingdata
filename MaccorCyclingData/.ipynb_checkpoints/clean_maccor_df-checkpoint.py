def clean_maccor_df(df):
	df['Watt-hr'] = pd.to_numeric(df['Watt-hr'], errors='coerce')

	# Rename various columns to use
	df.rename(columns={'Cyc#':'cyc'}, inplace=True)
	df.rename(columns={'Step':'step'}, inplace=True)
	df.rename(columns={'TestTime(s)':'test_time_s'}, inplace=True)
	df.rename(columns={'StepTime(s)':'step_time_s'}, inplace=True)
	df.rename(columns={'Capacity(Ah)':'capacity_mah'}, inplace=True)
	df.rename(columns={'Watt-hr':'energy_wh'}, inplace=True)
	df.rename(columns={'Current(A)':'current_ma'}, inplace=True)
	df.rename(columns={'Voltage(V)':'voltage_mv'}, inplace=True)
	df.rename(columns={'DPt Time':'dpt_time'}, inplace=True)
	df.rename(columns={'ACR':'acr'}, inplace=True)
	df.rename(columns={'DCIR':'dcir'}, inplace=True)
	df.rename(columns={'Temp 1':'thermocouple_temp_c'}, inplace=True)
	df.rename(columns={'EV Temp':'ev_temp'}, inplace=True)
	df.rename(columns={'Unnamed: 13':'nnnamed'}, inplace=True)
    
	# drop the ones we dont want
	df = df.drop(columns=['acr', 'dcir', 'nnnamed']) 
    
	# Change the units on everything
	# Note we don't need to convert capacity because it's already mah. Maccor just mislabels it (as of 5/05/2020)
	df.voltage_mv = df.voltage_mv * 1e3
    
	return df