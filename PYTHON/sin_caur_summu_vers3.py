#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sin

# a0, a1, a2, a3
# S0, S1, S2, S3 -> S

x = 1. * input ("Lietotāj, lūdzu, ievadi argumentu (x): ")
#x = float("Lietotāj, lūdzu, ievadi argumentu (x): "))

y = sin(x) 
print "sin(%.2f) = %.2f"%(x,y)

#a0 = (-1)**0*x**1/(1)
#S = a0
S = a
print "a0 = %.2f S0 = %.2f"%(a,S)

#a1 = (-1)**1*x**3/(1*2*3)
a = 1a * (-1)*x*x/(2*3)
S = S + a
print "a1 = %.2f S1 = %.2f"%(a,S)

#a2 = (-1)**2*x**5/(1*2*3*4*5)
a  = a * (-1)*x*x/(4*5)
S = S + a
print "a2 = %.2f S2 = %.2f"%(a,S)

#a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
a = a * (-1)*x*x/(6*7)
S = S + a
print "a3 = %.2f S3 = %.2f"%(a,S)
