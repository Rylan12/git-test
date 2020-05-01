#!/usr/bin/env python

import sys

def primes_method(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + ' <num>')
        exit(1)

    primes = primes_method(int(sys.argv[1]))

    if len(primes) > 0:
        print(' '.join(str(i) for i in primes))
    else:
        print('None')
