# Rookout/Rookout@4754620e

import sys
import inspect
from bdb import Bdb

class Debugger(Bdb):
    def __init__(self):
        Bdb.__init__(self)
        self.breakpoints = dict()
        self.set_trace()

def install_callback(self, filename, lineno, method, arguments):
    # Setting breakpoint at (filename, lineno)
    self.set_break(filename, lineno)
    # Keep the callback/args of the breakpoint
    self.breakpoints[(filename, lineno)].add((method, arguments))

def user_line(self, frame):
    if not self.break_here(frame):
        return
    # Get filename and lineno from frame (in order to fetch our saved callback)
    (filename, lineno, _, _, _) = inspect.getframeinfo(frame)

    callbacks = self.breakpoints[((filename, lineno))]
    # Each callback is a different breakpoint on this line
    for (callback, arguments) in callbacks:
        callback(frame, arguments)