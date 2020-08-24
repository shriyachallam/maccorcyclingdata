.. _overview:

Code overview
=============

The `maccorcyclingdata`_ package prepares exported data files produced by `Maccor`_ battery cyclers by:

#. Importing and Cleaning Data: Within the  `maccorcyclingdata`_ package, there are functions to import testdata from the cyclers. The cleaning process includes renaming, dropping, or changing the units of certain columns. 

#. Import the Schedule File: With the `maccorcyclingdata`_ package, there is a function that imports and cleans the schedule file that is input into the `Maccor`_ cycler. This allows the schedule file to be interpreted as a usable pandas dataframe.

#. Validating the Testdata against the Schedule file: With the `maccorcyclingdata`_ package, the testdata can be validated against the schedule file to ensure the cycler followed the correct cycling system. 

.. _maccorcyclingdata: https://github.com/shriyachallam/maccorcyclingdata

.. _Maccor: http://www.maccor.com/
