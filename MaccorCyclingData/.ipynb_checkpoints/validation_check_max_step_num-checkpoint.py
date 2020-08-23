def validation_check_max_step_num(validation_df, df, max_step):
    if df['step'][i] > max_step:
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - this step number surpasses the steps in scheduler'}, ignore_index=True)
    return validation_df
