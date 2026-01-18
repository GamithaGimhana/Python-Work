import pdb

print('start')
x = 5

pdb.set_trace()  # Set a breakpoint here

y = 0
z = x / y  # This will raise a ZeroDivisionError

print('finish')
