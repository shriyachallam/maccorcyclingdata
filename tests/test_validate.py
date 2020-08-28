from unittest import TestCase
import maccorcyclingdata.schedules as schedules
import maccorcyclingdata.testdata as testdata
import os

class TestJoke(TestCase):
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))
