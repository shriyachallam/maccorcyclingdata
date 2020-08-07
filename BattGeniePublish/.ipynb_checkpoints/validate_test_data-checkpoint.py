def validate_test_data(schedule_df , df, cell_id):
    column_names = ["time", "run", "cell_num", "row_number", "error"]
    validation_df = pd.DataFrame(columns = column_names)
    rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step = sort_scheduler_steps(schedule_df)
    for i in df.index: 
        validation_df = validation_check_rest(validation_df, df, rest_steps)
        validation_df = validation_check_charging(validation_df, df, charge_steps)
        validation_df = validation_check_discharging(validation_df, df, discharge_steps)
        validation_df = validation_check_advanced_cycle(validation_df, df, advance_steps)
        validation_df = validation_check_max_step_num(validation_df, df, max_step)
        
        if i != 0:
            if df['test_time_s'][i] >= (df['test_time_s'][i-1] + 40):
                validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'anomaly - more than 40 seconds has passed since the last collected data'}, ignore_index=True)
            if (df['thermocouple_temp_c'][i] >= (df['thermocouple_temp_c'][i-1] + 5)) or (df['thermocouple_temp_c'][i] <= (df['thermocouple_temp_c'][i-1] - 5)):
                validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'anomaly - jump in temperature (more than 5 degrees)'}, ignore_index=True)
        if df['thermocouple_temp_c'][i] >= 30:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'warning - the temperature has exceeded 30 degrees'}, ignore_index=True)
    if validation_df.empty:
        validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'run complete', 'cell_num': cell_id, 'row_number': '-', 'error': 'there are no errors'}, ignore_index=True)
        return validation_df
    validation_df = validation_df.append({'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'run complete', 'cell_num': cell_id, 'row_number': '-', 'error': 'errors listed above'}, ignore_index=True)
    return validation_df
