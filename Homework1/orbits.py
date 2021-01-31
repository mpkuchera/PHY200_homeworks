"""

name: orbits.py

This program converts from cartesian to polar coordinates.
Problem 2.6 from Newman's Computational Physics.

author: Jessica Jones
date created: 1/11/2018
date edited: 1/31/2021

"""


#imports



# user-defined functions
def calc_values(l1,v1):
   """
    
    Parameters
    ----------
    l1 : distance of perihelion in m
    v1 : velocity of perihelion in m/s

    Returns
    -------
    l2 : distance of aphelion in m
    v2 : velocity of aphelion in m/s
    T : period in s
    e : eccentricity

    """
    
    #complete me
    
    

    return l2, v2, T, e

def print_values(l1,v1):
    """

    Parameters
    ----------
    l1 : distance of perihelion in m
    v1 : velocity of perihelion in m/s

    Returns
    -------
    None.

    """
    
    l2, v2, T, e = calc_values(l1,v1)
    print("\nDistance at aphelion:", l2, "m")
    print("Velocity at aphelion:", v2, "m/s")
    print("Orbital period: ", T, "s")
    print("Eccentricity:", e)

def main():
    #complete me

    #part b
    
    print_values(l1,v1)
    # part c


    print_values(l1,v1)
    
    
    print_values(l1,v1)

if __name__ == "__main__":
    main()
