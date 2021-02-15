"""

name: prime.py

This program finds all of the prime numbers up through N

 

Problem 2.12 from Newman's Computational Physics.

author: Monica Rambeau
date created: 1/11/2018
date edited: 2/15/2021

"""

# imports here


# part a: function name: primes_a

    """
    Finds prime numbers up to N 

    Parameters
    ----------
    N : INT
        Find prime numbers up to this value

    Returns
    -------
    prime_list : LIST of INTs
        list of prime numbers up to N
    """

 
    
# part b: function name: primes_b

    """
    Finds prime numbers up to N 

    Parameters
    ----------
    N : INT
        Find prime numbers up to this value

    Returns
    -------
    prime_list : LIST of INTs
        list of prime numbers up to N
    """


  
# part c: function name: primes_c

    """
    Finds prime numbers up to N 

    Parameters
    ----------
    N : INT
        Find prime numbers up to this value

    Returns
    -------
    prime_list : LIST of INTs
        list of prime numbers up to N
    """
 
    
 
def main():
    # a smaller N is easier for developing / debugging!
    N = 10000
    
    # the following should all give the same results, but each one is faster to
    # compute than the previous
    print("The primes up to", N, "are", primes_a(N))
    print("The primes up to", N, "are", primes_b(N))
    print("The primes up to", N, "are", primes_c(N))
    
if __name__ == "__main__":
    main()
