import inspect

def a():
  print 'in a()'
  mystr = "mystr"
  frame = inspect.currentframe()
  print "local vars:", frame.f_locals
  mydict = {"mykey": "myvalue"}
  mylist = [1, 2, 3]
  frame = inspect.currentframe()
  print "local vars:", frame.f_locals
  print "frame info:", inspect.getframeinfo(frame)
  return mystr * 2

a()