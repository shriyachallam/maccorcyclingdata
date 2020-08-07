def validation_check_discharging(validation_df, df, discharge_steps):
    if df['step'][i] in discharge_steps:
        if df['current_ma'][i] >= 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is positive during discharging'}, ignore_index=True)
    return validation_df
