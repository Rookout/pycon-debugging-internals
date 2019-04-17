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

from pass_debugger import pass_tracer
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
        print ("Testing without tracer")
        print ("Empty method time was: " + str(self.measure(self.empty_method)))
        print ("Pass method time was: " + str(self.measure(self.simple_method)))

        sys.settrace(pass_tracer)

        print ("Testing with tracer in different file")
        print ("Empty method time was: " + str(self.measure(different_file_empty_method)))
        print ("Pass method time was: " + str(self.measure(different_file_simple_method)))

        sys.settrace(None)
        sys.settrace(pass_tracer)

        print ("Testing with tracer in same file")
        print ("Empty method time was: " + str(self.measure(self.empty_method)))
        print ("Pass method time was: " + str(self.measure(self.simple_method)))



if '__main__' == __name__:
    TestBdbLocationServicesPerformance().test_performance()