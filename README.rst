|docs| |pypi|

.. inclusion-marker-do-not-remove

Preparing MACCOR Data
======================

The **maccorcyclingdata** package is to be used on the raw data output from the `MACCOR`_ battery cyclers and the schedule file input into the `MACCOR`_ battery cyclers. The package can also be used to validate the testdata by comparing it against the schedules.

Example
-------

The **example.ipynb** provides examples where all the functions are used on the given example data. 
To run this example, simply open and run each cell in the example Jupyter Notebok provided.

Requirements and Installation
-----------------------------

This code has been developed in Python 3.7.6 and it is compatible with Python above 3.5 versions. The code has been tested to run in Windows, OSX and Linux operating systems. 

This code uses numpy and pandas as specified in docs/requirements.txt.

The code can be run directly from a cloned GitHub `repository`_ or it can also be installed as a python `package`_ through pip:

.. code::

   pip install maccorcyclingdata

The functions in the package can be used after importing testdata, schedules, validate for example as follows:

.. code-block:: python

   import maccorcyclingdata.testdata as testdata
   import maccorcyclingdata.schedules as schedules
   import maccorcyclingdata.validate as testdata

.. _compability:

Compatibility
-------------

If you encounter issues running the code for
any version of Novonix software report an issue. Note that an example
file will be needed in order to improve the code.

The raw testdata and schedule file that this package is used on shoudl be csv files.
Please export your raw testdata from the `MACCOR`_ battery cyclers with columns named and ordered as the following:

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


.. _MACCOR: http://www.maccor.com/

.. _package: https://pypi.org/project/maccorcyclingdata/

.. _repository: https://github.com/shriyachallam/maccorcyclingdata

.. |docs| image:: https://readthedocs.org/projects/maccorcyclingdata/badge/?version=latest
    :target: https://maccorcyclingdata.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi| image:: https://img.shields.io/pypi/v/preparenovonix.svg
    :target: https://pypi.org/project/maccorcyclingdata/
