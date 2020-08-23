.. _overview:

Code overview
=============

The `maccorcyclingdata`_ package prepares exported data files produced by `Maccor`_ battery cyclers by:

#. Importing and Cleaning Data: Within the  `maccorcyclingdata`_ package, there are functions to import testdata from the cyclers. The cleaning process includes renaming, dropping, or changing the units of certain columns. 

#. Import the Schedule File: With the `maccorcyclingdata`_ package, there is a function that imports and cleans the schedule file that is input into the `Maccor`_ cycler. This allows the schedule file to be interpreted as a usable pandas dataframe.

#. Validating the Testdata against the Schedule file: With the `maccorcyclingdata`_ package, the testdata can be validated against the schedule file to ensure the cycler followed the correct cycling system. 

BattGenie
----------------------------------------

The `maccorcyclingdata`_ package was created at `BattGenie Inc`_. 
`BattGenie`_ is a startup that provides efficient battery management solutions for Lithium-ion batteries for electric vehicles, consumer electronics and grid storage applications. 
Our patented technology uses physics-based battery models that are fast and more accurate compared to traditional empirical models.


.. _maccorcyclingdata: https://github.com/shriyachallam/MaccorCyclingData

.. _Maccor: http://www.maccor.com/

.. _BattGenie Inc: https://www.battgenie.life/

.. _BattGenie: https://www.battgenie.life/

.. _M.A.P.L.E. Lab: http://depts.washington.edu/maple/