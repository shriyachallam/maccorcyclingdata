def validation_check_rest(validation_df, df, rest_steps):
    if df['step'][i] in rest_steps:
        if df['current_ma'][i] != 0:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - current is not at 0 during rest step'}, ignore_index=True)
    return validation_df
