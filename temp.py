from calc import *

a = "1-2^(3+12)"

try:
	calculate(a)
except KeyError:
	print 'Please check name of your functions'
except ZeroDivisionError:
	print 'You try to divide by zero!'
