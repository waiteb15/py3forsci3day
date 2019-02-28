#!/usr/bin/env python

import numba

@numba.jit() # <1>
def get_primes(kmax):
    primes = [0] * kmax
    result = []
    k = 0
    current_prime = 2
    while k < kmax:
        i = 0
        while i < k and current_prime % primes[i] != 0:
            i = i + 1
        if i == k:
            primes[k] = current_prime
            k = k + 1
            result.append(current_prime)
        current_prime = current_prime + 1
    return result

if __name__ == '__main__':
    primes_list = get_primes(1000)
    print(primes_list)
