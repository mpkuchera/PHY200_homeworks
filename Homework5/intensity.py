"""

name: intensity.py

Compute and visualize diffraction of waves upon encountering a straight edge.
 
Problem 5.11 from Newman's Computational Physics.

author: Darcy Lewis
date created: 15/3/2021


"""
# Reminder: you can create other helper functions as long as the function
# behaviors below remain the same


 

# function name: C   

    """
    C(u) term of integral.

    Parameters
    ----------
    u : FLOAT
        input.

    Returns
    -------
    cc : FLOAT
        C value at u.

    """


# function name: S

    """
    S(u) term of integral.    

    Parameters
    ----------
    u : FLOAT
        input.

    Returns
    -------
    ss : FLOAT
        S value at u.

    """

# function name: I_ratio
def I_ratio(x):
    """
    Compute I ratio at given x values

    Parameters
    ----------
    x : array of FLOAT
        x values to compute diffraction.

    Returns
    -------
    I_r : array of FLOAT
        I/I0 at given x values.

    """

# function name: plot_ratio

    """
    plot I/I0 as a function of x

    Parameters
    ----------
    x : array of FLOAT
        x values.
    ratio : array of FLOAT
        I/Io.

    Returns
    -------
    None.

    """

    
def main():    

    
if __name__ == "__main__":
    main()