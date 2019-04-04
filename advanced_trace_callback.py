import sys

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print 'Executing line %s in func %s' % (line_no, func_name)

def trace_exceptions(frame, event, arg):
    if event != 'exception':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    exc_type, exc_value, exc_traceback = arg
    print 'Tracing exception: %s "%s" on line %s of %s' % \
        (exc_type.__name__, exc_value, line_no, func_name)

def tracer(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
    elif event == 'line':
        trace_lines(frame, event, arg)
    elif event == 'return':
        print '%s => %s' % (func_name, arg)
    elif event == 'exception':
        trace_exceptions(frame, event ,arg)
    return tracer

def c():
    raise RuntimeError('generating exception in c()')

def b():
    print 'in b()'
    c()
    return 'response_from_b'

def a():
    print 'in a()'
    val = b()
    return val * 2

sys.settrace(tracer)
try:
    a()
except Exception, e:
    print 'Exception handler:', e
