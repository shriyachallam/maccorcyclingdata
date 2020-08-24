def import_multiple_csv_data(file_path):

    df = pd.DataFrame()
    # r=root, d=directories, f = files
    for r, d, files in os.walk(file_path):

        # We only want to parse files that are CSVs
        files = [ file for file in files if file.endswith( ('.CSV') ) ]
        files.sort()

        for file in files:
            print(file)
            temp_df = pd.read_csv(file_path+file) # Read data from .csv file
            df = df_output.append(temp_df, ignore_index = True)
    
    df = clean_maccor_df(df)

    return df