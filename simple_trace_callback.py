import sys

def simple_tracer(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print("Event: {} | Function Name: {} | Line: {} | Filename: {}"
          .format(event, func_name, line_no, filename))
    return simple_tracer


def a():
    print 'in a()'
    val = b()
    return val * 2

    
def b():
    print 'in b()'
    return 'response_from_b' 


if __name__ == '__main__':
    sys.settrace(simple_tracer)
    a()