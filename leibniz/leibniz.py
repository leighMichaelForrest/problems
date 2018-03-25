import functools
import sys

SYMBOL = "\u03C0"

def leibniz(iterations):
    """Determine the value of pi using Gottfried Leibniz's method.
    Return a dictionary with two values:
    terms: the terms of the calculation.
    pi: The approximation of pi according to the summing of the terms, multiplied
    by 4."""
    try:
        iterations = int(iterations)
    except ValueException:
        iterations = 4

    terms = []
    for k in range(iterations):
        factor = (-1)**k/((2*k) + 1)
        terms.append(factor)

    # add terms
    summation = functools.reduce(lambda x, y: x + y, terms) * 4

    return {'pi': summation, 'terms': terms}

if __name__ == '__main__':
    iterations = int(sys.argv[1])

    pi_dict = leibniz(iterations)
    terms = pi_dict['terms']

    print(f"{SYMBOL}/ 4 = ")

    for index, value in enumerate(terms):
        print("%+0.6f" % value, end="")
        if (index + 1) % 6 == 0:
            print("")

    print(f"\n{SYMBOL} = {pi_dict['pi'] }")
