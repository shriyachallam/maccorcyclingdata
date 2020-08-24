def sort_scheduler_steps(schedule_df):
    rest_steps = []
    charge_steps = []
    advance_steps = []
    discharge_steps = []
    end_steps = []
    for i in schedule_df.index:
        if schedule_df['step_type'][i] == "Rest":
            rest_steps.append(i+1)
        if schedule_df['step_type'][i] == "Charge":
            charge_steps.append(i+1)
        if schedule_df['step_type'][i] == "Discharge":
            discharge_steps.append(i+1)
        if schedule_df['step_type'][i] == "Advance Cycle":
            advance_steps.append(i+1)
        if schedule_df['step_type'][i] == "End":
            end_steps.append(i+1)        
        max_step = schedule_df["step"].iloc[-1]
    return rest_steps, charge_steps, advance_steps, discharge_steps, end_steps, max_step
