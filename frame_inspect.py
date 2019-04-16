import inspect

def no_vars():
  print "local vars:", inspect.currentframe().f_locals


def has_vars():
  mystr = "mystr"
  mydict = {"mykey": "myvalue"}
  mylist = [1, 2, 3]
  print "local vars:", inspect.currentframe().f_locals


def frameinfo():
  frame = inspect.currentframe()
  print "frame info:", inspect.getframeinfo(frame)


print "no vars"
no_vars()

print "has vars"
has_vars()

print "frameinfo"
frameinfo()