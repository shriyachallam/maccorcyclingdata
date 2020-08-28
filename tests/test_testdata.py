from unittest import TestCase
import maccorcyclingdata.testdata as testdata
import os

expath = "example_data/"
exmult = "example_data/multiple_csv"
exfile = "testdata.csv"

class test_column():
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))
