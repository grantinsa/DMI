#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def mans_sinuss(x,n):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    while k < 5:
     k = k + 1
     a = a * (-1)*x*x/((2*k)*(2*k+1))
     S = S + a
    return S

x = np.arange(0.0, 6.28, 0.01)
y = np.sin(x)
yy = mans_sinuss(x,10)

plt.plot(x,y)
plt.plot(x,yy)
plt.show()

'''
k = 0
a = (-1)**0*x**1/(1)
S = a
print "a0 = %.2f S0 = %.2f"%(a,S)

while k < 3:
     k = k + 1
     a = a * (-1)*x*x/((2*k)*(2*k+1))
     S = S + a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

print "Beigas!"
'''


'''
k = k + 1
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

k = k + 1
a  = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

k = k + 1
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
'''
