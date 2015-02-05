"""Addition

   Thus far, these will only work for the natural numbers.
"""

# http://www.catonmat.net/blog/secret-perl-operators/
def inc(n):
    """Increment an integer."""
    return -~n

def dec(n):
    """Decrement an integer."""
    return ~-n


def naive_r(augend, addend):
    """A recursive definition of addition.
    (http://en.wikipedia.org/wiki/Addition#Natural_numbers)
    """
    if addend == 0:
        return augend
    return inc(naive_r(augend, dec(addend)))

# in theory this is iterative, but Python lacks tail recursion
def naive_i(augend, addend):
    if augend < addend:
        augend, addend = addend, augend
    if addend == 0:
        return augend
    return naive_i(inc(augend), dec(addend))

# gotta do it in a loop
def naive_i2(augend, addend):
    if augend < addend:
        augend, addend = addend, augend
    while addend > 0:
        augend, addend = inc(augend), dec(addend)
    return augend


def add(term1, term2):
    return naive_i2(term1, term2)


