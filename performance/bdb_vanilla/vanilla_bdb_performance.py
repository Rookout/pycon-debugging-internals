"""
This file can be used to benchmark and profile BdbLocationService
"""

import six
import inspect
import time
import sys
import os


def break_points_here():
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1
    a = 1


# Add rook base to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from vanilla_bdb_debugger import Debugger
from different_file import empty_method as different_file_empty_method, simple_method as different_file_simple_method

class TestBdbLocationServicesPerformance(object):

    @staticmethod
    def empty_method():
        pass

    @staticmethod
    def simple_method():
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8
        i = 9
        j = 10

    @staticmethod
    def measure(method, *args, **kwargs):
        stop = 2 ** 24
        if six.PY2:
            iterator = xrange(stop)
        else:
            iterator = range(stop)

        start = time.time()
        for i in iterator:
            method(*args, **kwargs)
        end = time.time()

        return (end - start) / stop * 1000 * 1000

    def test_performance(self):
        print ("Testing without engine")
        print ("Empty method time was: " + str(self.measure(self.empty_method)))
        print ("Pass method time was: " + str(self.measure(self.simple_method)))

        debugger = Debugger()

        print ("Testing with engine but no hooks")
        print ("Empty method time was: " + str(self.measure(self.empty_method)))
        print ("Pass method time was: " + str(self.measure(self.simple_method)))

        print ("Testing with engine and hook in different file")
        debugger.install_callback('different_file.py', 2, debugging_callback)
        print ("Empty method time was: " + str(self.measure(different_file_empty_method)))
        debugger.remove_callback('different_file.py', 2)

        debugger.install_callback('different_file.py', 5, debugging_callback)
        print ("Pass method time was: " + str(self.measure(different_file_simple_method)))
        debugger.remove_callback('different_file.py', 5)

        print ("Testing with engine and hook in same file")
        debugger.install_callback('bdb_performance.py', 39, debugging_callback)
        print ("Empty method time was: " + str(self.measure(self.empty_method)))
        debugger.remove_callback('bdb_performance.py', 39)

        debugger.install_callback('bdb_performance.py', 43, debugging_callback)
        print ("Pass method time was: " + str(self.measure(self.simple_method)))
        debugger.remove_callback('bdb_performance.py', 43)


def debugging_callback(frame, arguments):
    return debugging_callback


if '__main__' == __name__:
    TestBdbLocationServicesPerformance().test_performance()