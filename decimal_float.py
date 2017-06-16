##This script shows the "error?" in storing floating point decimals
##in memory as an approximation in binary representation by summing
##0.1 and 0.2 one million times to extrapolate the error value.

from decimal import *
import time

s = Decimal(0)
x = Decimal(0.1)
y = Decimal(0.2)
t = time.time()

for v in range(0,10):
    s =  s + x + y
print "looping took {} seconds".format(time.time()-t)
print s
