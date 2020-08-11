.. _features:
Code Features
=============

The main functions available in the `battgeniepublish`_ package are
listed below in alphabetical order. The list contains the module name
followed by the function name with the expected input parameters in
brackets.

-  ``testdata.clean_maccor_df(df)``: Given the testdata dataframe, this function will rename the headers and drop unnecessary columns.

-  ``testdata.delete_cycle_steps(df, steps_to_delete, decrement=False)``: Given the testdata dataframe and a list of integers (step numbers that you want to delete), this function
    will delete all rows from the dataframe that have a cycle step index that matches any in the list of integers.

-  ``testdata.get_cycle_data(df, Headings, cyc_range)``: This function gets the data specified in the "Headings" for each sample within the specified cyc_range.

-  ``testdata.get_index_range(df, cyc_range, cycle_step_idx)``: Given the testdata dataframe, this function returns the index range for the specified cycle range, 
    or if a cycle step index is passed, as subset of each cyle for only that specific cycle step.

-  ``testdata.get_num_cycles(df)``: Given the testdata dataframe, this function will return the number of cycles.

-  ``testdata.import_maccor_data(file_path, file_name)``: Given the file_path and file name of the testdata .csv file, this function will import the csv datafile as a df
	and clean it.

-  ``testdata.import_multiple_csv_data(file_path)``: Given the file path that holds multiple csv files (testdata files), this function will import and append 
    all of the csv files to one another as one dataframe. Returns a cleaned version of that dataframe.

-  ``schedules.import_schedules(file_path, file_name)``: Given the file path and file name (of the schedule file that is inputted into the Maccor Cycler), this 
	function will import and clean the schedule file and return it as a df.

-  ``schedules.sort_scheduler_steps(schedule_df)``: Given the schedule_df (the df of the schedule file), this function will sort rest, charge, discharge, advance
    cycle, and end step numbers.

-  ``validate.validation_check_advanced_cycle(validation_df, df, advance_steps)``: This function will validate the testdata against the advance cycle steps by making sure the cycle advances.

-  ``validate.validation_check_charging(validation_df, df, charge_steps)``: This function will validate the testdata against the charging steps by making sure the current is positive.

-  ``validate.validation_check_discharging(validation_df, df, discharge_steps)``: This function will validate the testdata against the discharging steps by making sure the current is negative.

-  ``validate.validation_check_max_step_num(validation_df, df, max_step)``: This function will validate the testdata against the max step by making sure no steps surpass the max.

-  ``validate.validation_check_max_temp(validation_df, df, max_temp, temp_tol=3)``: This function will validate the testdata against the max temperature by making sure no steps surpass the max.

-  ``validate.validation_check_time_interval(validation_df, df, temp_interval)``: This function will validate the testdata to make sure the temperature does not fluctuate suddenly.

-  ``validate.validation_check_rest(validation_df, df, rest_steps)``: This function will validate the testdata against the rest steps by making sure the current is at 0 when resting.

-  ``validate.validation_test_data(schedule_df, df, cell_id, time_interval, temp_interval, max_temp)``: This is a wrapper function that validates the testdata against the schedule file.
    The sub-functions that are validated are: 
    validation_check_rest, validation_check_charging, validation_check_discharging, validation_check_advanced_cycle, 
    validation_check_max_step_num, validation_check_max_temp, validation_check_time_interval, validation_check_temp_interval

In what follows, the above functions will be referred by simply their
name, without stating the modules they belong to.

The ``clean_maccor_df`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``delete_cycle_steps`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``get_cycle_data`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``get_index_range`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``get_num_cycles`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``import_maccor_data`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``import_multiple_csv_data`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``import_schedules`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``sort_scheduler_steps`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_advanced_cycle`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_charging`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_discharging`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_max_step_num`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_max_temp`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_time_interval`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_check_rest`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

The ``validation_test_data`` function
---------------------------------
The ``reduced_protocol`` function reads the complete header from the input file and generates (or reads)
the reduced protocol. This function returns the reduce protocol itself
and a boolean flag, ``viable_prot``. The reduced protocol consist of an
array of strings. Each string contains a line number, a command from the
experimental protocol and the corresponding experimental conditions (if
aplicable); for example: ``[4 : Repeat 49 times :]``. Only commands
referring to the following processes will appear in the reduced
protocol (note that the commands corresponding to incrementing the cycle counter and global emergency limits are ignored in the reduced protocol as there are no measurements associated with those):

-  Open circuit storage (or rest)

-  Constant current (dis)charge

-  Constant current - Constant Voltage (dis)charge

-  (End) Repeat

The reduced protocol is tested against the number of unique measurements
in the file, determined using the column State. If the number of
measurements expected from the protocol is less than the actual number
of measurements, the flag ``viable_prot`` is set to ``False``,
indicating that the construction of the reduced protocol was not viable.

.. _battgeniepublish: https://github.com/shriyachallam/BattGeniePublish