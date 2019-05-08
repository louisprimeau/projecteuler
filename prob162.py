"""
16 choose 3
then populate w/ everything else:
15 * 16 * 16 ... for 13 numbers.
Then we have
16! / (13! * 3!) * 15 * 16^12
is the number in decimal.
Convert to hexadecimal:
use a python library. """

import operator as op
def ncr(n, r):
    r = min(r, n-r) q
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom

print((ncr(16,3) * 15 * 16**12))
