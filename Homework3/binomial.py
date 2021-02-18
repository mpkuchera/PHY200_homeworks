"""

name: binomial.py

 This program calculates probabilities of coin flips

Problem 2.11 from Newman's Computational Physics.

author: Monica Rambeau
date created: 2/6/2018
date edited: 2/15/2021

"""



# part a: function name: binomial

    """
    Finds the binomial coefficient for n and k

    Parameters
    ----------
    n : INT

    k : INT


    Returns
    -------
    INT
        binomial coefficient
    """


# part b: function name: pascal_triangle

    """
    Prints N rows of Pascal's triangle

    Parameters
    ----------
    N : INT
        Number of rows in the triangle

    Returns
    -------
    None.

    """


#c-a: function name: prob

    """
    Calculates the probability of tossing n_heads out of n_tosses

    Parameters
    ----------
    n_tosses : INT
        number of tosses
    n_heads : INT
        number of heads

    Returns
    -------
    FLOAT
        probability
    """



#c-b: function name: prob_more_than

    """
    Calculates the probability of tossing n_heads or more out of n_tosses

    Parameters
    ----------
    n_tosses : INT
        number of tosses
    n_heads : INT
        number of heads

    Returns
    -------
    FLOAT
        probability
    """


def main():
    # some examples of using the functions

    print(binomial(5,2))

    pascal_triangle( 20)


    toss = 100
    heads = 60

    print("the probability of exactly 60 heads is:",prob(toss,heads))


    print("the probability of 60 or more heads is:",prob_more_60(heads,toss))

if __name__ == "__main__":
    main()
