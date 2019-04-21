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

    def set_breakpoint(self, filename=None, lineno=None, method=None):
        if filename is None and lineno is None and method is None:
            return
        self.set_break(filename, lineno)

        self.breakpoints.get((filename, lineno), {})

        try :
            self.breakpoints[(filename, lineno)].add(method)
        except KeyError:
            self.breakpoints[(filename, lineno)] = [method]

    def unset_breakpoint(self, filename=None, lineno=None):
        if filename is None and lineno is None:
            return
        del self.breakpoints[(filename, lineno)]

    def user_line(self, frame):
        if not self.break_here(frame):
            return

        (filename, lineno, function, code_context, index) = inspect.getframeinfo(frame)
        filename = filename.split("/")[-1]
        callbacks = self.breakpoints[((filename, lineno))]
        for callback in callbacks:
            callback(frame)