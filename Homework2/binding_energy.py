"""

name: semi_empirical.py

 This program calculates the most stable isotope for a given element
 and the overall most stable element.

Problem 2.10 from Newman's Computational Physics.

author: Wanda Maximoff
date created: 2/2/2018
date edited: 2/7/2021

"""


# import statements


# user-defned functions
def largest_BE_A(Z):
    """
    Computes the most stable isotope for a given element (part c).

    Parameters
    ----------
    Z : integer
        number of protons.

    Returns
    -------
    A : int
        number of nucleons for most stable isotope with Z protons.

    """
    
    
    
    return A

def most_stable():
    """
    Prints most stable A for each Z from 1 to 100 (part d) and returns the
    overall most stable Z.

    Returns
    -------
    Z : int
        number of protons for overall most stable element.

    """
    
    
    
    
    return Z

# main function 
def main():
    
    # part c. try with various number of protons
    Z = 28
    A = largest_BE_A(Z)
    print("the most stable isotope with", Z, "protons has", A, "nucleons.")
    
    # part c.
    print("The most stable element has", most_stable(), "protons.")

# run main() iff we are executing THIS file
if __name__ == "__main__":
    main()