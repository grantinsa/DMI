# -*- coding: utf-8 -*-
# print formāti - balstās uz C valodas f.
# http://www.cplusplus.com/reference/cstdio/printf

import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    while k < 500:
     k = k + 1
     R = (-1)*x*x/((2*k)*(2*k+1))
     a = a * R
     S = S + a
    return S

a = 0
b = 3 * np.pi
x = np.arange(a,b,0.05)
y =  mans_sinuss (x)
plt.plot(x,y)
plt.grid()
#plt.show()
 
n = len(x)
y_prim = []
for i in range(n-1):
    print i, x[i], y[i]
    delta_y = y[i+1] -y[i]
    delta_x = x[i+1] -x[i]
    #y_prim = delta_y/delta_x
    y_prim.append(delta_y/delta_x)

plt.plot(x[:n-1],y_prim)        
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
