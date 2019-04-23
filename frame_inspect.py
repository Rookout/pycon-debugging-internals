import inspect

def test_no_vars():
  print(inspect.currentframe().f_locals)


def test_vars():
  mystr = "mystr"
  mydict = {"mykey": "myvalue"}
  mylist = [1, 2, 3]
  print(inspect.currentframe().f_locals)


def test_frameinfo():
  frame = inspect.currentframe()
  print(inspect.getframeinfo(frame))


print("no vars")
test_no_vars()

print("has vars")
test_vars()

print("frameinfo")
test_frameinfo()