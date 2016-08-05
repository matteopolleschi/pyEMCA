#!/usr/bin/env python

"""
Tests for the pyEMCA function.
"""

import unittest
from ..pyemca import Dat

class TestEMCA(unittest.TestCase):
    """
    Test.
    """

    def test_basic(self):
        """
        Test a simple, valid example.
        """
        print "ciao"
        self.assertEquals(1, 1)

if __name__ == '__main__':
    unittest.main()