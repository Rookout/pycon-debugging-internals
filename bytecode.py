import dis

def multiply(a, b):
    result = a * b
    return result

print dis.dis(multiply)