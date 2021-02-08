"""
 This program calculates the most stable isotope for a given element
 and the overall most stable element.

 author: M.P. Kuchera
 date created: 1/20/2018
 date edited: 2/5/2018 
"""

# imports here
from math import sqrt

# user-defned functions here


# main function here
def main():
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2

    max_BA = -9999.
    max_Z = 0
    
    for Z in range(1,101):
        max_BA_Z = -9999.
        max_A_Z = 0
        for A in range(Z,3*Z+1):
            if A%2 == 1:
                a5=0.0
            elif Z%2 == 0:
                a5 = 12.0
            else:
                a5 = -12.0
            
            B = a1*A - a2*A**(2/3)-a3*Z**2/A**(1/3) - a4*(A-2*Z)**2/A + a5/sqrt(A)
            BA = B/A
            if BA > max_BA:
                max_BA = BA
                max_Z = Z
            if BA > max_BA_Z:
                max_BA_Z = BA
                max_A_Z = A
        print("For Z =", Z, "the most stable A is", max_A_Z, "with a BE/A =", max_BA_Z)
    print("\n\nThe most stable element has Z =",max_Z, "with a binding energy per" +
         "nucleon of", max_BA, "MeV/u")

# run main() iff we are executing THIS file
if __name__ == "__main__":
    main()