"""

name: madelung.py

This program calculates the Madelung constant for sodium chloride

Problem 2.5 from Newman's Computational Physics.

author: Wanda Maximoff
date created: 2/2/2018
date edited: 2/7/2021

"""

def m_constant(L):
    """
    calculates the Madelung constant for 2L+1 atoms

    Parameters
    ----------
    L : integer
        Use 2L+1 atoms in calculation

    Returns
    -------
    m : float
        Madelung constant for sodium chloride

    """
    
    # complete me
    
    
    
    return m


def main():
    # make sure to choose a large enough L
    L = 3
    M = m_constant(L)
    print("the Madelung constant for L =", L, "is ", M)
    
    
if __name__ == "__main__":
    main()