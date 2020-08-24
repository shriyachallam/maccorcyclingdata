def import_maccor_data(file_path , file_name):
	
	df = pd.read_csv(file_path+file_name,sep='\t', header = 2)  # Read data from .txt is the line the data starts on

	df = clean_maccor_df(df)
    
	return df