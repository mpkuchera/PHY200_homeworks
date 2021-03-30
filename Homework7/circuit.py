#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:52:49 2017

@author: mikuchera
"""


Vp = 5. #V
R1 = 1000. #Ohm
R2 = 4000. #Ohm
R3 = 3000. #Ohm
R4 = 2000. #Ohm
I0 = 3e-9 #A
VT = 0.05 #V

from math import exp, sqrt, log
from numpy import array
from numpy.linalg import solve


def main():
    V = array([1.,1.], float)
    accuracy = 1e-2
    err = 1.
    while abs(err) > accuracy:
         #   if count > 100:
            #    break
            #count += 1
            Vprev = V
            V1 = V[0]
            V2 = V[1]
            x = exp((V1-V2)/VT)*I0/VT
            a11 = 1/R1 + 1/R2 + x
            a12 = -x
            a21 = -x
            a22 = 1/R3 + 1/R4 + x
            A = array([[a11, a12],[a21, a22]], float)
            b1 = (V1-Vp)/R1 +V1/R2 + I0*(exp((V1-V2)/VT)-1)
            b2 = (V2-Vp)/R3 +V2/R4 - I0*(exp((V1-V2)/VT)-1)
            b = array([b1,b2],float)
            #print("b = ",b)
            dV = solve(A,b)
            #print(dV)
            #print("dV = ",dV)
            V = Vprev - dV
            #print("V =",V)
            err = sqrt(dV[0]**2+dV[1]**2)
            #print("err =",err)
    print(V)
    
if __name__ == "__main__":
    main()



