import sys
import inspect
from bdb import Bdb


class Debugger(Bdb):

    def __init__(self):
        Bdb.__init__(self)
        self.breakpoints = dict()
        self.set_trace()

    def end(self):
        self.reset()

        # bdb does not seem to actually support clearing, so we do it manually
        sys.settrace(None)

    def install_callback(self, filename=None, lineno=None, method=None, arguments=None):
        if filename is None and lineno is None and method is None:
            return
        # print "Setting breakpoint at " + str((filename, lineno, method, arguments))
        self.set_break(filename, lineno)

        try :
            self.breakpoints[(filename, lineno)].add((method, arguments))
        except KeyError:
            self.breakpoints[(filename, lineno)] = [(method, arguments)]

    def remove_callback(self, filename=None, lineno=None):
        if filename is None and lineno is None:
            return
        del self.breakpoints[(filename, lineno)]

    def user_line(self, frame):
        if not self.break_here(frame):
            return

        (filename, lineno, function, code_context, index) = inspect.getframeinfo(frame)
        filename = filename.split("/")[-1]
        callbacks = self.breakpoints[((filename, lineno))]
        for (callback, arguments) in callbacks:
            callback(frame, arguments)