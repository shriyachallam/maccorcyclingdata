.. _overview:

Code overview
=============

The `preparenovonix`_ package prepares exported data files produced by `Novonix`_ battery-testers by (i) cleaning them and (ii) adding derived information to the file. The package also allows reading an individual column given its name. The derived information includes:

#. A State column with explicit information of the start and end of a
   given type of measurement. Novonix provides a Step number with a
   different value for each type of measurement, for example, 0
   corresponds to an open circuit. However, it is possible to have two
   consecutive measurements of the same type but with different
   experimental conditions, for example charging at different currents.
   These can now be set appart using the State value.

#. A reduced protocol summarising the experimental protocol into having
   each command and corresponding experimental conditions in a single
   line. This is needed to directly relate a measurement with the
   experimental protocol. The reduced protocol is output as a string of
   arrays and it is stored as part of the header when using the
   :ref:`prepare_novonix` function.

#. A Protocol line column with values that assign a measurement to a
   particular line of the reduced protocol.

#. A Loop number column with a counter of the repetitions of a given
   measurement within a loop in the experimental protocol.

Combining the state and step number values makes it possible to select
the capacities from a charge or discharge experimental step. These are
needed for estimating the coulombic efficiency. This combination of
state with step number also allows the computation of resistances based
on current experimental steps or pulses. Specific cycles or individual
sections of the experiment can be selected combining the loop number
with either the state and step number values or the protocol line
values.

The example data provided within the repository for this code is shown
in the figure below :ref:`comparison`. This figure compares the raw
Novonix data with the data after being processed by the
`preparenovonix`_ package. The example raw data contains individual
measurements for which the experimental run time decreases. As it can be
seen in the :ref:`comparison`, these measurements are
removed by the `preparenovonix`_ package. The example raw data file
also includes a failed test. The `preparenovonix`_ package takes the
capacity from the failed test and adds it to the capacities from the
completed experiment. This shifts the result capacity curve by a
constant value, as it can be seen in the :ref:`comparison`. This figure also shows the
increasing loop number when the measurements are within a repeat loop
and the protocol line each measurement corresponds to.

.. _comparison: comparison figure

Plot comparing the raw and processed data
-----------------------------------------

.. figure:: ../example_data/compare_vct.png
   :align: center
   :alt: Data comparison

Comparison of the raw battery testing data (thin dashed lines) and the
data after being processed by the `preparenovonix`_ package (thick
solid lines), as a function of the experimental run time. The top panel
shows the potential and capacity of the battery. The middle panel shows
the step number, which indicates the type of measurement being done. The
bottom panel shows the loop number and protocol line, which are only
available after processing the raw data with the
`preparenovonix`_ package.


.. _preparenovonix: https://github.com/BatLabLancaster/preparenovonix

.. _Novonix: http://www.novonix.ca/

.. _module index: https://prepare-novonix-data.readthedocs.io/en/latest/py-modindex.html