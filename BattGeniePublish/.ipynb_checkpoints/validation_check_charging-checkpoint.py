def validation_check_charging(validation_df, df, charge_steps):
    if df['step'][i] in charge_steps:
        if df['current_ma'][i] <= 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is negative during charging'}, ignore_index=True)
    return validation_df
