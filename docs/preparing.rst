.. _peparing:

Before using this package:
================================

The `maccorcyclingdata`_ package is to be used on raw data output from the `Maccor`_ Battery Cyclers. 
Before using this package, please ensure that your data exports as a csv file with the following columns (the order of columns should also follow this template):
#. 'Cyc#'

#. 'Step'

#. 'TestTime(s)'

#. 'StepTime(s)'

#. 'Capacity(Ah)'

#. 'Watt-hr'

#. 'Current(A)'

#. 'Voltage(V)'

#. 'DPt Time'

#. 'ACR'

#. 'DCIR'

#. 'Temp 1'

#. 'EV Temp'

#. 'Unnamed: 13'

Additionally, the schedule file should be exported as a csv file with the following columns (the order of columns should also follow this template):

#. 'step'

#. 'step_type'

#. 'step_mode'

#. 'step_mode_value'

#. 'step_limit'

#. 'step_limit_value'

#. 'step_end_type'

#. 'step_end_type_op'

#. 'step_end_type_value'

#. 'goto_step', 'report_type'

#. 'report_type_value'

#. 'options'

#. 'step_note'


Examples
-----------------------------------------

We have provided a Jupyter Notebook using all functions from the `maccorcyclingdata`_ package. 
Click `here`_ to view the example notebook. 


.. _maccorcyclingdata: https://github.com/shriyachallam/MaccorCyclingData

.. _Maccor: http://www.maccor.com/

.. _BattGenie: https://www.battgenie.life/

.. _here: https://github.com/shriyachallam/MaccorCyclingData/tree/master/examples