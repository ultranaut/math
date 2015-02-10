"""Helper functions."""

import math

# http://www.catonmat.net/blog/secret-perl-operators/
def inc(n):
    """Increment an integer."""
    return -~n

def dec(n):
    """Decrement an integer."""
    return ~-n

def digit_count(n, base=10):
    """Return the number of digits used to represent a number."""
    return math.ceil(math.log(n, base))

def halve(n):
    return n>>1

def double(n):
    return n<<1
