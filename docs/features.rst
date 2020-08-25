.. _features:
Code Features
=============

The main functions available in the `maccorcyclingdata`_ package are
listed below in alphabetical order. The list contains the module name
followed by the function name with the expected input parameters in
brackets.

-  ``testdata.delete_cycle_steps(df, steps_to_delete, decrement=False)``: Given the testdata dataframe and a list of integers (step numbers that you want to delete), this function will delete all rows from the dataframe that have a cycle step index that matches any in the list of integers.

-  ``testdata.get_cycle_data(df, Headings, cyc_range, cycle_step_idx=0)``: This function gets the data from the specified column for each sample within the specified cyc_range.

-  ``testdata.get_num_cycles(df)``: Given the testdata dataframe, this function will return the number of cycles.

-  ``testdata.import_maccor_data(file_path, file_name, header=0)``: Given the file_path and file name of the testdata .csv file, this function will import the csv datafile as a df and clean it.

-  ``testdata.import_multiple_csv_data(file_path)``: Given the file path that holds multiple csv files (testdata files), this function will import and append all of the csv files to one another as one dataframe. Returns a cleaned version of that dataframe.

-  ``schedules.import_schedules(file_path, file_name)``: Given the file path and file name (of the schedule file that is inputted into the Maccor Cycler), this function will import and clean the schedule file and return it as a df.

-  ``validate.validate_test_data(schedule_df, df, cell_id, time_interval, temp_interval, max_temp)``: This is a function that validates the testdata against the schedule file.
    
In what follows, the above functions will be referred by simply their name, without stating the modules they belong to.

.. _chart:

Flow chart
----------
.. figure:: flowchart.png
   :align: center
   :alt: Flow chart

Flow chart for the `maccorcyclingdata`_ package with all the functionality of
all the functions presented here. In this chart rounder rectangles indicate the start 
and end of processes, rectangles indicate questions to determine the next step, and 
parallelograms indicate functions. 
Note that for simplicity not all the decisions made in the code are shown here.

The ``delete_cycle_steps`` function
------------------------------------------
The ``delete_cycle_steps`` function reads an array of the step numbers that should be deleted, ``steps_to_delete``, and deletes all rows that occur during those steps from the inputted testdata dataframe.
This function returns the testdata dataframe itself with the steps deleted. If the boolean ``decrement`` is set to True, the function will renumber the steps at the end. The ``decrement`` boolean is optional. The default value if False.

The ``get_num_cycles`` function
--------------------------------------
The ``get_num_cycles`` function finds the number of cycles given the testdata dataframe, ``df``. 
The function returns an integer of the number of cycles in the dataframe. This function assumes that the first cycle is cycle 0.

The ``get_cycle_data`` function
-------------------------------------
The ``get_cycle_data`` function gets the data from the array of specified columns, ``Headings``, for each sample within the array of the cycle numbers that are of interest, ``cyc_range``.
It can also get the data for specific steps within each cycle if the ``cycle_step_idx`` parameter is input.
This function returns a pandas dataframe that has the data for the specified headers at the specified cycles and steps.

The ``import_maccor_data`` function
--------------------------------------
The ``import_maccor_data`` function creates a pandas dataframe given a string of the file path, ``file_path``, and a string of the file name, ``file_name``, of a testdata dataframe. 
The function will import and clean the testdata by renaming the headers and dropping unnecessary columns. 
The columns must be named properly to be renamed to the following:

- From 'Cyc#' to 'cyc'

- From 'Step' to 'step'

- From 'TestTime(s)' to 'test_time_s'

- From 'StepTime(s)' to 'step_time_s'

- From 'Capacity(Ah)' to 'capacity_mah'

- From 'Current(A)' to 'current_ma'

- From 'Voltage(V)' to 'voltage_mv'

- From 'DPt Time' to 'dpt_time'

- From 'Temp 1' to 'thermocouple_temp_c'}

- From 'EV Temp' to 'ev_temp'

If the following columns exist, the function will delete these columns: ``ACR``, ``DCIR``, ``Watt-hr``, and ``nnnamed``.
As of 5/05/2020, Maccor mislabels the Voltage column so this function also changes the units of Voltage.

The optional input- an integer that specifies which line is the header, ``header``- will set the header to be that line number. The default value of ``header`` is 0.

The function returns a pandas dataframe of the cleaned testdata.

The ``import_multiple_csv_data`` function
--------------------------------------------
The ``import_multiple_csv_data`` function creates a pandas dataframe given a string of the file path, ``file_path``, of a directory that contains multiple csv files of testdata. 
The function will import all files within the directory that end in .csv. Additionally, this function will append the csv files to one another depending on the order they appear in the directory.
This function will clean the data similar to the ``import_maccor_data`` function. The function will import and clean the testdata by renaming the headers and dropping unnecessary columns. 
The columns must be named properly to be renamed to the following:

- From 'Cyc#' to 'cyc'

- From 'Step' to 'step'

- From 'TestTime(s)' to 'test_time_s'

- From 'StepTime(s)' to 'step_time_s'

- From 'Capacity(Ah)' to 'capacity_mah'

- From 'Current(A)' to 'current_ma'

- From 'Voltage(V)' to 'voltage_mv'

- From 'DPt Time' to 'dpt_time'

- From 'Temp 1' to 'thermocouple_temp_c'}

- From 'EV Temp' to 'ev_temp'

If the following columns exist, the function will delete these columns: ``ACR``, ``DCIR``, ``Watt-hr``, and ``nnnamed``.
As of 5/05/2020, Maccor mislabels the Voltage column so this function also changes the units of Voltage.

The function returns a pandas dataframe with the cleaned testdata appended to one another.

The ``import_schedules`` function
--------------------------------------
The ``import_schedules`` function creates a pandas dataframe given a string of the file path, ``file_path``, and a string of the file name, ``file_name``, of the schedule file (csv file) that is inputted into the Maccor Cycler. 
The function will rename the columns to the following (in this order): 'step', 'step_type', 'step_mode', 'step_mode_value', 'step_limit', 'step_limit_value', 'step_end_type', 'step_end_type_op', 'step_end_type_value', 'goto_step', 'report_type', 'report_type_value', 'options', 'step_note'.

For all multiline steps (for example: steps with multiple options for the step it should go to depending on the result), this function will append those multiple lines into an array with each element being the value of each line. This allows for the function to keep each step to one line. 
This function sets the datatype of the ``step`` and ``step_limit_value`` to integer and float respectively.

The function returns a pandas dataframe of the cleaned scheduler.

The ``validate_test_data`` function
-------------------------------------------
The ``validate_test_data`` function validates the testdata against the scheduler.

Parameters of this function (in this order):

- schedule_df = the dataframe of the cleaned schedule file (from the ``import_schedules`` function)

- df = testdata dataframe (from the ``import_maccor_data`` or ``import_multiple_csv_data`` functions)

- cell_id = the cell id of the testdata (integer)

- time_interval = the maximum interval of how often the cycler should be recording data in seconds (integer)

- temp_interval = the maximum interval of a temperature change in number of degrees (integer)

- max_temp = the threshold for the highest temperature allowed (integer)

- tol = when making sure the temperature doesn't exceed a certain amount, this function will return either a warning, error, or ABORT message. this input specifies the tolerance should these messages. This is an optional input, the default value is 3.

The erros this function checks for:

- if during all the rest steps, the battery is actually resting

- if during all charging steps, the battery is charging

- if during all discharging steps, the battery is discharging

- if during all advance cycle steps, the cycle is being advanced

- if the step number never exceeds the max step number

- data is collected for every ``time_interval`` given 

- the temperate never jumps or drops by an interval greater than the ``temp_interval``

- the temperature never goes past the max temperature

For the max temperature error, there are 3 possibilities of error messages:

1. warning - temperature approaching the max! (current temperature + tol > max)

2. error - temperature has surpassed the max! (current temperature >= max)

3. ABORT - temperature is way too hot! (current temperature > max + tol)
 
The function returns a pandas dataframe that lists all errors, ``validation_df``.
Headers of the ``validation_df``:

1. time (the current time of when the validation occurs)

2. run (tells whether the validation function is in progress or complete)

3. cell_num (the cell number of the testdata)

4. row_number (the row number where the error occurs)

5. error (what the error is)

If the testdata does not have any errors, this function will return the ``validation_df`` that says "there are no errors."

.. _maccorcyclingdata: https://github.com/shriyachallam/maccorcyclingdata