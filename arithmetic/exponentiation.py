"""Exponentiation """

def root(rad, n=2):
    ret = 1.0
    generator = (lambda x: (((n-1) * x**n) + rad) / (n * x**(n-1)))
    while True:
        _next = generator(ret)
        if abs(_next - ret) < 10e-8:
            return ret
        ret = _next
