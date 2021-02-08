"""
 This program calculates the binding energy and binding energy per 
 nucleon for a given isotope.

 author: M.P. Kuchera
 date created: 1/20/2018
 date edited: 2/2/2018 
"""

a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2

from math import sqrt


def main():
    Z = int(input("Number of protons in nucleus: "))
    A = int(input("Atomic number of nucleus: "))
    print()
    if A%2 == 1:
        a5=0.0
    elif Z%2 == 0:
        a5 = 12.0
    else:
        a5 = -12.0
    
    BE = a1*A - a2*A**(2/3)-a3*Z**2/A**(1/3) - a4*(A-2*Z)**2/A + a5/sqrt(A)
    print("Binding energy:", BE, "MeV\nBinding energy per nuleon:",BE/A,"MeV/u")

if __name__ == "__main__":
    main()