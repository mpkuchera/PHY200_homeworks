"""
name: altitude.py

This program calculates the altitude of a satellite given a desired
period of orbit, T. Problem 2.2 from Newman's Computational Physics


author: Jessica Jones
date created: 1/11/2018 
date edited: 1/31/2021

"""


#imports
from math import pi

#user-defined functions
def alt(T):
    """

    Parameters
    ----------
    T : period of orbit in seconds

    Returns
    -------
    h : altitude in meters
    
    """  
    # complete me
    
    
    return h

def ask_user():
    """

    Returns
    -------
    float
        altitude in meters for given T.

    """
    
    T = float(input("Enter the orbital period in seconds: "))    
    
    return alt(T)

# main function
def main():
    
    #part b
    h = ask_user()
    print("The height above the earth is:", h,"meters")
    print("or",h/1000,"kilometers")

    # part c
    # complete me, do NOT use ask_user()
     
 
# run this code
if __name__ == "__main__":
    main()