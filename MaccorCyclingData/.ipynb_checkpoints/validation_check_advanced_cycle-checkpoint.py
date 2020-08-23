def validation_check_advanced_cycle(validation_df, df, advance_steps):
    if df['step'][i] in advance_steps:
        if df['cyc'][i] != (df['cyc'][i-1] + 1):
            validation_df = validation_df.append({'time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'run': 'in progress', 'cell_num': cell_id, 'row_number': i, 'error': 'error - the cycle did not advance properly'}, ignore_index=True)
    return validation_df
